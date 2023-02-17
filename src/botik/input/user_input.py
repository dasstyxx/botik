import logging

from navigation import navigator


class UserInput:
    def __init__(self, users):
        self.users = users

    async def forward_inline_button(self, user, text):
        page = navigator.get_user_page(user)
        await page.handle_raw_input(user, text, True)
        logging.debug("Forward button")

    async def handle_input(self, user, text):
        # TODO: Do not render page on every user message!
        page = navigator.get_user_page(user)

        await page.handle_raw_input(user, text)
