from links.links import Links
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class Page20ProgressBar(BasePage):

    url = Links.page_progress_bar

    start_button_locator = ('xpath', '//button[@id="startStopButton"]')
    progress_locator = ('xpath', '//div[@role="progressbar"]')

    target_value = None
    progress = None


    def specify_value(self):
        self.target_value = input("Введите произвольное целое число от 1 до 99 включительно:")
        try:
            self.target_value = int(self.target_value)
        except:
            raise ValueError("Вы ввели текст. Значение должно быть целым числом.")
        if self.target_value < 1 or self.target_value > 99:
            raise ValueError("Значение должно в диапазоне от 1 до 99 включительно.")
        return self.target_value


    def click_start(self):
        self.wait.until(EC.element_to_be_clickable(self.start_button_locator)).click()


    def get_progress(self):
        # убрано ожидание, т.к. оно значительно замедляет выполнение теста, и тест падает на значениях ниже 6
        self.progress = int((self.driver.find_element(*self.progress_locator)).get_attribute('ariaValueNow'))
        return self.progress


    def check_progress(self):
        while True:
            if self.get_progress() < self.target_value:
                continue
            if self.get_progress() == self.target_value:
                self.click_stop()
                break
            if self.get_progress() > self.target_value:
               raise ValueError("тормози, перебрали)))")


    def click_stop(self):
        self.wait.until(EC.element_to_be_clickable(self.start_button_locator)).click()



