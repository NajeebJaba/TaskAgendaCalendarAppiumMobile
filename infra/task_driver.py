from appium import webdriver

class TaskAgendaDriver:
    def get_driver(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'platformVersion': '11.0',
            'appPackage': 'com.claudivan.taskagenda',
            'appActivity': 'YOUR_APP_MAIN_ACTIVITY',
            'automationName': 'UiAutomator2'
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return driver

    def find_element_by_id(self, element_id):
        return self.driver.find_element_by_id(element_id)

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def click(self, element):
        element.click()

    def send_keys(self, element, keys):
        element.send_keys(keys)
