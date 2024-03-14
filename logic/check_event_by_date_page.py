from infra.task_driver import TaskAgendaDriver

class EventByDatePage(TaskAgendaDriver):
    def __init__(self, driver):
        self.driver = driver

    def click_calendar(self):
        calendar_button = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Calendar']")
        calendar_button.click()

    def select_date(self, date_text="28"):
        date_button = self.driver.find_element_by_xpath(f"//android.widget.TextView[@text='{date_text}']")
        date_button.click()

    def click_on_event(self):
        event_element = self.driver.find_element_by_xpath("//android.widget.ListView[@resource-id='com.claudivan.taskagenda:id/lvListaEventos']/android.widget.FrameLayout/android.widget.RelativeLayout")
        event_element.click()