import requests

GUPSHUP_API_KEY = "sk_87281b6777f042d785e4caae1871dbd5"
APP_NAME = "Agrikwik"

def send_whatsapp_message(to, text):
    url = "https://api.gupshup.io/sm/api/v1/msg"
    headers = {
            "apikey": GUPSHUP_API_KEY
            }
    payload = {
            "channel": "whatsapp",
            "source": APP_NAME,
            "destination": to,
            "message": text,
            "src.name": APP_NAME
            }
    requests.post(url, headers=headers, data=payload)
