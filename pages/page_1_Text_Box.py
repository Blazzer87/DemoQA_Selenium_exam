from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class Page1TextBox(BasePage):

    text_box_locator = (By.XPATH, '//span[text()="Text Box"]')
    full_name_locator = (By.XPATH, '//input[@id="userName"]')
    email_locator = (By.XPATH, '//input[@id="userEmail"]')
    current_address_locator = (By.XPATH, '//textarea[@id="currentAddress"]')
    permanent_address_locator = (By.XPATH, '//textarea[@id="permanentAddress"]')
    submit_button_locator = (By.XPATH, '//button[@id="submit"]')
    test_field_locator = (By.XPATH, '//div[@class="output"]')

    def enter_full_name(self, full_name):
        self.wait.until(EC.element_to_be_clickable(self.full_name_locator)).send_keys('123456')