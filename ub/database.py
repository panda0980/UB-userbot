"""
from motor.motor_asyncio import AsyncIOMotorClient

mongodb = AsyncIOMotorClient()
UBbot_db = mongodb["UBbotd"]
"""
import pymongo
from Config import MONGO_URI

UB_db = pymongo.MongoClient(MONGO_URI)

collection = UB_db["UB"]["pm_guard"]

#add users in APPROVED_USERS list
async def add_approved(user_id):
    user =int(user_id)
    user_check = await collection.find_one({"_id": "APPROVED_USERS"})
    if user_check:
        await collection.update_one({"_id":"APPROVED_USERS"},{"$push":{"user_id":user}})
    else:
        await collection.insert_one({"_id":"APPROVED_USERS", "user_id":[user]})

#remove users from APPROVED_USERS list
async def remove_approved(user_id):
    user = int(user_id)
    user_check = await collection.find_one({"_id":"APPROVED_USERS"})
    if user_check:
        await collection.update_one({"_id":"APPROVED_USERS"},{"$pull":{"user_id":user}})
    else:
        return None

#check users in APPROVED_USERS list
async def check_approved (user_id):
    user = int(user_id)
    approved_user = await collection.find_one({"_id": "APPROVED_USERS"})
    if approved_user:
        user_list = [users for users in approved_user.get("user_id")]
        if user in user_list:
            return True
        else:
            return False
    else:
        return False
