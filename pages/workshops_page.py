from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from support.logger import logger
from selenium.webdriver.common.by import By
from time import sleep


class WorkshopsPage(Page):

    OPEN_WORKSHOPS = (By.CSS_SELECTOR, "a[wized='educationPageMenu']")

    def open_workshops(self):
        self.click(*self.OPEN_WORKSHOPS)