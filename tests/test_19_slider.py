import time

from base.base_test import BaseTest


class Test19Slider(BaseTest):

    def test_19_slider(self):
        self.page_slider.open_page(self.page_slider.url)
        self.page_slider.get_width()
        time.sleep(1)
        self.page_slider.move_slider_to_target()
        time.sleep(3)