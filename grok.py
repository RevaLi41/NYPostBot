from langchain_xai import ChatXAI
from dotenv import load_dotenv
import os
from const import CONST

class Grok:
    def __init__(self):
        load_dotenv()
        self.chat = ChatXAI(
            xai_api_key = os.getenv('GROK_API_KEY'),
            model = 'grok-beta'
        )

    def send_to_grok(self, msg):
        print(self.chat.invoke(msg))