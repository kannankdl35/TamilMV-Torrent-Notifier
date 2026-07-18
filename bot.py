from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.filters import command

from config import BOT_TOKEN, API_ID, API_HASH
from handlers.start import start_command
from handlers.help import help_command
from handlers.latest import latest_command
from handlers.status import status_command

app = Client(
    "TamilMVNotifier",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

app.add_handler(MessageHandler(start_command, command("start")))
app.add_handler(MessageHandler(help_command, command("help")))
app.add_handler(MessageHandler(latest_command, command("latest")))
app.add_handler(MessageHandler(status_command, command("status")))

if __name__ == "__main__":
    print("🚀 TamilMV Notifier Bot Started...")
    app.run()
