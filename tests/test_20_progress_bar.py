import time
from tests.base_test import BaseTest


class Test20ProgressBar(BaseTest):

    def test_20_progress_bar(self):
        self.page_progress_bar.open_page(self.page_progress_bar.url)
        self.page_progress_bar.specify_value()
        self.page_progress_bar.click_start()
        self.page_progress_bar.check_progress()
        time.sleep(2)