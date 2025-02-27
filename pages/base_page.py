from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from tests.conftest import driver


class BasePage:

    action = None
    main_tab = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url):
        self.driver.get(url)
        self.main_tab = self.driver.current_window_handle

    def create_action(self):
        self.action = ActionChains(self.driver)
