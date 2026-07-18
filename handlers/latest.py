from pyrogram import Client
from pyrogram.types import Message


async def latest_command(client: Client, message: Message):
    await message.reply_text(
        "🚧 Latest uploads feature is under development.\n\nSoon this command will display the latest 10 uploads from TamilMV."
    )
