import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui 
def test_check_incorrect_username():
    # Create object for driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open page https://github.com/login
    driver.get("https://github.com/login")    

    # Find field  to input username or email
    login_elem = driver.find_element(By.ID, "login_field")

    # input incorrect username or email
    login_elem.send_keys("viktord@gmail.com")

    # Finf field to input incorrect password
    pass_elem = driver.find_element(By.ID, "password")

    # input incorrect password
    pass_elem.send_keys("wrong password")

    # find button sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    # emulate a click
    btn_elem.click()

    # verify page name
    assert driver.title == "Sign in to GitHub · GitHub"
    time.sleep(3)

    # close browser
    driver.close()
    