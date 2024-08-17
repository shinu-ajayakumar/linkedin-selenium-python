from selenium.webdriver.common.by import By

from linkedin.helpers.assert_helper import AssertHelper
from linkedin.helpers.element_helper import ElementHelper

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.element_helper = ElementHelper(self.driver)
        self.assert_helper = AssertHelper(self.driver)
        self.txt_search = (By.CSS_SELECTOR,"input[aria-label=Search]")
        self.btn_search = (By.CSS_SELECTOR, "div[class*='search-icon']")


    def enter_search(self, search_keyword):
        self.element_helper.enter_text(self.txt_search, search_keyword)

    def click_search(self):
        self.element_helper.click(self.btn_search)

    def search_for(self, search_keyword):
        self.enter_search(search_keyword)
        self.click_search()
