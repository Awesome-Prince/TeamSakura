from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from database.users_chats_db import db
from utils import temp


async def banned_users(_, client, message: Message):
    return (
        message.from_user is not None or not message.sender_chat
    ) and message.from_user.id in temp.BANNED_USERS


banned_user = filters.create(banned_users)


async def disabled_chat(_, client, message: Message):
    return message.chat.id in temp.BANNED_CHATS


disabled_group = filters.create(disabled_chat)


@Client.on_message(filters.private & banned_user)
async def ban_reply(bot, message):
    ban = await db.get_ban_status(message.from_user.id)
    await message.reply(
        f'Sorry Dude, You are Banned to use be. \nBan Reason: {ban["ban_reason"]}'
    )


@Client.on_message(filters.group & disabled_group)
async def grp_bd(bot, message):
    buttons = [[InlineKeyboardButton("Support", url="https://t.me/EvaMariaSupport")]]
    reply_markup = InlineKeyboardMarkup(buttons)
    vazha = await db.get_chat(message.chat.id)
    k = await message.reply(
        text=f"CHAT NOT ALLOWED 🐞\n\nMy admins has restricted me from working here ! If you want to know more about it contact support..\nReason : <code>{vazha['reason']}</code>.",
        reply_markup=reply_markup,
    )
    try:
        await k.pin()
    except:
        pass
    await bot.leave_chat(message.chat.id)
