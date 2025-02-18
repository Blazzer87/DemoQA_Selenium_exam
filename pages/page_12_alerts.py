from links.links import Links
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class Page12Alerts(BasePage):

    url = Links.page_alerts_url

    alertButton_locator = ('xpath', '//button[@id="alertButton"]')
    timerAlertButton_locator = ('xpath', '//button[@id="timerAlertButton"]')
    confirmAlertButton = ('xpath', '//button[@id="confirmButton"]')
    promtAlertButton_locator = ('xpath', '//button[@id="promtButton"]')


    def click_alertButton(self):
        self.wait.until(EC.element_to_be_clickable(self.alertButton_locator)).click()

    def accept_alert(self):
        self.wait.until(EC.alert_is_present()).accept()

    def check_text_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        print('\n', "alert #1", alert.text)
        assert alert.text == "You clicked a button", "с алертом что-то не так"




    def click_timerAlertButton(self):
        self.wait.until(EC.element_to_be_clickable(self.timerAlertButton_locator)).click()

    def check_text_timeralert(self):
        alert = self.wait.until(EC.alert_is_present())
        print("alert #2", alert.text)
        assert alert.text == "This alert appeared after 5 seconds", "с алертом что-то не так"



    def click_confirmAlertButton(self):
        self.wait.until(EC.element_to_be_clickable(self.confirmAlertButton)).click()

    def check_text_confirmalert(self):
        alert = self.wait.until(EC.alert_is_present())
        print("alert #3", alert.text)
        assert alert.text == "Do you confirm action?", "с алертом что-то не так"

    def dissmis_alert(self):
        self.wait.until(EC.alert_is_present()).dismiss()



    def click_promtAlertButton(self):
        self.wait.until(EC.element_to_be_clickable(self.promtAlertButton_locator)).click()

    def send_keys_to_promt_alert(self, message_to_alert):
        self.wait.until(EC.alert_is_present()).send_keys(message_to_alert)
        self.message_to_alert = message_to_alert
        self.accept_alert()


    def check_text_promtalert(self):
        text = self.wait.until(EC.visibility_of_element_located(('xpath', '//span[@id="promptResult"]'))).get_attribute('textContent')
        print(text)
        assert text == "You entered " + self.message_to_alert, 'что-то не так'







