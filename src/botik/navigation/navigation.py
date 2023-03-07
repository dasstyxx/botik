import asyncio
import logging

from botik.navigation.routing import concat_paths


class Navigation:
    def __init__(self):
        self.page_factory = None
        self.path_to_page_data = {}
        self.change_page_delayed = {}

        loop = asyncio.get_event_loop()
        loop.create_task(self._monitor_page_change())

    def initialize(self, page_factory, data):
        self.page_factory = page_factory
        self.path_to_page_data = {e.path: e for e in data}

    def get_page_data(self, path):
        return self.path_to_page_data.get(path)

    async def change_page(self, user, path):
        """
        Change page for user.
        :param user: User
        :param path: Absolute (starts with a '~') or relative path to page
        """
        if user not in self.change_page_delayed:
            self.change_page_delayed[user] = []
        self.change_page_delayed[user].append(path)

    async def get_back(self, user):
        """
        Gets the path from the active page's 'get_back_path' method and navigates to the page at that path.
        :param user: User
        :param path: Absolute (starts with a '~') or relative path to page
        """
        page = user.current_page
        back_path = page.get_back_path()
        await self.change_page(user, back_path)

    async def _render_page(self, user, path):
        data = self.get_page_data(path)
        if not data:
            return None

        page = self.page_factory.create(data)
        await page.make_page_content(user)
        return page

    async def _monitor_page_change(self):
        while True:
            if self.change_page_delayed:
                await self.execute_page_change()
            await asyncio.sleep(0.1)

    async def execute_page_change(self):
        """
        Inner method, don't use it
        """
        for user, paths in self.change_page_delayed.items():
            for path in paths:
                current_page = user.current_page
                current_path = current_page.path if current_page else '/'
                concat_path = concat_paths(current_path, path)

                page = await self._render_page(user, concat_path)
                if page:
                    user.set_page(page)
                    if current_page:
                        current_page.destruct()
                    logging.debug(f"User {user.id} has changed page\n\tfrom {current_path}\n\tto {concat_path}")

        self.change_page_delayed.clear()
