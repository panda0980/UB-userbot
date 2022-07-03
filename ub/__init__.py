import time
from pyrogram import Client  
from Config import SESSION, API_ID, API_HASH
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

LOGGER = logging.getLogger("pyrogram").setLevel(logging.WARNING)

HELP = {}
CMD_HELP = {}

StartTime = time.time()



UBbot = Client(
    api_hash=API_HASH,
    api_id=API_ID,
    session_string=SESSION,
    sleep_threshold=10
)
