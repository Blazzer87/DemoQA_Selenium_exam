
from tests.base_test import BaseTest
from conftest import driver

class TestButtons(BaseTest):

    def test_buttons(self):
        self.page_buttons.open_page(self.page_buttons.url)
        self.page_buttons.create_action()
        self.page_buttons.action_double_click()
        self.page_buttons.action_right_click()
        self.page_buttons.action_click()