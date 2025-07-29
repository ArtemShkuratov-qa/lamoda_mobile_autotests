from selene import browser
from selenium.webdriver.common.actions.action_builder import ActionBuilder


def perform_tap_at_coordinates(x: int, y: int):
    """Кликает по заданным координатам."""
    driver = browser.config.driver
    actions = ActionBuilder(driver)  # Предполагается, что browser — это объект Selene
    actions.add_pointer_input("touch", "my_touch_device")  # Сразу добавляем указатель в ActionBuilder

    # Перемещение указателя и выполнение нажатия
    actions.pointer_action.move_to_location(x, y)
    actions.pointer_action.pointer_down(button=0)
    actions.pointer_action.pause(duration=0.1)
    actions.pointer_action.pointer_up(button=0)

    # Выполнение последовательности действий
    actions.perform()