import json
import random
import pickle
from datetime import datetime

user_info = {
    "name": None,
    "phone": None
}

def days_until(event_name):
    today = datetime.now()
    events = {
        "new year": datetime(today.year + 1, 1, 1),
        "christmas": datetime(today.year, 12, 25),
        "independence day": datetime(today.year, 8, 15)
    }

    for key in events:
        if key in event_name.lower():
            event_date = events[key]
            if event_date < today:
                event_date = event_date.replace(year=event_date.year + 1)
            delta = (event_date - today).days
            return f"There are {delta} days until {key.title()}."

    return "I'm not sure about that date."

def get_response(user_input):
    if not user_info["name"]:
        user_info["name"] = user_input
        return f"Nice to meet you, {user_info['name']}! Can you please provide your phone number?"

    if not user_info["phone"]:
        user_info["phone"] = user_input
        return f"Thanks {user_info['name']}! How can I assist you today?"

    if "how many days" in user_input.lower() or "how long until" in user_input.lower():
        return days_until(user_input)

    with open("chatbot_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("intents.json") as f:
        data = json.load(f)

    intent = model.predict([user_input])[0]

    for i in data["intents"]:
        if i["tag"] == intent:
            return random.choice(i["responses"])

    return "Sorry, I didn't understand that."
