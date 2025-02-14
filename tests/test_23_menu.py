import time

from tests.base_test import BaseTest
from pages.page_1_text_box import Page1TextBox
from conftest import driver

class TestMenu(BaseTest):

    def test_menu(self):
        self.page_menu.open_page(self.page_menu.url)
        self.page_menu.move_to_elements_mi1()
        self.page_menu.move_to_elements_mi2()
        self.page_menu.move_to_elements_mi3()
        self.page_menu.move_to_elements_mi2()
        self.page_menu.move_to_elements_subsublist()
        self.page_menu.move_to_elements_subsubitem1()
        self.page_menu.move_to_elements_subsubitem2()





