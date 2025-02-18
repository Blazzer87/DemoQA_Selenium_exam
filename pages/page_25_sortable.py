from links.links import Links
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Page25Sortable(BasePage):

    url = Links.page_sortable_url

    list_one_locator = ('xpath', '//div[contains(@class,"vertical")]//div[text()="One"]')
    list_two_locator = ('xpath', '//div[contains(@class,"vertical")]//div[text()="Two"]')
    list_three_locator = ('xpath', '//div[contains(@class,"vertical")]//div[text()="Three"]')
    list_four_locator = ('xpath', '//div[contains(@class,"vertical")]//div[text()="Four"]')
    list_five_locator = ('xpath', '//div[contains(@class,"vertical")]//div[text()="Five"]')
    list_six_locator = ('xpath', '//div[contains(@class,"vertical")]//div[text()="Six"]')

    grid_locator = ('xpath', '//a[@id="demo-tab-grid"]')

    grid_one_locator = ('xpath', '//div[@class="create-grid"]/div[text()="One"]')
    grid_two_locator = ('xpath', '//div[@class="create-grid"]/div[text()="Two"]')
    grid_three_locator = ('xpath', '//div[@class="create-grid"]/div[text()="Three"]')
    grid_four_locator = ('xpath', '//div[@class="create-grid"]/div[text()="Four"]')
    grid_five_locator = ('xpath', '//div[@class="create-grid"]/div[text()="Five"]')
    grid_six_locator = ('xpath', '//div[@class="create-grid"]/div[text()="Six"]')
    grid_seven_locator = ('xpath', '//div[@class="create-grid"]/div[text()="Seven"]')
    grid_eight_locator = ('xpath', '//div[@class="create-grid"]/div[text()="Eight"]')
    grid_nine_locator = ('xpath', '//div[@class="create-grid"]/div[text()="Nine"]')

    def drag_and_drop_list_nine_to_one(self):
        self.action.drag_and_drop(
            self.wait.until(EC.visibility_of_element_located(self.list_six_locator)),
            self.wait.until(EC.visibility_of_element_located(self.list_one_locator))
        )
        self.action.pause(1)
        self.action.perform()

    def go_to_grid (self):
        self.wait.until(EC.element_to_be_clickable(self.grid_locator)).click()

    def drag_and_drop_grid_nine_to_one(self):
        self.action.drag_and_drop(
            self.wait.until(EC.element_to_be_clickable(self.grid_nine_locator)),
            self.wait.until(EC.element_to_be_clickable(self.grid_one_locator))
        )
        self.action.pause(1)
        self.action.perform()
