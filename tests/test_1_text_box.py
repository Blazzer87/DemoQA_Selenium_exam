import time

from base.base_test import BaseTest


class Test1TextBox(BaseTest):

    def test_1_text_box(self):
        self.page_textbox.open_page(self.page_textbox.url)
        self.page_textbox.enter_fullname('SERGEY')
        self.page_textbox.enter_email('laba@qpd.ru')
        self.page_textbox.enter_current_adress('ВоронеВжжжж')
        self.page_textbox.enter_permanent_adress("Москва")
        self.page_textbox.click_submit_button()
        self.page_textbox.check_result()
        time.sleep(2)