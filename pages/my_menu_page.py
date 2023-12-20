from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from support.logger import logger
from selenium.webdriver.common.by import By
from time import sleep


class MenuPage(Page):

    OPEN_MY_MENU = (By.CSS_SELECTOR, "a[href='/'][class*='menu-button']>div")

    def open_my_menu(self):
        self.click(*self.OPEN_MY_MENU)


    def open_main_page(self):
        self.open_url("https://soft.reelly.io/")

