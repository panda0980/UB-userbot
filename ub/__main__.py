from pyrogram import Client, filters
from pyrogram.types import Message
from ub import UBbot


botcommand = "."

@UBbot.on_message(filters.command("alive", botcommand))
async def start_message(Client, message:Message):
    await Client.send_message(message.chat.id, "UB-userbot succefully started")
   


print("UB started")

if __name__ == "__main__":
    UBbot.run()
