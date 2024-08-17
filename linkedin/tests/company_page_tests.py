import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",".."))
import time
from selenium import webdriver
from linkedin.pages.login_page import LoginPage



def test_company_page_send_invites():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.enter_username("")
    login_page.enter_password("")
    time.sleep(5)
    title = login_page.get_page_title()
    if title == "LinkedIn Login, Sign in | LinkedIn":
        print("Expected title : "+ title)
    else:
        print("Unexpected title : "+title)
    driver.quit()