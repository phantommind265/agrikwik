from flask import Flask, request
import requests
import os
from dotenv import load_dotenv
from bot_logic import handle_message

load_dotenv()
app = Flask(__name__)

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")


@app.route("/gupshup/webhook", methods=["POST"])
def gupshup_webhook():
    sender = request.form.get("sender")
    message = request.form.get("message")

    if not sender or not message:
        return "OK"
    reply = handle_message(sender, message)
    send_whatsapp_message(sender, reply)
    return "OK"

# Verify Webhook
@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    return "Verification failed", 403

# Receive Messages
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    try:
        message = data["entry"][0]["changes"][0]["value"]["messages"][0]
        sender = message["from"]
        text = message["text"]["body"]

        reply = handle_message(text, sender)
        send_message(sender, reply)

    except KeyError:
        pass
    return "OK", 200

# Send Message
def send_message(to, text):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "text": {"body": text}
    }
    requests.post(url, headers=headers, json=payload)

if __name__ == "__main__":
    app.run(port=5000, debug=True)

