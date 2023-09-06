import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    MONGO_URI = os.getenv("MONGO_URI")
