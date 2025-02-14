from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from conftest import driver
from links.links import Links
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Page23Menu(BasePage):

    url = Links.page_menu_url

    action_chain = None

    main_item_1_locator = ('xpath', '//a[text()="Main Item 1"]')
    main_item_2_locator = ('xpath', '//a[text()="Main Item 2"]')
    main_item_3_locator = ('xpath', '//a[text()="Main Item 3"]')
    subsublist_locator = ('xpath', '//a[text()="SUB SUB LIST »"]')
    subsubitem1 = ('xpath', '//a[text()="Sub Sub Item 1"]')
    subsubitem2 = ('xpath', '//a[text()="Sub Sub Item 2"]')


    def move_to_elements_mi1(self):

        self.action.move_to_element(self.wait.until(EC.visibility_of_element_located(self.main_item_1_locator)))
        self.action.perform()
        self.action.pause(1)

    def move_to_elements_mi2(self):
        self.action.move_to_element(*self.main_item_2_locator)
        self.action.perform()
        self.action.pause(1)

    def move_to_elements_mi3(self):
        self.action.move_to_element(*self.main_item_3_locator)
        self.action.perform()
        self.action.pause(1)

    def move_to_elements_subsublist(self):
        self.action.move_to_element(*self.subsublist_locator)
        self.action.perform()
        self.action.pause(1)

    def move_to_elements_subsubitem1(self):
        self.action.move_to_element(*self.subsubitem1)
        self.action.perform()
        self.action.pause(1)

    def move_to_elements_subsubitem2(self):
        self.action.move_to_element(*self.subsubitem2)
        self.action.perform()
        self.action.pause(1)







