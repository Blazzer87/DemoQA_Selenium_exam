

from tests.base_test import BaseTest
from conftest import driver

class TestUpDownloads(BaseTest):

    def test_updownloads(self):
        self.page_updownloads.open_page(self.page_updownloads.url)
        self.page_updownloads.click_download()
        self.page_updownloads.open_file()
        self.page_updownloads.click_upload()
        self.page_updownloads.check_success_upload()
