from links.links import Links
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class Page11Browser(BasePage):

    url = Links.page_browser_url

    new_tab_locator = ('xpath', '//button[@id="tabButton"]')
    new_window_locator = ('xpath', '//button[@id="windowButton"]')
    new_window_message_locator = ('xpath', '//button[@id="messageWindowButton"]')

    def open_new_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.new_tab_locator)).click()

    def open_new_window(self):
        self.wait.until(EC.element_to_be_clickable(self.new_window_locator)).click()

    def open_new_window_message(self):
        self.wait.until(EC.element_to_be_clickable(self.new_window_message_locator)).click()

    def switch_to_new_tab(self):
        for i in self.driver.window_handles:
            if i != self.main_tab:
                new_tab = i
                self.driver.switch_to.window(new_tab)

    def switch_to_main_tab(self):
        self.driver.switch_to.window(self.main_tab)

    def close_current_tab (self):
        self.driver.current_window_handle
        self.driver.close()

    def check_tab_and_window(self):
        assert self.wait.until(EC.visibility_of_element_located(('xpath', '//h1'))).get_attribute('textContent') == "This is a sample page", "заголовок отличается, где-то ошибка"


""" пока неудачно
    def check_window_message(self):
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        print(self.main_tab)
        print(self.driver.find_element('xpath', '//body').is_displayed())

        # assert self.wait.until(EC.visibility_of_element_located(('xpath', '//body[contains(text(),"Knowledge increases")]'))).is_displayed() == True, "ошибка"
        # assert self.wait.until(EC.visibility_of_element_located(('xpath', '//body[contains(text(),"Knowledge increases")]'))).get_attribute('textContent') == "Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization."), "ошибка"
"""