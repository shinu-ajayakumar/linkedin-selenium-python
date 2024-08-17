import random
import time
from operator import truediv

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

global_timeout = 30

class ElementHelper:



    def __init__(self, driver):
        self.driver = driver
        self.random_timeout = random.randint(5,10)

    def enter_text(self, txt_field, text_to_enter):
        time.sleep(random.randint(5,10))
        try:
            WebDriverWait(self.driver,global_timeout).until(EC.presence_of_element_located(txt_field))
            self.driver.find_element(*txt_field).send_keys(text_to_enter)
            print(f"Set Element text : {txt_field}")
        except Exception as e:
            print(f"An error occurred : {e}")
            return False

    def click(self, click_field):
        time.sleep(random.randint(5,10))
        try:
            WebDriverWait(self.driver, global_timeout).until(EC.presence_of_element_located(click_field))
            self.driver.find_element(*click_field).click()
            print(f"Clicked Element : {click_field}")
        except Exception as e:
            print(f"An error occurred : {e}")
            return False


