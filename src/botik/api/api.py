from abc import ABC

from botik.api.send_message import SendMessage


class Api(ABC):
    def __init__(self, bot):
        self.bot = bot
        self.msg: SendMessage = None
        self.api_type = None
