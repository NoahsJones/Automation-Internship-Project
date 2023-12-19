from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from support.logger import logger
from selenium.webdriver.common.by import By
from time import sleep


class SecondaryPage(Page):

    OPEN_SECONDARY = (By.CSS_SELECTOR, "a[href='/secondary-listings'][aria-current='page']>div[class='div-block-33']")

    def open_secondary(self):
        self.click(*self.OPEN_SECONDARY)
