from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def open_page(self, url):
        self.driver.get(url)

