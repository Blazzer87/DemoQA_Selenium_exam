
from links.links import Links
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Page28Droppable(BasePage):

    url = Links.page_droppable_url

    simple_drag_me_locator = ('xpath', '//div[@id="draggable"]')
    simple_drop_here_locator = ('xpath', '//div[@id="droppable"]')


    def drag_and_drop_simple_drag_me_to_simple_drop_here(self):
        self.action.drag_and_drop(
            self.wait.until(EC.visibility_of_element_located(self.simple_drag_me_locator)),
            self.wait.until(EC.visibility_of_element_located(self.simple_drop_here_locator)))
        self.action.pause(2)
        self.action.perform()

    def check_success(self):
        assert self.driver.find_element(*self.simple_drop_here_locator).get_attribute('textContent') == 'Dropped!', 'Что-то пошло не так'
