import pytest
from allure_commons._allure import step
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selene import browser, have

from vi_project.utils import attach


import config

def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    options = config.to_driver_options(context=context)

    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    browser.config.timeout = 10.0

    yield

    attach.add_screenshot()
    attach.add_xml()
    session_id = browser.driver.session_id

    browser.quit()

    if context == 'bstack':
        attach.add_video(session_id)

@pytest.fixture(scope='function')
def skip_welcome_screen():
    with step('Нажатие на кнопку "Начать"'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/button')).click()

    with step('Пропустить 1-й экран'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/dismiss')).click()

    with step('Пропустить 2-й экран'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/dismiss')).click()

    with step('Пропустить 3-й экран'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/dismiss')).click()