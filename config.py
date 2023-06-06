import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "29063836"))
    API_HASH = os.environ.get("API_HASH", "2a8a0cea43b248ee282eef91893e428b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6009229371:AAEAfCE66j330OXyGnD5H0dJJ_-rFRn7rsg") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "5403801894")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://movie:bot2@cluster0.n7ssqbz.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "Forward_Session")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001976486639"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
