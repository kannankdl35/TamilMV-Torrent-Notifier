from pyrogram import Client
from pyrogram.types import Message

from config import SITE_URL, CHECK_INTERVAL


async def start_command(client: Client, message: Message):
    text = f"""
👋 **Welcome to TamilMV Notifier Bot**

This bot monitors TamilMV for new uploads and notifies you instantly.

📡 Website:
{SITE_URL}

⏱ Check Interval:
{CHECK_INTERVAL} seconds

Available Commands:

/latest - Show latest uploads
/status - Bot status
/help - Help
"""

    await message.reply_text(text)
