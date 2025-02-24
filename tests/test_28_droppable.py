import time
from tests.base_test import BaseTest


class Test28Droppable(BaseTest):

    def test_28_droppable(self):
        time.sleep(2)
        self.page_droppable.open_page(self.page_droppable.url)
        self.page_droppable.create_action()
        self.page_droppable.drag_and_drop_simple_drag_me_to_simple_drop_here()
        self.page_droppable.check_success()
