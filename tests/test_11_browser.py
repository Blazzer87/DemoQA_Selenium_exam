import time
from conftest import driver
from tests.base_test import BaseTest


class Test11Browser(BaseTest):

    def test_11_browser(self):
        self.page_browser.open_page(self.page_browser.url)

        self.page_browser.open_new_tab()
        self.page_browser.open_new_tab()
        self.page_browser.open_new_tab()
        self.page_browser.switch_to_new_tab()
        self.page_browser.check_tab_and_window()
        time.sleep(1)
        self.page_browser.close_current_tab()
        self.page_browser.switch_to_main_tab()

        self.page_browser.open_new_window()
        self.page_browser.switch_to_new_tab()
        self.page_browser.check_tab_and_window()
        time.sleep(1)
        self.page_browser.close_current_tab()
        self.page_browser.switch_to_main_tab()

        self.page_browser.open_new_window_message()
        self.page_browser.switch_to_new_tab()
        # self.page_browser.check_window_message()
        time.sleep(1)
        self.page_browser.close_current_tab()
        self.page_browser.switch_to_main_tab()



