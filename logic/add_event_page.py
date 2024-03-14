from infra.task_driver import TaskAgendaDriver


class AddEventPage(TaskAgendaDriver):
    def __init__(self, driver):
        self.driver = driver

    def click_plus(self):
        plus_button = self.driver.find_element_by_id("com.claudivan.taskagenda:id/btNovoEvento")
        self.driver.click(plus_button)

    def select_today(self):
        today_option = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='android:id/text1' and @text='Today']")
        self.driver.click(today_option)

    def enter_event_name(self, name):
        event_name_field = self.driver.find_element_by_id("com.claudivan.taskagenda:id/etTitulo")
        self.driver.send_keys(event_name_field, name)

    def enter_description(self, description):
        description_field = self.driver.find_element_by_id("com.claudivan.taskagenda:id/etDescricao")
        self.driver.send_keys(description_field, description)

    def save_event(self):
        save_button = self.driver.find_element_by_id("com.claudivan.taskagenda:id/item_salvar")
        self.driver.click(save_button)