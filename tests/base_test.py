import pytest
from selenium.webdriver import ActionChains

from pages.page_1_text_box import Page1TextBox
from conftest import driver
from pages.page_23_menu import Page23Menu


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page_textbox = Page1TextBox(driver)
        self.page_menu = Page23Menu(driver)
        self.action = ActionChains(driver)
