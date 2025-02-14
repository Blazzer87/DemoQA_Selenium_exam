import pytest
from conftest import driver
from pages.page_1_text_box import Page1TextBox
from pages.page_23_menu import Page23Menu
from pages.page_28_droppable import Page28Droppable


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page_textbox = Page1TextBox(driver)
        self.page_menu = Page23Menu(driver)
        self.page_droppable = Page28Droppable(driver)
