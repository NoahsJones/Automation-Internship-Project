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
    ### DESKTOP LOCATORS ###
    OPEN_SECONDARY = (By.CSS_SELECTOR, "a[href='/secondary-listings']")
    FILTERS_BUTTON = (By.CSS_SELECTOR, "div.filter-button[wized='openFiltersWindow']")
    FT_WANT_TO_SELL = (By.XPATH, "//div[contains(text(), 'Want to sell')]")
    FT_WANT_TO_BUY = (By.XPATH, "//div[contains(text(), 'Want to buy')]")
    FT_ALL = (By.XPATH, "//div[contains(text(), 'All')]")
    APPLY_FILTER = (By.CSS_SELECTOR, "[wized='applyFilterButtonMLS']")
    TAGS = (By.XPATH, "//div[@wized='saleTagMLS']")
    AGENTS = (By.CSS_SELECTOR, "[wized='usersCounter']")
    NUMBER = (By.XPATH, "//div[@wized='usersCounter']")

    ### MOBILE LOCATORS ###
    SECONDARY_TAB = (By.CSS_SELECTOR, "[wized='mobileTabGame']")


    ### DESKTOP METHODS ###
    def open_secondary(self):
        self.wait_for_element_click(*self.OPEN_SECONDARY)
        self.click(*self.OPEN_SECONDARY)


    def verify_secondary_page_opened(self):
        self.verify_partial_url("secondary")


    def open_filters_panel(self):
        self.wait_for_text_present(self.FILTERS_BUTTON, "Filters")
        can_open = False
        while can_open == False:
            number = self.find_element(*self.NUMBER).text
            if number.isdigit():
                can_open = True
                self.click(*self.FILTERS_BUTTON)


    def choose_filter_type(self, type):
        if type == 'Want to sell':
            self.wait_for_element_visible(*self.FT_WANT_TO_SELL)
            self.click(*self.FT_WANT_TO_SELL)
        elif type == 'Want to buy':
            self.wait_for_element_visible(*self.FT_WANT_TO_BUY)
            self.click(*self.FT_WANT_TO_BUY)
        else:
            self.wait_for_element_visible(*self.FT_ALL)
            self.click(*self.FT_ALL)
        self.wait_for_element_visible(*self.APPLY_FILTER)
        self.click(*self.APPLY_FILTER)


    def verify_all_cards_for_filter(self, text):
        self.wait_for_text_present(self.TAGS, text)
        self.scroll_down(5000)
        tags = self.find_elements(*self.TAGS)
        for tag in tags:
            tag_text = tag.text
            assert text in tag_text, f"expected '{text}' but got '{tag_text}'"


    ###### MOBILE METHODS #####

    def mobile_secondary_tab(self):
        self.click(*self.SECONDARY_TAB)