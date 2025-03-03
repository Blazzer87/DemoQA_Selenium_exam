import time

from base.base_test import BaseTest


class Test17AutoComplete(BaseTest):

    def test_17_auto_complete(self):
        self.page_auto_complete.open_page(self.page_auto_complete.url)
        time.sleep(3)           # очень нестабильная загрузка страницы

        self.page_auto_complete.send_keys_to_field(self.page_auto_complete.multiple_field, 'e')
        self.page_auto_complete.find_and_choise_color("Purple")
        self.page_auto_complete.send_keys_to_field(self.page_auto_complete.multiple_field, 'w')
        self.page_auto_complete.find_and_choise_color("White")

        self.page_auto_complete.send_keys_to_field(self.page_auto_complete.single_field, 'e')
        self.page_auto_complete.find_and_choise_color("Yellow")
        self.page_auto_complete.send_keys_to_field(self.page_auto_complete.single_field, 'r')
        self.page_auto_complete.find_and_choise_color("Red")

        time.sleep(1.5)
