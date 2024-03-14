from infra.task_driver import TaskAgendaDriver


class DarkModePage(TaskAgendaDriver):
    def __init__(self, driver):
        self.driver = driver

    def click_menu(self):
        menu_button = self.driver.find_element_by_id("com.claudivan.taskagenda:id/hamburguer")
        menu_button.click()

    def click_colors_and_event_types(self):
        colors_and_event_types_button = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Colors and event types']")
        colors_and_event_types_button.click()

    def click_dark_mode(self):
        dark_mode_button = self.driver.find_element_by_id("com.claudivan.taskagenda:id/itemTemaEscuro")
        dark_mode_button.click()

    def click_enable(self):
        enable_button = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='android:id/text1' and @text='Enabled']")
        enable_button.click()

    def click_save(self):
        save_button = self.driver.find_element_by_id("com.claudivan.taskagenda:id/item_salvar")
        save_button.click()