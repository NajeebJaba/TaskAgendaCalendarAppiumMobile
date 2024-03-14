import unittest
from logic.alarm_and_notification_page import AlarmNotificationPage


class TestAlarmAndNotification(unittest.TestCase):

    def setUp(self):
        self.page = AlarmNotificationPage(self.driver)

    def test_change_alarm_sound_to_silent(self):
        self.page.click_menu()
        self.page.click_settings()
        self.page.click_alarm_and_notifications()
        self.page.click_sound_in_event_alarm()
        self.page.select_argon()
        self.page.click_back()

        self.assertEqual(self.page.get_current_sound_setting(), "Silent", "Sound setting is not set to Silent.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
