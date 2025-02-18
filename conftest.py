import pytest
from selenium import webdriver



@pytest.fixture(autouse=True, scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_argument('incognito')
    options.page_load_strategy = 'eager'        # приложение не стабильно, поэтому ставим раннюю загрузку
    driver = webdriver.Chrome(options)
    yield driver
    driver.quit()