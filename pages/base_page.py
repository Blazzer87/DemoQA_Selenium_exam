from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver


class BasePage:

    action = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def open_page(self, url):
        self.driver.get(url)

    def create_action(self):
        self.action = ActionChains(self.driver)
