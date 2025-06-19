import os

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

from vi_project import utils


def to_driver_options(context):
    options = UiAutomator2Options()

    if context == 'local_emulator':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))  # адрес удаленного сервера
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))  # имя устройства
        options.set_capability('appPackage', os.getenv('APP_PACKAGE'))
        options.set_capability('appActivity', os.getenv(
            'APP_ACTIVITY'))  # активити, которая будет открыта после запуска apk файла
        # options.set_capability('udid', os.getenv('UDID')) # уникальный идентификатор устройства
        options.set_capability('app', utils.file.abs_path_from_project(os.getenv('APP')))  # путь до apk файла

    if context == 'local_real_device':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        # options.set_capability('udid', os.getenv('UDID'))
        options.set_capability('app', utils.file.abs_path_from_project(os.getenv('APP')))

    if context == 'bstack':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
        options.set_capability('platformVersion', os.getenv('PLATFORM_VERSION'))
        options.set_capability('language', os.getenv('LANGUAGE'))
        options.set_capability('locale', os.getenv('LOCALE'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', os.getenv('APP'))
        load_dotenv(dotenv_path=utils.file.abs_path_from_project(
            '.env.credentials'))  # загрузка переменных окружения из файла .env.credentials
        options.set_capability(
            'bstack:options', {
                'projectName': 'Wikipedia project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack test',
                'userName': os.getenv('USER_NAME'),
                'accessKey': os.getenv('ACCESS_KEY'),
            },
        )

    return options