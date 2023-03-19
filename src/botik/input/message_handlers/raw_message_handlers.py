import logging
from abc import ABC, abstractmethod

from botik.navigation import navigator
from botik.user import users


class RawMessageHandlers(ABC):
    def __init__(self, bot, start_callback, user_input):
        self.bot = bot
        self.user_input = user_input
        self.start_callback = start_callback

        self._initialize_handlers(bot)

    @abstractmethod
    def _initialize_handlers(self, bot):
        pass

    @abstractmethod
    async def _get_user_from_message(self, message):
        pass

    async def _get_user_from_id(self, user_id):
        if users.exists(user_id):
            user = users.get(user_id)
            logging.debug(f"Existing user! id: {user.id}")
        else:
            user = users.add(user_id)
            await navigator.change_page(user, '/')
            # await navigator.execute_page_change()
            logging.debug(f"New user! id: {user.id}")
        return user

    async def start_reply(self, message):
        user = self._get_user_from_message(message)

        if self.start_callback:
            await self.start_callback(user)

    async def message_reply(self, message):
        user = await self._get_user_from_message(message)

        # TODO: replace by proper raw-messages service
        await user.storage.set("message", message)

        await self.user_input.handle_input(user, message.text)
