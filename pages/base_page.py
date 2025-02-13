from conftest import Setup


class BasePage(Setup):

    def __init__(self):
        self.wait = WeDriverWait(self.driver)
        self.start_driver()


    def open(self):
        self.driver.
        self.driver.get("https://demoqa.com/text-box")

