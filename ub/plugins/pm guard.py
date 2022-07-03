import os
from pyrogram import filters
from pyrogram.types import Message
from bot import UBbot
from ub.helper.database import add_approved, remove_approved, check_approved

PMPERMIT_MESSAGE = ("""
    This is PM Security of {} 🛑
    You are contactng my master pm.you not yet approved to msg my master
    `Please wait for my Master to come back Online.\n\n`
    `Until then, Don't spam, Or you'll get **blocked and reported!**\n\n`
    you have only {} if you you excedding {} you willbe blocked  
    """
)
PM_WARNS ={}
PM_MSGS = {}
DEFAULT_PM_LIMIT = 3

botcommand = "."

@UBbot.on_message(filters.command("a","approve", botcommand))
async def approve_user(_, message:Message):
    msg = await message.reply_text("Processing....")
    chat_type = message.chat.type
    if chat_type == "me":
        return await msg.edit("It is not correct way, you can not approve yourself")
    elif chat_type == ["group", "supergroup"]:
        if not message.reply_to_message:
            return await msg.edit("Reply to the user message to approve ")
        users_id = message.reply_to_message.from_user.id
    elif chat_type == "private":
        users_id = message.from_user.id
    else:
        return 

    approved = await check_approved(users_id)
    if approved:
        return await msg.edit("User already approved")
    await add_approved(users_id)
    if users_id in PM_WARNS:
        PM_WARNS.pop(users_id)
        try:
            await UBbot.delete_messages(chat_id=users_id, message_id=PM_MSGS[users_id])
        except:
            pass

    await msg.edit("You are allow to PM my **Master** here after")
    

@UBbot.on_message(filters.command("da","disapprove", botcommand))
async def remove_user(_, message:Message):
    msg = await message.reply_text("Processing....")

    chat_type = message.chat.type
    if chat_type == "me":
        return await msg.edit("it is not correct way, you can not disapprove yourself")
    elif chat_type == ["group", "supergroup"]:
        if not message.reply_messsage:
            return await msg.edit("Reply to user to disapprove")
        users_id = message.reply_to_message.from_user.id

    elif chat_type == "private":
        users_id = message.from_user.id
    else:
        return
    approved = await check_approved(users_id)
    if not approved:
        return await msg.edit("This users not even approved to remove")

    await remove_approved(users_id)
        
    await msg.edit("You are not allow to PM my **Master**")

    

@UBbot.on_message(
    filters.private
    & filters.incoming
    & ~filters.service
    & ~filters.me
    & ~filters.bot
)
async def reply_pm(client, message):
    user = message.from_user
    master = UBbot.get_me()
    check_user = await check_approved(user.id)
    if check_user:
        return
    if user.is_fake or user.is_scam:
        await message.reply("you are look like spammer. blocking you")
        return await UBbot.block_user(user.id)

    if user.is_support or user.is_verified or user.is_self:
        return
    
    if user.id in PM_WARNS:

        try:
            if message.chat.id in PM_MSGS:
                await UBbot.delete_messages(chat_id = message.chat.id, message_ids = PM_MSGS[message.chat.id])
        except:
            pass
        PM_WARNS[user.id] += 1
        if PM_WARNS[user.id] >= DEFAULT_PM_LIMIT:
            await message.reply("your are exceeding the actual pm limit. DOn't pm my master. i have blocked you 😑 ") 
            return await UBbot.block_user(user.id)  
        else:
            reply_msg = await message.reply_text(PMPERMIT_MESSAGE.format(master.mention, PM_WARNS[user.id], DEFAULT_PM_LIMIT))

    else:
        PM_WARNS[user.id] = 1
        reply_msg = await message.reply_text(PMPERMIT_MESSAGE.format(master.mention, PM_WARNS[user.id], DEFAULT_PM_LIMIT))

    PM_MSGS[message.chat.id] = [reply_msg.id]







