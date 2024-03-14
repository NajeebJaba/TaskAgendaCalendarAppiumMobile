import unittest
from logic.dark_mode_page import DarkModePage


class TestEnableDarkMode(unittest.TestCase):

    def setUp(self):
        self.page = DarkModePage(self.driver)

    def test_enable_dark_mode(self):
        self.page.click_menu()
        self.page.click_colors_and_event_types()
        self.page.click_dark_mode()
        self.page.click_enable()
        self.page.click_save()

    def test_enable_dark_mode(self):
        self.assertTrue(self.page.is_dark_mode_enabled(), "Dark Mode was not enabled successfully.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()