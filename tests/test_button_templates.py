from unittest import TestCase

from botik.input.keyboard.button.button_data import ButtonData
from botik.navigation.navigation import Navigation
from botik.templates.button_templates import ButtonTemplates


class TestButtonTemplates(TestCase):

    def test_save(self):
        templates = self.new_templates()
        self.set_button_data(templates, 'Test1')
        self.set_button_data(templates, 'Test2')

        self.assertEqual(templates.Test1.text, 'Test1')
        self.assertEqual(templates.Test2.text, 'Test2')

    def test_add_default_navigation(self):
        templates = self.new_templates()
        templates.add_default_navigation('Back', 'Home')
        self.set_button_data(templates, 'Test1')

        self.assertEqual(templates.Back.text, 'Back')
        self.assertEqual(templates.Home.text, 'Home')
        self.assertEqual(templates.Test1.text, 'Test1')

    def new_templates(self):
        nav = Navigation()
        return ButtonTemplates(nav)

    def set_button_data(self, templates, text):
        data = ButtonData(text, None)
        templates.set(text, data)
