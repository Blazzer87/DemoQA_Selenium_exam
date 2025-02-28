import pytest
from pages.page_11_browser import Page11Browser
from pages.page_12_alerts import Page12Alerts
from pages.page_14_nested_frames import Page14NestedFrames
from pages.page_19_slider import Page19Slider
from pages.page_1_text_box import Page1TextBox
from pages.page_20_progress_bar import Page20ProgressBar
from pages.page_23_menu import Page23Menu
from pages.page_25_sortable import Page25Sortable
from pages.page_27_resizable import Page27Resizable
from pages.page_28_droppable import Page28Droppable
from pages.page_5_buttons import Page5Buttons
from pages.page_8_upload_download import Page8UpDownload
from pages.page_9_dinamic_prop import Page9DinamicProp


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page_textbox = Page1TextBox(driver)
        self.page_buttons = Page5Buttons(driver)
        self.page_updownloads = Page8UpDownload(driver)
        self.page_menu = Page23Menu(driver)
        self.page_sortable = Page25Sortable(driver)
        self.page_droppable = Page28Droppable(driver)
        self.page_browser = Page11Browser(driver)
        self.page_alerts = Page12Alerts(driver)
        self.page_dinamic_prop = Page9DinamicProp(driver)
        self.page_nested_frames = Page14NestedFrames(driver)
        self.page_progress_bar = Page20ProgressBar(driver)
        self.page_slider = Page19Slider(driver)
        self.page_resizable = Page27Resizable(driver)

