from abc import ABC, abstractmethod

from botik.input.user_input import UserInput
from botik.page.page_factory import PageFactory
from botik.user.user_base import UserBase


class App(ABC):
    """
    The root object of bot.
    """

    def __init__(self, bot):
        self.bot = bot
        self._page_fac: PageFactory = None
        self.user_input = UserInput()
        self.pages_data = None

    @abstractmethod
    def start(self):
        """
        Call this method to start listening for connections.
        """
        pass

    @abstractmethod
    def initialize(self):
        pass

    def set_pages(self, pages_data):
        """
        Set the PageData list to be handled by bot.
        """
        self.pages_data = pages_data
