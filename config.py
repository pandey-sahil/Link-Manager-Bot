import os
from dotenv import load_dotenv
load_dotenv()

API_ID = int(os.getenv("API_ID", "Your Api Id"))
API_HASH = os.environ.get("API_HASH", "Your Api Hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "Bot Token")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "").split(",")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Db Name")
DATABASE_URL = os.getenv("DATABASE_URL", "Mongo URL")
OWNER_ID = int(os.environ.get("OWNER_ID", "Owner Id"))

if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)

ADMINS.append(123456789)

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "Logs Channels Id"))
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Updates Channel Username Without @")
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True")
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '')
LINK_BYPASS = "False"
