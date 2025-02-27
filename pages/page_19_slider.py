from dataclasses import replace

from links.links import Links
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Page19Slider(BasePage):

    url = Links.page_slider

    range_locator = ('xpath', '//input[@type="range"]')
    input_locator = ('xpath', '//input[@id="sliderValue"]')

    width = None

    target_value = 99

    def get_width(self):
        self.width = self.wait.until(EC.element_to_be_clickable(self.range_locator)).value_of_css_property('width')
        self.width = float(self.width.replace('px',''))


    def move_slider_to_target(self):
        print(self.width)
        print(type(self.width))
        x = (self.target_value - 50) * (self.width / 100)
        print(x)
        self.create_action()
        self.action.move_to_element(self.driver.find_element(*self.range_locator))
        self.action.click()
        self.action.move_by_offset(x,0)
        self.action.click()
        self.action.pause(1)
        self.action.perform()

    def check(self):
        print(self.wait.until(EC.element_to_be_clickable(self.input_locator)).get_attribute('defaultValue'))
        assert int(self.wait.until(EC.element_to_be_clickable(self.input_locator)).get_attribute('defaultValue')) == self.target_value







