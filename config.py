# Copyright (c) 2022 - 2024 EDM115
import os
from urllib.parse import quote_plus


class Config:
    APP_ID = int(os.environ.get("APP_ID", "21851558"))
    API_HASH = str(os.environ.get("API_HASH", "045a99f29cbc003618d9786d0b4683d0"))
    BOT_TOKEN = str(os.environ.get("BOT_TOKEN", "8142840152:AAHg3DtFZbDAt0TQtR4Xt1gvoxR-nK6u8vQ"))
    AUTHORIZED_GROUPS = [-4583650175]
    LOGS_CHANNEL = (
        int(os.environ.get("LOGS_CHANNEL", "-1002127549042"))
        # if os.environ.get("LOGS_CHANNEL").strip("-").isdigit()
        # else os.environ.get("LOGS_CHANNEL")
    )
    db_password = quote_plus("Sato#321")
    MONGODB_URL = os.environ.get("MONGODB_URL", f"mongodb+srv://Kazuma:{db_password}@deployment.zwliu.mongodb.net/?retryWrites=true&w=majority&appName=deployment")
    MONGODB_DBNAME = os.environ.get("MONGODB_DBNAME", "deployment")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "1132901778"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2097152000
    MAX_MESSAGE_LENGTH = 4096
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 1024 * 10  # 10 MB
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
    MAX_CONCURRENT_TASKS = 75
    MAX_TASK_DURATION_EXTRACT = 120 * 60  # 2 hours (in seconds)
    MAX_TASK_DURATION_MERGE = 240 * 60  # 4 hours (in seconds)
