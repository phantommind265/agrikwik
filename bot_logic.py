from sessions import get_session, update_session, reset_session
from database import add_user, user_exists, get_user

# Messages
WELCOME_MSG = (
    "Welcome to AgriKwik!\n\n"
    "Your digital agriculture marketplace.\n"
    "Buy farm inputs, rent equipment, and connect with trusted agro-suppliers — safely and easily.\n\n"
    "Tap the *AgriKwik Menu* button below to get started 👇\n"
    "1️⃣ Sign Up\n2️⃣ Already a Customer\n3️⃣ Talk to Support"
)

MAIN_MENU = (
    "AgriKwik Main Menu\n\n"
    "1️⃣ Official Store\n2️⃣ Agro-dealers\n3️⃣ Lend & Share"
)

def handle_message(message, sender):
    msg = message.strip()
    session = get_session(sender)
    state = session["state"]

    # Universal greeting reset & some should be added
    if msg.lower() in ["hi", "hello"]:
        reset_session(sender)
        return WELCOME_MSG

    # START: Ask user to choose signup/login/support
    if state == "START":
        if msg == "1":
            session["state"] = "SIGNUP_USERNAME"
            return "Please enter your username:"
        elif msg == "2":
            session["state"] = "LOGIN_PHONE"
            return "Please enter your registered phone number:"
        elif msg == "3":
            session["state"] = "SUPPORT"
            return "Please wait, an AgriKwik agent will assist you shortly 👨‍💼"
        else:
            return "Invalid option. Please reply with 1, 2, or 3."

    if state == "MAIN_MENU":
    if msg == "1":
        session["state"] = "OFFICIAL_STORE_MENU"
        return (
            "📋 Official Store\n\n"
            "1️⃣ Fertilizer\n"
            "2️⃣ Seeds\n"
            "3️⃣ Agro-chemicals\n"
            "4️⃣ Animal Feed\n"
            "5️⃣ Farm Tools\n\n"
            "AgriKwik"
        )
    elif msg == "2":
        session["state"] = "AGRO_DEALERS_MENU"  # Placeholder for next step
        return "Agro-dealers functionality coming soon."
    elif msg == "3":
        session["state"] = "LEND_SHARE_MENU"    # Placeholder for next step
        return "Lend & Share functionality coming soon."
    else:
        return "Invalid option. Please select 1, 2, or 3."

# Handle Official Store Menu selection
if state == "OFFICIAL_STORE_MENU":
    categories = {
        "1": "Fertilizer",
        "2": "Seeds",
        "3": "Agro-chemicals",
        "4": "Animal Feed",
        "5": "Farm Tools"
    }
    if msg in categories:
        session["state"] = "OFFICIAL_STORE_CATEGORY"
        session["data"]["store_category"] = categories[msg]
        return f"You selected *{categories[msg]}* 📦.\n(Product list coming soon)\nReply *menu* to return to main menu."
    else:
        return (
            "Invalid option. Please select a category:\n"
            "1️⃣ Fertilizer\n2️⃣ Seeds\n3️⃣ Agro-chemicals\n4️⃣ Animal Feed\n5️⃣ Farm Tools"
        )

    if state == "MAIN_MENU":
    if msg == "1":
        session["state"] = "OFFICIAL_STORE_MENU"
        return (
            "📋 Official Store\n\n"
            "1️⃣ Fertilizer\n2️⃣ Seeds\n3️⃣ Agro-chemicals\n4️⃣ Animal Feed\n5️⃣ Farm Tools\n\n"
            "AgriKwik"
        )
    elif msg == "2":
        session["state"] = "AGRO_DEALERS_MENU"
        return (
            "📋 Agro-dealers\n\n"
            "1️⃣ Fertilizer\n2️⃣ Seeds\n3️⃣ Chemicals\n4️⃣ Tools\n5️⃣ Animal Feed\n\n"
            "AgriKwik"
        )
    elif msg == "3":
        session["state"] = "LEND_SHARE_MENU"    # Placeholder for next step
        return "Lend & Share functionality coming soon."
    else:
        return "Invalid option. Please select 1, 2, or 3."

