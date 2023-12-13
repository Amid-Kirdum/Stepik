from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # link = "https://suninjuly.github.io/registration1.html"
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, 'input.first[required]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input.second[required]')
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input.third[required]')
    input3.send_keys('test@mail.tt')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)

    browser.quit()