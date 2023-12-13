from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # находим первую цифру, записываем её в текст
    num_1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    # print(num_1)

    # находим вторую цифру, записываем её в текст
    num_2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    # print(num_2)

    # складываем полученные числа, предварительно переведя их в числа (int), т.к. в Python это изначально строки
    sum = int(num_1) + int(num_2)
    # print(sum)

    # находим выпадающий список и выбираем в нем значение,
    # равное ранее полученной сумме чисел (предварительно переведя число в строку)
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(sum))

    # находим и нажимаем кнопку submit
    btn = browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    time.sleep(10)
    browser.quit()