# Handle Agro-dealers Menu selection
if state == "AGRO_DEALERS_MENU":
    categories = {
        "1": "Fertilizer",
        "2": "Seeds",
        "3": "Chemicals",
        "4": "Tools",
        "5": "Animal Feed"
    }
    if msg in categories:
        session["state"] = "AGRO_DEALERS_CATEGORY"
        session["data"]["agro_category"] = categories[msg]
        return f"You selected *{categories[msg]}* 📦.\n(Dealer list coming soon)\nReply *menu* to return to main menu."
    else:
        return (
            "Invalid option. Please select a category:\n"
            "1️⃣ Fertilizer\n2️⃣ Seeds\n3️⃣ Chemicals\n4️⃣ Tools\n5️⃣ Animal Feed"
        )

    if state == "MAIN_MENU":
    if msg == "1":
        session["state"] = "OFFICIAL_STORE_MENU"
        return (
            "📋 Official Store\n\n"
            "1️⃣ Fertilizer\n2️⃣ Seeds\n3️⃣ Agro-chemicals\n4️⃣ Animal Feed\n5️⃣ Farm Tools\n\n"
            "AgriKwik"
        )
    elif msg == "2":
        session["state"] = "AGRO_DEALERS_MENU"
        return (
            "📋 Agro-dealers\n\n"
            "1️⃣ Fertilizer\n2️⃣ Seeds\n3️⃣ Chemicals\n4️⃣ Tools\n5️⃣ Animal Feed\n\n"
            "AgriKwik"
        )
    elif msg == "3":
        session["state"] = "LEND_SHARE_MENU"
        return (
            "📋 Lend & Share\n\n"
            "1️⃣ Tractors\n2️⃣ Ploughs\n3️⃣ Sprayers\n4️⃣ Irrigation Equipment\n5️⃣ Transport & Storage\n\n"
            "AgriKwik"
        )
    else:
        return "Invalid option. Please select 1, 2, or 3."

    # Handle Lend & Share Menu selection
if state == "LEND_SHARE_MENU":
    categories = {
        "1": "Tractors",
        "2": "Ploughs",
        "3": "Sprayers",
        "4": "Irrigation Equipment",
        "5": "Transport & Storage"
    }
    if msg in categories:
        session["state"] = "LEND_SHARE_CATEGORY"
        session["data"]["lend_share_category"] = categories[msg]
        return f"You selected *{categories[msg]}* 🚜.\n(Availability coming soon)\nReply *menu* to return to main menu."
    else:
        return (
            "Invalid option. Please select a category:\n"
            "1️⃣ Tractors\n2️⃣ Ploughs\n3️⃣ Sprayers\n4️⃣ Irrigation Equipment\n5️⃣ Transport & Storage"
        )


    # SIGNUP FLOW
    if state == "SIGNUP_USERNAME":
        session["data"]["username"] = msg
        session["state"] = "SIGNUP_LOCATION"
        return "Enter your location:"

    if state == "SIGNUP_LOCATION":
        session["data"]["location"] = msg
        session["state"] = "SIGNUP_EMAIL"
        return "Enter your email address:"

    if state == "SIGNUP_EMAIL":
        session["data"]["email"] = msg
        # Save user
        add_user(sender, session["data"]["username"], session["data"]["location"], session["data"]["email"])
        session["state"] = "MAIN_MENU"
        return f"✅ Registration Successful!\nWelcome {session['data']['username']} \n\n" + MAIN_MENU

    # LOGIN FLOW
    if state == "LOGIN_PHONE":
        if user_exists(msg):
            user = get_user(msg)
            session["state"] = "MAIN_MENU"
            session["data"]["username"] = user[2]
            return f"✅ Login Successful!\nWelcome back {user[2]} 🌱\n\n" + MAIN_MENU
        else:
            session["state"] = "START"
            return "Phone number not found. Please sign up first.\n\n" + WELCOME_MSG

    # MAIN MENU (After login)
    if state == "MAIN_MENU":
        if msg in ["1", "2", "3"]:
            return f"You selected option {msg}. (Functionality coming soon)"
        else:
            return "Invalid option. Please select 1, 2, or 3."

    # SUPPORT
    if state == "SUPPORT":
        return "Please wait, an AgriKwik agent will assist you shortly 👨‍💼"

    return "Something went wrong. Reply 'hi' to start over."

