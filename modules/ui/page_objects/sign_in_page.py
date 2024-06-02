from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Find field to input incorrect username or email
        login_elem = self.driver.find_element(By.ID, "login_field") 

        # input incorrect username or email
        login_elem.send_keys(username)

        # Finf field to input incorrect password
        pass_elem = self.driver.find_element(By.ID, "password")

        # input incorrect password
        pass_elem.send_keys(password)

        # find button sign in
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # emulate a click
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title    