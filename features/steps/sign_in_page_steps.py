from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



@given("Open sign-in page")
def open_sign_in(context):
    context.app.sign_in_page.open_sign_in_page()


@when("Log in with email: {email} and password: {password}")
def logging_in(context, email, password):
    context.app.sign_in_page.log_in(email, password)