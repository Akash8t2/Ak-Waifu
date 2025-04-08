from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client.waifubot

def update_memory(user_id, message):
    history = db.memory.find_one({"user_id": user_id}) or {"messages": []}
    history["messages"].append(message)
    history["messages"] = history["messages"][-10:]
    db.memory.update_one({"user_id": user_id}, {"$set": {"messages": history["messages"]}}, upsert=True)

def get_memory(user_id):
    data = db.memory.find_one({"user_id": user_id})
    return data["messages"] if data else []