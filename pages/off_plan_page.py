from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from support.logger import logger
from selenium.webdriver.common.by import By
from time import sleep


class OffPlanPage(Page):

    OPEN_OFF_PLAN = (By.CSS_SELECTOR, "a[href='/off-plan']")

    def open_off_plan(self):
        self.click(*self.OPEN_OFF_PLAN)
