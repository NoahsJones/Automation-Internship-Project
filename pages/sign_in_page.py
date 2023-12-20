from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from support.logger import logger
from selenium.webdriver.common.by import By
from time import sleep


class SignInPage(Page):
    EMAIL_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    CONTINUE_LOGIN_BUTTON = (By.CSS_SELECTOR, "[wized='loginButton']")

    def open_sign_in_page(self):
        self.open_url("https://soft.reelly.io/sign-in")


    def log_in(self, email, password):
        sleep(1)
        self.wait_for_element_click(*self.EMAIL_FIELD)
        self.wait_for_element_click(*self.PASSWORD_FIELD)
        self.input(email, *self.EMAIL_FIELD)
        self.input(password, *self.PASSWORD_FIELD)
        self.click(*self.CONTINUE_LOGIN_BUTTON)
