import os

import allure
from dotenv import load_dotenv
from selene import browser

from vi_project import utils


def add_video(session_id):

    import requests
    load_dotenv(dotenv_path=utils.file.abs_path_from_project(
        '.env.credentials'))
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(os.getenv('USER_NAME'), os.getenv('ACCESS_KEY'))
        ).json()
    print(bstack_session)
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )

def add_screenshot():
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png,
                  name='Screenshot',
                  attachment_type=allure.attachment_type.PNG)


def add_xml():
    xml_dump = browser.driver.page_source
    allure.attach(body=xml_dump,
                  name='XML screen',
                  attachment_type=allure.attachment_type.XML)