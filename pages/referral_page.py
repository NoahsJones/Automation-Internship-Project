from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from support.logger import logger
from selenium.webdriver.common.by import By
from time import sleep


class ReferralPage(Page):

    OPEN_REFERRAL = (By.CSS_SELECTOR, "a[href='/referral/dashboard']>div")

    def open_referral(self):
        self.click(*self.OPEN_REFERRAL)