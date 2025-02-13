import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def driver():
    options = webdriver.ChromeOptions()  # создаём опции хрома
    options.add_argument('start-maximized')  # передаём фулскрин в опции хрома
    options.add_argument('incognito')  # передаём инкогнито в опции хрома
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options)
    return driver

def open(driver):
    wait = WebDriverWait(driver, 2)
    driver.get("https://demoqa.com/text-box")


class Page1TextBox:

    full_name = "ABCDE"

    text_box_locator = (By.XPATH, '//span[text()="Text Box"]')
    full_name_locator = (By.XPATH, '//input[@id="userName"]')
    email_locator = (By.XPATH, '//input[@id="userEmail"]')
    current_address_locator = (By.XPATH, '//textarea[@id="currentAddress"]')
    permanent_address_locator = (By.XPATH, '//textarea[@id="permanentAddress"]')
    submit_button_locator = (By.XPATH, '//button[@id="submit"]')
    test_field_locator = (By.XPATH, '//div[@class="output"]')

    def enter_full_name(self, full_name):
        self.wait.until(EC.element_to_be_clickable(self.full_name_locator)).send_keys(full_name)



open(driver())
page = Page1TextBox()
page.enter_full_name(page.full_name)

time.sleep(3)