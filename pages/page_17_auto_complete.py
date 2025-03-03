from base.base_page import BasePage
from links.links import Links
from selenium.webdriver.support import expected_conditions as EC


class Page17AutoComplete(BasePage):

    url = Links.page_auto_complete

    text = None

    multiple_field = ('xpath', '//div[@id="autoCompleteMultiple"]//div[contains(@class, "auto-complete__value-container")]')
    single_field = ('xpath', '//div[@id="autoCompleteSingleContainer"]')


    def send_keys_to_field(self, locator, text):
        self.create_action()
        self.action.click(self.wait.until(EC.visibility_of_element_located(locator)))
        self.action.send_keys(text)
        self.action.perform()
        self.text = text

    def find_and_choise_color(self, color):
        color_list = ('xpath', f'//div[text()="{color}"]')
        self.wait.until(EC.visibility_of_element_located(color_list)).click()








