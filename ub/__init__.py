import time
from pyrogram import Client  
from Config import API_HASH, API_ID, SESSION

HELP = {}
CMD_HELP = {}

StartTime = time.time()



UBbot = Client(
    "UB-userbot",
    api_hash=API_HASH,
    api_id=API_ID,
    session_string=SESSION,
    sleep_threshold=10,
)
