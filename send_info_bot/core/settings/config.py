import os
from typing import Optional

from dotenv import load_dotenv


class Settings:
    def __init__(self):
        load_dotenv()
        self.b_token: Optional[str] = os.getenv('b_token')
        self.channel_id: Optional[int] = os.getenv('channel_id')

    '''def get(self, key: str, default: Optional[str] = None) -> Optional[str]:
        return getattr(self, key.lower(), default)'''
