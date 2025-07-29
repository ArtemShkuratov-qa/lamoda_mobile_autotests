from allure import step
from selenium.webdriver.support import expected_conditions as EC
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be
from selenium.webdriver.support.wait import WebDriverWait
from lamoda_mobile_autotests.utils.gui_utils import perform_tap_at_coordinates


@allure.title('Проверка поиска')
def test_search(skip_welcome_screen):
    with step('Выполняем тап по поисковой строке и вводим данные в строку поиска'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/searchTextView')).click()
        search_field = browser.element((AppiumBy.ID, 'com.lamoda.lite:id/searchEditText')).with_(timeout=8)
        search_field.type('рубашка')

    with step('Выбираем элемент из найденной выборки'):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).second.click()

    with step('Дожидаемся элемента "Показать похожие"'):
        WebDriverWait(browser.config.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, 'com.lamoda.lite:id/tooltip_text'))
        )

    with step('Выполняем тап вне активных кнопок'):
        perform_tap_at_coordinates(980, 426)

    with step('Проверяем, что первый элемент содержит текст из поиска'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/nameSingleLineFadingTextView')).should(have.text('Рубашка '))

    with step('Проверяем, что количество найденных элементов больше 0'):
        browser.all((AppiumBy.ID, 'com.lamoda.lite:id/nameSingleLineFadingTextView')).should(have.size_greater_than(0))


@allure.title('Провека содержимого онбординг экрана')
def test_onboarding_screen():
    with step('Нажатие на кнопку "Начать"'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/button')).click()

    with step('Проверяем отображение 1-го экрана и его заголовок'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/headline')).should(be.visible)
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/headline')).should(have.text('Пишем только по делу!'))

    with step('Выполняем переход на 2-й экран'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/dismiss')).click()

    with step('Проверяем отображение 2-го экрана и его заголовок'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/headline')).should(be.visible)
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/headline')).should(have.text('Пункты выдачи рядом с домом'))

    with step('Выполняем переход на 3-й экран'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/dismiss')).click()

    with step('Проверяем отображение 3-го экрана и его заголовок'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/headline')).should(be.visible)
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/headline')).should(have.text('Войди и получи скидку 10%'))

    with step('Пропустить 3-й экран'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/dismiss')).click()

    with step('Проверяем отображение домашнего экрана'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/root_home')).should(be.visible).with_(timeout=5)


@allure.title('Добавление товара в избранное')
def test_add_item_to_favorite(skip_welcome_screen):
    with step('Проверяем, что карточка товара отображается'):
        browser.element((AppiumBy.CLASS_NAME, 'android.view.View')).should(be.visible)

    with step('Добавляем товар в избранное'):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.CheckBox')).click()

    with step('Переходим в "Избранное"'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Избранное')).click()

    with step('Проверяем наличие товара в избранном'):
        browser.all((AppiumBy.ID, 'com.lamoda.lite:id/catalogItemRoot')).should(have.size(1))


@allure.title('Добавление товара в корзину')
def test_add_product_to_cart(skip_welcome_screen):
    with step('Переходим в каталог'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Каталог')).click()

    with step('Переходим в категорию "Новинки"'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Новинки"]')).click()

    with step('Переходим в категорию "Обувь"'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.lamoda.lite:id/title" and @text="Обувь"]')).click()

    with step('Дожидаемся элемента "Показать похожие"'):
         WebDriverWait(browser.config.driver, 10).until(
             EC.element_to_be_clickable((AppiumBy.ID, 'com.lamoda.lite:id/tooltip_text'))
             )

    with step('Выполняем тап вне активных кнопок'):
        perform_tap_at_coordinates(980, 426)

    with step('Выполняем тап по карточке товара'):
        results = browser.all((AppiumBy.ID, 'com.lamoda.lite:id/priceTextView'))
        results[1].click()

    with step('Закрываем вспывающее окно'):
        if browser.element((AppiumBy.CLASS_NAME, 'android.widget.ImageView')).should(be.visible):
            browser.element((AppiumBy.ID, 'com.lamoda.lite:id/ypaySplitOnboardingApplyButton')).click()

    with step('Выбираем размер'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/cellLayout')).click()

    with step('Наживаем на кнопку "Добавить в корзину"'):
        browser.element((AppiumBy.ID, 'com.lamoda.lite:id/buyButtonWidget')).click()

    with step('Осуществляем переход в "Корзину"'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Корзина')).click()

    with step('Проверяем количество товара в корзине'):
        results = browser.all((AppiumBy.ID, 'com.lamoda.lite:id/name')).should(have.size(1))

