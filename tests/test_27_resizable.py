import pytest

from tests.base_test import BaseTest


class Test27Resizable(BaseTest):

    def test_27_resizable(self):
        self.page_resizable.open_page(self.page_resizable.url)
        self.page_resizable.decrease_box_1()
        self.page_resizable.increase_box_1()
        self.page_resizable.crazy_box_2()