
from tests.base_test import BaseTest
from conftest import driver

class TestDroppable(BaseTest):

    def test_droppable(self):
        self.page_droppable.open_page(self.page_droppable.url)
        self.page_droppable.create_action()
        self.page_droppable.drag_and_drop_simple_drag_me_to_simple_drop_here()
        self.page_droppable.check_success()





