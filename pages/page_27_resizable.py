import time
from random import randint

from selenium.webdriver import Keys

from links.links import Links
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Page27Resizable(BasePage):

    url = Links.page_resizable

    dot_1_locator = ('xpath', '//div[@class="constraint-area"]//span')
    dot_2_locator = ('xpath', '//div[@id="resizable"]/span')

    def decrease_box_1(self):
        self.create_action()
        self.action.click_and_hold(self.wait.until(EC.element_to_be_clickable(self.dot_1_locator)))
        # на 50 влево и 50 вверх
        self.action.move_by_offset(-50,-50)
        self.action.release()
        self.action.pause(1)
        self.action.perform()

    def increase_box_1(self):
        self.create_action()
        self.action.click_and_hold(self.wait.until(EC.element_to_be_clickable(self.dot_1_locator)))
        # на 350 вправо и 150 вниз
        self.action.move_by_offset(350,150)
        self.action.release()
        self.action.pause(1)
        self.action.perform()

    def crazy_box_2(self):
        current_time = time.time() + 10
        while current_time > time.time():
            self.create_action()
            self.action.scroll_by_amount(0,300)
            self.action.click_and_hold(self.wait.until(EC.element_to_be_clickable(self.dot_2_locator)))
            self.action.move_by_offset(randint(-100, 100), randint(-100, 100))
            self.action.release()
            self.action.pause(1)
            self.action.perform()



