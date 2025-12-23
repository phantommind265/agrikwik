user_sessions = {}

def get_session(phone):
    if phone not in user_sessions:
        user_sessions[phone] = {
            "state": "START",
            "data": {}
        }
    return user_sessions[phone]

def update_session(phone, key, value):
    if phone not in user_sessions:
        get_session(phone)
    user_sessions[phone][key] = value

def reset_session(phone):
    user_sessions[phone] = {
        "state": "START",
        "data": {}
    }

