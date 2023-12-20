from pages.base_page import Page
from pages.map_page import MapPage
from pages.my_menu_page import MenuPage
from pages.referral_page import ReferralPage
from pages.secondary_page import SecondaryPage
from pages.search_page import SearchPage
from pages.off_plan_page import OffPlanPage
from pages.settings_page import SettingsPage
from pages.workshops_page import WorkshopsPage
from pages.market_page import MarketPage
from pages.sign_in_page import SignInPage


class Applications:

    def __init__(self, driver):
        self.page = Page(driver)
        self.map_page = MapPage(driver)
        self.menu_page = MenuPage(driver)
        self.referral_page = ReferralPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.settings_page = SettingsPage(driver)
        self.workshops_page = WorkshopsPage(driver)
        self.search_page = SearchPage(driver)
        self.market_page = MarketPage(driver)
        self.sign_in_page = SignInPage(driver)