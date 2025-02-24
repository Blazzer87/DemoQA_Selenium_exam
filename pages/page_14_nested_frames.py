from links.links import Links
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Page14NestedFrames(BasePage):

    url = Links.page_nested_frames

    parent_frame_locator = ('xpath', '//body')
    child_frame_locator = ('xpath', '//body')

    def switch_to_parent_frame_by_id(self):
        self.driver.switch_to.frame("frame1")

    def switch_to_frame_by_index(self):
        self.driver.switch_to.frame(0)

    def find_text(self, locator):
        self.text = self.wait.until(EC.visibility_of_element_located(locator)).get_attribute('textContent')
        print('\n Внутри фрейма написано', self.text)

