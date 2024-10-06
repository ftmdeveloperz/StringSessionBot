import os
from dotenv import load_dotenv

load_dotenv()

# Provided credentials
API_ID = "28776072"
API_HASH = "b3a786dce1f4e7d56674b7cadfde3c9d"
BOT_TOKEN = os.getenv("BOT_TOKEN", "7515672383:AAEY-hBw4OGwUiIsDJ3qWfc1ZJMPHmV9C-4").strip()  # Add your bot token here
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()  # Optional variable for database URL
MUST_JOIN = os.getenv("MUST_JOIN", "")

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
