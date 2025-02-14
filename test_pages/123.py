import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def driver_yield():
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options)
    yield driver


def driver_return():
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options)
    return driver




next(driver_yield()).get("google.com")
time.sleep(2)
next(driver_yield()).close()
time.sleep(2)




