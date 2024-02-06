from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/a7a74c92af4aff94d158f.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/a7a74c92af4aff94d158f.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/t7_au")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/wx_pm")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6945048358").split()))


FAILED = "https://telegra.ph/file/a7a74c92af4aff94d158f.jpg"
