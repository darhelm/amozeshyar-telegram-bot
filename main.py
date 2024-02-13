#!/usr/bin/python

from convert_text import convert_persian_for_db
from pyrogram.handlers import MessageHandler
from dotenv import load_dotenv
from pyrogram import filters
import pyrogram
import os

# Get bot token
load_dotenv(".env")
TOKEN = os.environ["TOKEN"]
API_ID = os.environ["API_ID"]
API_HASH = os.environ["API_HASH"]

proxy = {
    "scheme": "socks5",  # "socks4", "socks5" and "http" are supported
     "hostname": "127.0.0.1",
     "port": 1080,
     
}

# set proxy=proxy if you are deploying on an iranian server
app = pyrogram.Client(name="Amoozeshyar Converter", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, proxy=proxy)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("به ربات تغییر متن آموزشیار خوش آمدید.متن خود را ارسال کنید تا نسخه تبدیل شده برای شما ارسال شود.")

@app.on_message()
async def text_converter(client, message):
    await message.reply_text(convert_persian_for_db(message.text))



app.run()
