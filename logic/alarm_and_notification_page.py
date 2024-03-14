class AlarmNotificationPage:
    def __init__(self, driver):
        self.driver = driver

    def click_menu(self):
        menu_button = self.driver.find_element_by_id("com.claudivan.taskagenda:id/hamburguer")
        menu_button.click()

    def click_settings(self):
        settings_button = self.driver.find_element_by_id("com.claudivan.taskagenda:id/tvAjustes")
        settings_button.click()

    def click_alarm_and_notifications(self):
        alarm_and_notifications_button = self.driver.find_element_by_xpath(...)
        alarm_and_notifications_button.click()

    def click_sound_in_event_alarm(self):
        sound_button = self.driver.find_element_by_id("com.claudivan.taskagenda:id/itemSomAlarmeEvento")
        sound_button.click()

    def select_argon(self):
        argon_option = self.driver.find_element_by_xpath(...)
        argon_option.click()

    def click_back(self):
        back_button = self.driver.find_element_by_xpath(...)
        back_button.click()
