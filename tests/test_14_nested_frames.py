from tests.base_test import BaseTest


class Test14NestedFrames(BaseTest):


    def test_14_nested_frames(self):
        self.page_nested_frames.open_page(self.page_nested_frames.url)
        self.page_nested_frames.switch_to_parent_frame_by_id()
        self.page_nested_frames.find_text(self.page_nested_frames.parent_frame_locator)
        self.page_nested_frames.switch_to_frame_by_index()
        self.page_nested_frames.find_text(self.page_nested_frames.child_frame_locator)

