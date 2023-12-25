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
    ### DESKTOP LOCATORS ###
    EMAIL_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    CONTINUE_LOGIN_BUTTON = (By.CSS_SELECTOR, "[wized='loginButton']")
    USER_COUNTER = (By.CSS_SELECTOR, "[wized='usersCounter']")
    NUMBER = (By.XPATH, "//div[@wized='usersCounter']")

    ### MOBILE LOCATORS ###


    ### DESKTOP METHODS ###
    def open_sign_in_page(self):
        self.open_url("https://soft.reelly.io/sign-in")


    def log_in(self, email, password):
        can_input = False
        while can_input == False:
            number = self.find_element(*self.NUMBER).text
            if number != ' ' and number != '-':
                can_input = True
                self.wait_for_text_present(self.USER_COUNTER, text=number)
                self.input(email, *self.EMAIL_FIELD)
                self.input(password, *self.PASSWORD_FIELD)
                self.click(*self.CONTINUE_LOGIN_BUTTON)


    ### MOBILE METHODS ###

