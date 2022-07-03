from pyrogram import idle, Client, filters
from pyrogram.types import Message
from ub import UBbot, LOGGER
import os


botcommand = "."

@UBbot.on_message(filters.command("alive", botcommand))
async def start_message(Client, message:Message):
    Client.send_message("me", "UBbot succefully started")




if __name__ == "__main__":
  UBbot.run()
  
