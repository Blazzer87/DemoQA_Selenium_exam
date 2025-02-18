import time

from tests.base_test import BaseTest
from conftest import driver

class Test5Buttons(BaseTest):

    def test_5_buttons(self):
        self.page_buttons.open_page(self.page_buttons.url)
        self.page_buttons.create_action()
        self.page_buttons.action_double_click()
        self.page_buttons.action_right_click()
        self.page_buttons.action_click()
        time.sleep(2)