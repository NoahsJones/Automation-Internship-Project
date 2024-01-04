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



#### MOBILE STEPS ####

@when("Mobile - Tap on Off-Plan tab")
def mobile_tap_off_plan_tab(context):
    context.app.menu_page.mobile_open_off_plan_tab()


@when("Mobile - Tap on secondary market")
def mobile_tap_off_plan_tab(context):
    context.app.page.scroll_down(6000)
    context.app.menu_page.open_secondary_market()


@when("Mobile - Tap on Secondary tab")
def mobile_tap_secondary_tab(context):
    context.app.menu_page.mobile_open_secondary_tab()