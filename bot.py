import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local use)
load_dotenv()

# Load required environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Optional: Topic IDs for filtering
EVENT_TOPIC_ID = os.getenv("EVENT_TOPIC_ID")
MARKETPLACE_TOPIC_ID = os.getenv("MARKETPLACE_TOPIC_ID")

# Check for missing credentials
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("Missing TELEGRAM_BOT_TOKEN in environment variables.")

if not GOOGLE_APPLICATION_CREDENTIALS:
    raise ValueError("Missing GOOGLE_APPLICATION_CREDENTIALS path.")

print("Environment variables loaded successfully.")