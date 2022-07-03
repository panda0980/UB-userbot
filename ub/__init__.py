import time
from pyrogram import Client  
from Config import API_HASH, API_ID, SESSION
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

LOGGER = logging.getLogger("pyrogram").setLevel(logging.WARNING)

HELP = {}
CMD_HELP = {}

StartTime = time.time()



UBbot = Client("UBbot",
               SESSION, 
               api_id=API_ID, 
               api_hash=API_HASH)
