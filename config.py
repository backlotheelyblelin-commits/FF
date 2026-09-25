import os
from dotenv import load_dotenv

load_dotenv()

# ═══ ENV ═══
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]
TTS_API_KEY = os.getenv("TTS_API_KEY", "")

# ═══ GIỚI HẠN ═══
TOKEN_LIMITS = {"user": 3, "admin": 999999, "owner": 999999}
SESSION_LIMITS = {"user": 999999, "admin": 999999, "owner": 999999}

MIN_DELAY = 0.1
MAX_DELAY = 3600.0
DEFAULT_SPAM_DELAY = 1.0
DEFAULT_CALL_DELAY = 3.0


def is_owner(uid: int) -> bool:
    return uid == OWNER_ID


def is_admin(uid: int) -> bool:
    if uid == OWNER_ID:
        return True
    if uid in ADMIN_IDS:
        return True
    try:
        from database.db import db
        return db.is_admin(uid)
    except Exception:
        return False


def get_token_limit(uid: int) -> int:
    if is_owner(uid):
        return TOKEN_LIMITS["owner"]
    if is_admin(uid):
        return TOKEN_LIMITS["admin"]
    return TOKEN_LIMITS["user"]


def get_session_limit(uid: int) -> int:
    return 999999