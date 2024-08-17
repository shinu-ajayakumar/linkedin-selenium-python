import random
import time


class ElementHelper:

    def __init__(self, driver):
        self.driver = driver
        self.random_timeout = random.randint(5,10)

    def enter_text(self, txt_field, text_to_enter):
        time.sleep(random)
        self.driver.find_element(*txt_field).send_keys(text_to_enter)

    def click(self, click_field):
        time.sleep(random)
        self.driver.find_element(*click_field).click()

