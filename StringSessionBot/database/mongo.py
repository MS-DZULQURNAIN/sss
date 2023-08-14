from pymongo import MongoClient
from config import MONGO_URL, MONGO_DB

MongoClient 

async def cek(user_id : int):
    ada = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return
