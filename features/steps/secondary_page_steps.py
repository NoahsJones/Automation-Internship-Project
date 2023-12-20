from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then("Verify Secondary page opens")
def verify_secondary_page(context):
    context.app.secondary_page.verify_secondary_page_opened()


@when("Click on Filters")
def open_filters_panel(context):
    context.app.secondary_page.open_filters_panel()


@when("Filter for {listing_type}")
def choose_filter_type(context, listing_type):
    context.app.secondary_page.choose_filter_type(listing_type)


@then("Verify all cards have: {tag} tag")
def verify_cards_filters(context, tag):
    context.app.secondary_page.verify_all_cards_for_filter(tag)
