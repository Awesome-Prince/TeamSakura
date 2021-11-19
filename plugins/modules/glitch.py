import os
import glitchart
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_TEXT = """
Hello I am a photo to glitch art Module Created By @SakuraBotSupport

Made by @SakuraBotUpdates
"""
START_BUTTONS = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('Channel', url='https://telegram.me/FayasNoushad'),
        InlineKeyboardButton('Feedback', url='https://telegram.me/TheFayas')
    ]]
)
PATH = os.environ.get("PATH", "./DOWNLOADS")

@Bot.on_message(filters.private & filters.command(["glitch"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.photo)
async def glitch_art(bot, update):
    download_path = PATH + "/" + str(update.from_user.id) + "/"
    download_location = download_path + "photo.jpg"
    message = await update.reply_text(
        text="`Processing...`",
        quote=True
    )
    try:
        await update.download(
            file_name=download_location
        )
    except Exception as error:
        await message.edit_text(
            text=f"**Error :** `{error}`\nContact @SakuraBotSupport"
        )
        return 
    await message.edit_text(
        text="`Converting to glitch...`"
    )
    try:
        glitch_art = glitchart.jpeg(download_location)
        await update.reply_photo(photo=glitch_art, quote=True)
        os.remove(download_location)
        os.remove(glitch_art)
    except Exception as error:
        await message.edit_text(
            text=f"**Error :** `{error}`\nContact @SakuraBotUpdates"
        )
        return
    await message.delete()