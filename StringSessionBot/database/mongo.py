import pymongo, os
from config import MONGO_URI, DB_NAME


dbclient = pymongo.MongoClient(MONGO_URI)
database = dbclient[DB_NAME]

user_data = database['users']


async def cek(user_id : int):
    ada = user_data.find_one({'id': user_id})
    return bool(ada)

async def add(user_id: int):
    user_data.insert_one({'id': user_id})
    return
