import requests

def get_chatbot_reply(message, user_id):
    url = f"https://mukesh-api.vercel.app/chatbot?message={message}&uid={user_id}"
    response = requests.get(url)
    return response.json().get("reply", "Hmm...")