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

    ### DESKTOP LOCATORS ###
    OPEN_MY_MENU = (By.CSS_SELECTOR, "a[href='/'][class*='menu-button']")
    ADD_A_PROJECT_BUTTON = (By.CSS_SELECTOR, "a[href='/add-a-project']")
    USER_COUNTER = (By.CSS_SELECTOR, "[wized='usersCounter']")


    ### MOBILE LOCATORS ###
    SECONDARY_TAB = (By.CSS_SELECTOR, "[wized='mobileTabGame']")
    OFF_PLAN_TAB = (By.XPATH, "//*[@class='menu-button-text' and text()='Off-plan']") #Does not work but shows valid
    MARKET_TAB = (By.CSS_SELECTOR, "a[href='/education']")
    ENTIRE_MENU_BAR_TABS = (By.CSS_SELECTOR, "[wized='mobileMenuForVerifiedUsers']") #Does not work but shows valid
    ABSOLUTE_PATH_OFF_PLAN_TAB = (By.XPATH, "/html/body/div[4]/a[1]/div[2]") #Works but obviously not most stable



    ### DESKTOP METHODS ###
    def open_my_menu(self):
        self.click(*self.OPEN_MY_MENU)


    def open_main_page(self):
        self.open_url("https://soft.reelly.io/")


    def add_project(self):
        self.click(*self.ADD_A_PROJECT_BUTTON)


    ### MOBILE METHODS ###

    def mobile_open_off_plan_tab(self):
        self.click(*self.ABSOLUTE_PATH_OFF_PLAN_TAB)



    def mobile_open_secondary_tab(self):
        self.click(*self.SECONDARY_TAB)

