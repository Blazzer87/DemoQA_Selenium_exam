import time
from tests.base_test import BaseTest



class Test9DinamicProp(BaseTest):

    def test_dinamic_prop(self):
        self.page_dinamic_prop.open_page(self.page_dinamic_prop.url)
        self.page_dinamic_prop.find_color()
        self.page_dinamic_prop.wait_change_color()
        time.sleep(1)
