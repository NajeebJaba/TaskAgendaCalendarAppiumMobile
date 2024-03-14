import unittest
from logic.check_event_by_date_page import EventByDatePage


class TestCheckEventByDate(unittest.TestCase):

    def setUp(self):
        self.page = EventByDatePage(self.driver)

    def test_check_event_by_date(self):
        expected_event_title = "aaa"
        self.page.click_calendar()
        self.page.select_date("28")
        self.page.click_on_event()

        actual_event_title = self.page.get_event_title()
        self.assertEqual(actual_event_title, expected_event_title, f"Event title does not match. Expected: '{expected_event_title}', Got: '{actual_event_title}'")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()