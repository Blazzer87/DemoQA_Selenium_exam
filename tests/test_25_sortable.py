import time
from tests.base_test import BaseTest


class Test25Sortable (BaseTest):

    def test_25_sortable(self):
        self.page_sortable.open_page(self.page_sortable.url)
        self.page_sortable.create_action()
        self.page_sortable.drag_and_drop_list_nine_to_one()
        self.page_sortable.go_to_grid()
        self.page_sortable.drag_and_drop_grid_nine_to_one()
        time.sleep(1)