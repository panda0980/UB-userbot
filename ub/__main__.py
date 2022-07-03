from pyrogram import idle, Client, filters
from pyrogram.types import Message
from ub import UBbot, LOGGER
import os


botcommand = "."

@UBbot.on_message(filters.command("alive", botcommand))
async def start_message(Client, message:Message):
    await Client.send_message(message.chat.id, "UBbot succefully started")
    LOGGER.warning("userbot succesfully running")




if __name__ == "__main__":
  UBbot.run()
  
