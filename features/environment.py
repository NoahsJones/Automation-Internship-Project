from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from apps.applications import Applications
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait



def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    ####CHROME BROWSER###
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    ##CHROME HEADLESS MODE##
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(options=options, service=service)
    context.driver.set_window_size(2000, 1000)
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 20)
    context.app = Applications(context.driver)

    ###FIREFOX BROWSER###
    # DESKTOP PATH#
    # service = Service(executable_path="C:/Users/noahsj/Desktop/Automation Internship Project/geckodriver.exe")
    # LAPTOP PATH#
    # service = Service(executable_path="...")
    # context.driver = webdriver.Firefox(service=service)

    ###SAFARI BROWSER### can't use since I do not have Safari installed
    # context.driver = webdriver.Safari()


    # # ##BROWSERSTACK EDGE##
    # bs_user = 'noahsj_p3KDFs'
    # bs_key = 'BAiKTuqj9kkQtzaDyRBE'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     "browserName" : "Edge",
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    # ##BROWSERSTACK FIREFOX##
    # bs_user = 'noahsj_p3KDFs'
    # bs_key = 'BAiKTuqj9kkQtzaDyRBE'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    ####GENERAL SETTINGS####
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.driver.wait = WebDriverWait(context.driver, 20)
    # context.app = Applications(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
