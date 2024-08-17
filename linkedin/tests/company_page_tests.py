import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), "..",".."))
from selenium import webdriver
from linkedin.pages.home_page import HomePage
from linkedin.pages.login_page import LoginPage


def test_company_page_send_invites():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    login_page.open_page()
    login_page.login()
    home_page.search_for("Adobe")
    time.sleep(5)
    driver.quit()