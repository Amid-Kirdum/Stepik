from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    # Заполнить текстовые поля: имя, фамилия, email
    input_first_name = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys ("John")
    input_last_name = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys ("Doe")
    input_email = browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys ("j_d@mail.h")

    #Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    # print(file_path)
    element.send_keys(file_path)

    # не забывай CLICK() в конце!!!!!!
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()

