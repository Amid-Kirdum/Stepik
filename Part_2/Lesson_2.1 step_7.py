from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# функция для вычисления значения вносимого в поле input
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # находим элемент-картинку(сундук)
    img_treasure = browser.find_element(By.CSS_SELECTOR, "#treasure")

    #берем у этого элемента значение атрибута "valuex", которое является значением X для задачи
    x_element = img_treasure.get_attribute("valuex")
    # создаём переменную X со значением X_element чтобы подставить в формулу
    x = x_element
    # находим текстовое поле и вносим ответ который вычисляется в (calc(x))
    input = browser.find_element(By.CSS_SELECTOR, "#answer"). send_keys(calc(x))

    # Отметить checkbox "I'm the robot".
    check_box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox"). click()

    # Выбрать radiobutton "Robots rule!".
    radio_btn = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    #Н ажать на кнопку "Submit".
    btn = browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    time.sleep(10)
    browser.quit()