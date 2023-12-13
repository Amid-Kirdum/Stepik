import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    #проверяем значение атрибута checked у people_radio
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked == "true", "People radio is not selected by default"

    #проверяем значение атрибута checked у robots_radio
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots rule:", robots_checked)
    assert robots_checked is None

    #проверяем значение атрибута disabled у кнопки Submit
    btn_submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn_disabled = btn_submit.get_attribute("disabled")
    print("value of button submit:",btn_disabled)
    assert btn_disabled is None

    #проверяем значение атрибута disabled у кнопки Submit после таймаута
    time.sleep(5)
    btn_disabled = btn_submit.get_attribute("disabled")
    print("value of button submit after 10sec:", btn_disabled)
    assert btn_disabled is None

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()