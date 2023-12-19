from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from support.logger import logger
from selenium.webdriver.common.by import By
from time import sleep


class SettingsPage(Page):

    OPEN_SETTINGS = (By.CSS_SELECTOR, "a[href='/settings']>div[class='menu-icon w-embed']")

    def open_settings(self):
        self.click(*self.OPEN_SETTINGS)


