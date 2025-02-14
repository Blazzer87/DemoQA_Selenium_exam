import time
from selenium import webdriver
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.page_load_strategy = 'eager'

driver = webdriver.Chrome(options)
driver.get("https://demoqa.com/menu")

