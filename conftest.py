import pytest
from selenium import webdriver



@pytest.fixture(autouse=True, scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options)
    yield driver
    driver.quit()