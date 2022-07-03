import time
from pyrogram import Client, filters
from pyrogram.types import Message
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
    "UB-userbot",
    api_hash=API_HASH,
    api_id=API_ID,
    session_string=SESSION,
    sleep_threshold=10,
    plugins={
                "root": "ub"
            },
)

botcommand = "."

@UBbot.on_message(filters.command("alive", botcommand))
async def start_message(Client, message:Message):
    await Client.send_message(message.chat.id, "UBbot succefully started")
   


if __name__ == "__main__":
  UBbot.run()
