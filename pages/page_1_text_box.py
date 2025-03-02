from selenium.webdriver.common.by import By
from links.links import Links
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Page1TextBox(BasePage):

    url = Links.page_text_box_url

    fullname = None
    email = None
    current_adress = None
    permanent_adress = None

    full_name_locator = (By.XPATH, '//input[@id="userName"]')
    email_locator = (By.XPATH, '//input[@id="userEmail"]')
    current_address_locator = (By.XPATH, '//textarea[@id="currentAddress"]')
    permanent_address_locator = (By.XPATH, '//textarea[@id="permanentAddress"]')
    submit_button_locator = (By.XPATH, '//button[@id="submit"]')
    test_field_locator = (By.XPATH, '//div[@id="output"]')

    def enter_fullname(self, fullname):
        self.wait.until(EC.element_to_be_clickable(self.full_name_locator)).send_keys(fullname)
        self.fullname = fullname

    def enter_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.email_locator)).send_keys(email)
        self.email = email

    def enter_current_adress(self, current_adress):
        self.wait.until(EC.element_to_be_clickable(self.current_address_locator)).send_keys(current_adress)
        self.current_adress = current_adress

    def enter_permanent_adress(self, permanent_adress):
        self.wait.until(EC.element_to_be_clickable(self.permanent_address_locator)).send_keys(permanent_adress)
        self.permanent_adress = permanent_adress

    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.submit_button_locator)).click()

    def check_result(self):
         self.text = self.wait.until(EC.element_to_be_clickable(self.test_field_locator)).get_property("textContent")
         assert self.text == f"Name:{self.fullname}Email:{self.email}Current Address :{self.current_adress} Permananet Address :{self.permanent_adress}", "Текст не совпадает"

