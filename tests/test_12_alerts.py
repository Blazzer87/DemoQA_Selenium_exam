import time
from tests.base_test import BaseTest


class Test12Alerts(BaseTest):

    def test_12_alerts(self):
        self.page_alerts.open_page(self.page_alerts.url)

        self.page_alerts.click_alertButton()
        self.page_alerts.check_text_alert()
        time.sleep(1)
        self.page_alerts.accept_alert()
        time.sleep(1)

        self.page_alerts.click_timerAlertButton()
        self.page_alerts.check_text_timeralert()
        time.sleep(1)
        self.page_alerts.accept_alert()
        time.sleep(1)

        self.page_alerts.click_confirmAlertButton()
        self.page_alerts.check_text_confirmalert()
        time.sleep(1)
        self.page_alerts.dissmis_alert()
        time.sleep(1)
        self.page_alerts.click_confirmAlertButton()
        self.page_alerts.check_text_confirmalert()
        time.sleep(1)
        self.page_alerts.accept_alert()
        time.sleep(1)

        self.page_alerts.click_promtAlertButton()
        time.sleep(1)
        self.page_alerts.send_keys_to_promt_alert("HELLO DEMOQA")
        time.sleep(1)
        self.page_alerts.check_text_promtalert()
        time.sleep(2)






