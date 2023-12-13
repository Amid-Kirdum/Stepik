from selenium import webdriver
from selenium.webdriver.common.by import By
from my_func import calc
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # Считать значение для переменной x, передать её в текст
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    x = x_element

    #вычислить значение с помощью импортированной функции calc, ввести ответ в текстовое поле
    input = browser.find_element(By.CSS_SELECTOR, ".form-control").send_keys(calc(x))

    # Проскроллить страницу вниз
    button = browser.find_element(By.CSS_SELECTOR,".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Выбрать checkbox "I'm the robot"
    checkbox = browser.find_element(By.CSS_SELECTOR, ".form-check-input").click()

    # Переключить radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    # Нажать на кнопку "Submit"
    button.click()

finally:
    time.sleep(5)
    browser.quit()

