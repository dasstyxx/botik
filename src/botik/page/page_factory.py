from abc import ABC, abstractmethod

from botik.page.page_data import PageData


class PageFactory(ABC):

    @abstractmethod
    def _make_dependencies(self, page_data: PageData):
        pass

    def create(self, data: PageData):
        self._make_dependencies(data)
        return data.page_type(data.path, self.markup_factory, data)
