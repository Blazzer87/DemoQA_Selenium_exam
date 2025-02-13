import pytest
from selenium import webdriver




class Setup:

    @pytest.fixture(autouse=True)
    def start_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        driver = webdriver.Chrome(options)
        yield driver
        driver.close()