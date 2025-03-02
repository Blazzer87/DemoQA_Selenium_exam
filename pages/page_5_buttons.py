from links.links import Links
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class Page5Buttons(BasePage):

    url = Links.page_buttons_url

    double_click_button_locator = ('xpath', '//button[@id="doubleClickBtn"]')
    right_click_button_locator = ('xpath', '//button[@id="rightClickBtn"]')
    click_button_locator = ('xpath', '//button[text()="Click Me"]')


    def action_double_click(self):
        self.action.double_click(self.wait.until(EC.element_to_be_clickable(self.double_click_button_locator)))
        self.action.perform()
        self.action.pause(1)

    def action_right_click(self):
        self.action.context_click(self.wait.until(EC.element_to_be_clickable(self.right_click_button_locator)))
        self.action.perform()
        self.action.pause(1)

    def action_click(self):
        self.action.click(self.wait.until(EC.element_to_be_clickable(self.click_button_locator)))
        self.action.perform()
        self.action.pause(1)


"""    Дописать авто-тесты на успешность нажатия
def check_double_click (self):
def check_right_click(self):
def check_click(self):
"""

"""     локаторы для авто-тестов
check_double_click_locator =
check_right_click_locator =
check_click_locator ="""