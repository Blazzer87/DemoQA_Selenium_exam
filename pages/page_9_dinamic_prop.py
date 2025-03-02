from links.links import Links
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class Page9DinamicProp (BasePage):

    url= Links.page_dinamic_properties

    text_color = None

    text_with_random_id_locator = ('xpath', '//div[@class="row"]/div/div/p')
    enable_after_5_button_locator = ('xpath', '//button[@id="enableAfter"]')
    color_change_button_locator = ('xpath', '//button[@id="colorChange"]')
    visible_after_5_button_locator = ('xpath', '//button[@id="visibleAfter"]')

    def find_color(self):
        self.text_color = self.wait.until(EC.visibility_of_element_located(self.color_change_button_locator)).value_of_css_property("color")
        print("\nСейчас цвет текста в кнопке = ", self.text_color)
        return self.text_color

    def wait_change_color(self):
        while self.text_color != "rgba(220, 53, 69, 1)":
            self.text_color = self.wait.until(EC.visibility_of_element_located(self.color_change_button_locator)).value_of_css_property("color")
        print("\nЦвет изменился, теперь цвет текста в кнопке = ", self.text_color)

