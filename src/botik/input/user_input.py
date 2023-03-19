import logging


class UserInput:

    async def forward_inline_button(self, user, text):
        page = user.current_page
        await page.handle_raw_input(user, text, True)
        logging.debug("Forward button")

    async def handle_input(self, user, text):
        page = user.current_page

        await page.handle_raw_input(user, text)
