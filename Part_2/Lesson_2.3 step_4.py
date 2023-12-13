from selenium import webdriver

from selenium.webdriver.common.by import By
import time
from my_func import calc

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # Нажать на кнопку
    _ = browser.find_element(By.CSS_SELECTOR, ".btn").click()

    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # На новой странице находим Х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    # находим окно для ввода и сразу вставляем туда импортируемую функцию с аргументом x,
    # чтобы получить число с ответом
    input = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))

    button = browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    time.sleep()
    browser.quit()

