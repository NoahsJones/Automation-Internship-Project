from pages.base_page import Page
from pages.map_page import MapPage
from pages.my_menu_page import MenuPage
from pages.referral_page import ReferralPage
from pages.secondary_page import SecondaryPage
from pages.search_page import SearchPage


class Applications:

    def __init__(self, driver):
        self.page = Page(driver)
        self.map_page = MapPage(driver)
        self.menu_page = MenuPage(driver)
        self.referral_page = ReferralPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.search_page = SearchPage(driver)