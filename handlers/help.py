from pyrogram import Client
from pyrogram.types import Message


async def help_command(client: Client, message: Message):
    await message.reply_text(
        """
📚 **TamilMV Notifier Help**

Available Commands:

/start - Start the bot
/help - Show this help message
/latest - Show the latest uploads
/status - Show bot status

🤖 The bot automatically checks for new uploads and will notify you when a new post is detected.
"""
    )
