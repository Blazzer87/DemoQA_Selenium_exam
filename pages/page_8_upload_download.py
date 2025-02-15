import os.path
import time

from links.links import Links
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class Page8UpDownload(BasePage):

    url = Links.page_updownloads_url



    download_button_locator = ('xpath','//a[@id="downloadButton"]')
    upload_button_locator = ('xpath', '//input[@id="uploadFile"]')
    check_upload_locator = ('xpath', '//p[@id="uploadedFilePath"]')

    def click_download(self):
        self.wait.until(EC.element_to_be_clickable(self.download_button_locator)).click()

    def open_download_file(self):
        time.sleep(2)
        download_directory = os.path.join(os.path.expanduser("~"), "Downloads")     # Определение пути к папке загрузок
        files = [os.path.join(download_directory, f) for f in os.listdir(download_directory)]   # Получаем файл с максимальным временем создания
        latest_file = max(files, key=os.path.getctime)
        os.startfile (latest_file)      # Открываем последний загруженный файл
        time.sleep(5)

    def click_upload(self):
        relative_path_image = 'C:\QA\PycharmProjects\DemoQA_Selenium_exam\pages\page_8_test_file.jpg'
        self.wait.until(EC.element_to_be_clickable(self.upload_button_locator)).send_keys(relative_path_image)
        time.sleep(1)

    def check_success_upload(self):
        self.wait.until(EC.element_to_be_clickable(self.check_upload_locator)).is_displayed()

