import time
from tests.base_test import BaseTest


class Test8UpDownloads(BaseTest):

    def test_8_updownloads(self):
        self.page_updownloads.open_page(self.page_updownloads.url)
        self.page_updownloads.click_upload()
        self.page_updownloads.check_success_upload()
        time.sleep(1)
        self.page_updownloads.click_download()
        self.page_updownloads.open_download_file()
        time.sleep(5)
