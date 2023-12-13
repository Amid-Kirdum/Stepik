from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()

finally:
    time.sleep(5)
    browser.quit()

