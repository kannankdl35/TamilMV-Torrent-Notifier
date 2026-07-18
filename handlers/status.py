from datetime import datetime

from pyrogram import Client
from pyrogram.types import Message

from config import SITE_URL, CHECK_INTERVAL


async def status_command(client: Client, message: Message):
    await message.reply_text(
        f"""
🟢 **Bot Status**

Status: Running

🌐 Website:
{SITE_URL}

⏱ Check Interval:
{CHECK_INTERVAL} seconds

🕒 Server Time:
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

⚠️ Last Scan:
Not available yet
"""
    )
