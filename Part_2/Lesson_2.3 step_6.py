from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from my_func import calc
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # это не обязательно!!! просто опция, чтобы кнопка не летала по экрану
    # У каждого тега могут быть атрибуты ID или class. Обычно на них и вешается какое-то событие через CSS или JS
    # Если убрать trollface, то и анимация пропадёт. Это поле я и удаляю.
    browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")

    # определяем текущее окно (не обязательно!!!)
    current_window = browser.current_window_handle

    # находим и нажимаем  кнопку на первом окне
    first_btn = browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    # определяем новое окно и переходим на него
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # найти x
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    # Пройти капчу для робота и получить число-ответ
    input = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))

    btn = browser.find_element(By.CSS_SELECTOR, ".btn").click()

    # alert = browser.switch_to.alert
    # alert_text = alert.text
    # text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)",
    #                   alert_text)
    # print(text)

finally:
    time.sleep(4)
    browser.quit()
