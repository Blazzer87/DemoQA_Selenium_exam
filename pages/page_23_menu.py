from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from conftest import driver
from links.links import Links
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Page23Menu(BasePage):

    url = Links.page_menu_url

    main_item_1_locator = ('xpath', '//a[text()="Main Item 1"]')
    main_item_2_locator = ('xpath', '//a[text()="Main Item 2"]')
    main_item_3_locator = ('xpath', '//a[text()="Main Item 3"]')
    subsublist_locator = ('xpath', '//a[text()="SUB SUB LIST »"]')
    subsubitem1_locator = ('xpath', '//a[text()="Sub Sub Item 1"]')
    subsubitem2_locator = ('xpath', '//a[text()="Sub Sub Item 2"]')

    def create_action(self):
        self.action = ActionChains(self.driver)

    def move_to_elements_mi1(self):
        self.action.move_to_element(self.wait.until(EC.visibility_of_element_located(self.main_item_1_locator)))
        self.action.pause(1)
        self.action.perform()

    def move_to_elements_mi2(self):
        self.action.move_to_element(self.wait.until(EC.visibility_of_element_located(self.main_item_2_locator)))
        self.action.pause(1)
        self.action.perform()

    def move_to_elements_mi3(self):
        self.action.move_to_element(self.wait.until(EC.visibility_of_element_located(self.main_item_3_locator)))
        self.action.pause(1)
        self.action.perform()


    def move_to_elements_subsublist(self):
        self.action.move_to_element(self.wait.until(EC.visibility_of_element_located(self.subsublist_locator)))
        self.action.pause(1)
        self.action.perform()


    def move_to_elements_subsubitem1(self):
        self.action.move_to_element(self.wait.until(EC.visibility_of_element_located(self.subsubitem1_locator)))
        self.action.pause(1)
        self.action.perform()


    def move_to_elements_subsubitem2(self):
        self.action.move_to_element(self.wait.until(EC.visibility_of_element_located(self.subsubitem2_locator)))
        self.action.pause(1)
        self.action.perform()

