import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH")
OWNER_ID = int(os.getenv("OWNER_ID", 0))

# Website
SITE_URL = os.getenv("SITE_URL")

# Check interval (seconds)
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 300))

# Database
DATABASE_NAME = "data/notifier.db"
