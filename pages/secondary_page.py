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

    OPEN_SECONDARY = (By.CSS_SELECTOR, "a[href='/secondary-listings']")
    FILTERS_BUTTON = (By.CSS_SELECTOR, "[wized='openFiltersWindow']")
    FT_WANT_TO_SELL = (By.XPATH, "//div[contains(text(), 'Want to sell')]")
    FT_WANT_TO_BUY = (By.XPATH, "//div[contains(text(), 'Want to buy')]")
    FT_ALL = (By.XPATH, "//div[contains(text(), 'All')]")
    APPLY_FILTER = (By.CSS_SELECTOR, "[wized='applyFilterButtonMLS']")
    CARDS = (By.CSS_SELECTOR, "[wized = 'saleTagBoxMLS']")

    def open_secondary(self):
        # sleep(4)
        self.wait_for_element_click(*self.OPEN_SECONDARY)
        self.click(*self.OPEN_SECONDARY)


    def verify_secondary_page_opened(self):
        self.verify_partial_url("secondary")


    def open_filters_panel(self):
        # sleep(5)
        self.wait_for_element_visible(*self.FILTERS_BUTTON)
        self.click(*self.FILTERS_BUTTON)


    def choose_filter_type(self, type):
        # sleep(5)
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
        # sleep(5)
        cards = self.find_elements(*self.CARDS)
        self.scroll_down(500)
        for card in cards:
            tag = (By.XPATH, "//div[contains(text(), 'For sale')]")
            assert tag, f"{tag} is not found in {card}"
