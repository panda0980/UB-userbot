import time
from pyrogram import Client  
from Config import API_HASH, API_ID, SESSION

HELP = {}
CMD_HELP = {}

StartTime = time.time()

UBbot = Client(SESSION, api_id=API_ID, api_hash=API_HASH)



print("UB started")

if __name__ == "__main__":
    UBbot.run()
