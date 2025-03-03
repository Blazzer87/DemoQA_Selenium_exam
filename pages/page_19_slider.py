from links.links import Links
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Page19Slider(BasePage):

    url = Links.page_slider

    range_locator = ('xpath', '//input[@type="range"]')
    input_locator = ('xpath', '//input[@id="sliderValue"]')

    width = None
    target_value = 30

    def get_width(self):
        self.width = self.wait.until(EC.element_to_be_clickable(self.range_locator)).value_of_css_property('width')
        self.width = float(self.width.replace('px',''))


    def move_slider_to_target(self):
        if self.target_value > 50: x = 1
        elif self.target_value < 50: x = -1

        self.wait.until(EC.element_to_be_clickable(self.range_locator)).click()


        self.create_action()
        self.action.click(self.wait.until(EC.element_to_be_clickable(self.range_locator)))

        while self.check_fact_value() is not True:
            self.action.move_by_offset(self.width/200 * x, 0)
            self.action.click()
            self.action.perform()


    def check_fact_value(self):
        return int(self.wait.until(EC.element_to_be_clickable(self.input_locator)).get_attribute('defaultValue')) == self.target_value







