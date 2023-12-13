from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser= webdriver.Chrome()
# применение неявного ожидания(теперь webriver будет искать каждый элемент в течение 5 секунд)
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")

# Нажать на кнопку "Verify"
button = browser.find_element(By.ID, 'verify')
button.click()
# Проверить, что появилась надпись "Verification was successful!"
message = browser.find_element(By.ID, 'verify_message')

assert "successful" in message.text