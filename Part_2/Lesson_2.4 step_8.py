from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from my_func import calc
import re
from re import findall

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#price"),"100")
    )
    button_1 = browser.find_element(By.CSS_SELECTOR, "#book").click()

    # на странице находим Х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    # находим окно для ввода и сразу вставляем туда импортируемую функцию с аргументом x,
    # чтобы получить число с ответом
    input = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))

    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # найти и вывести в консоль ответ из alerta
    alert = browser.switch_to.alert
    alert_text = alert.text
    text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)",
                      alert_text)
    print(text)

finally:
    browser.quit()

