from tests.base_test import BaseTest


class Test23Menu(BaseTest):

    def test_23_menu(self):
        self.page_menu.open_page(self.page_menu.url)
        self.page_menu.create_action()
        self.page_menu.move_to_elements_mi1()
        self.page_menu.move_to_elements_mi2()
        self.page_menu.move_to_elements_mi3()
        self.page_menu.move_to_elements_mi2()
        self.page_menu.move_to_elements_subsublist()
        self.page_menu.move_to_elements_subsubitem1()
        self.page_menu.move_to_elements_subsubitem2()
