import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",".."))
from linkedin.helpers.driver_helper import DriverHelper
from linkedin.helpers.element_helper import ElementHelper
from selenium.webdriver.common.by import By

username = str(os.getenv('LINKEDIN_USER_NAME'))
password = str(os.getenv('LINKEDIN_PASSWORD'))

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.page_url = "https://www.linkedin.com/checkpoint/lg/login"
        self.txt_username = (By.ID,"username")
        self.txt_password = (By.ID,"password")
        self.btn_signIn = (By.CSS_SELECTOR,"button[aria-label='Sign in']")
        self.element_helper = ElementHelper(self.driver)
        self.driver_helper = DriverHelper(self.driver)

    def open_page(self):
        self.driver.get(self.page_url)

    def enter_username(self, username):
        self.element_helper.enter_text(self.txt_username,username)

    def enter_password(self, password):
        self.element_helper.enter_text(self.txt_password,password)

    def click_signin(self):
        self.element_helper.click(self.btn_signIn)

    def get_page_title(self):
        return  self.driver_helper.get_page_title()

    def login(self):
        self.enter_username(username)
        self.enter_password(password)
        self.click_signin()