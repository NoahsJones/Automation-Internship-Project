from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



@given("Open main page")
def open_main_page(context):
    context.app.menu_page.open_main_page()


@when("Click on Secondary tab")
def open_secondary_tab(context):
    context.app.secondary_page.open_secondary()