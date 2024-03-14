import unittest
from infra.task_driver import TaskAgendaDriver
from logic.add_event_page import AddEventPage


class TestTaskAgenda(unittest.TestCase):

    def setUp(self):
        self.driver = TaskAgendaDriver()
        self.page = AddEventPage(self.driver)

    def test_add_new_event_for_today(self):
        event_name = "Study"
        description = "In AppFlyer"

        # Act
        self.page.click_plus()
        self.page.select_today()
        self.page.enter_event_name(event_name)
        self.page.enter_description(description)
        self.page.save_event()

        self.assertIn(event_name, self.page.get_event_titles(), "Event name not found in the agenda view.")
        self.assertIn(description, self.page.get_event_descriptions(),
                      "Event description not found in the agenda view.")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
