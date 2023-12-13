# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://SunInJuly.github.io/execute_script.html")
#
# try:
#     # Эта строка кода находит элемент на веб-странице, используя driver (экземпляр WebDriver)
#     button = driver.find_element(By.TAG_NAME, "button")
#
#     # location_once_scrolled_into_view - это свойство (property) WebElement в Selenium.
#     # Когда вы обращаетесь к location_once_scrolled_into_view, Selenium прокручивает страницу так,
#     # чтобы элемент был видимым в текущем видимом окне.
#     # Это свойство используется для того, чтобы гарантировать, что элемент, на который вы хотите выполнить действия,
#     # видим в текущем окне просмотра.
#
#     # переменная с именем _, что является общепринятой практикой для случаев,
#     # когда значение переменной не будет использоваться. Также это сигнализирует читателю кода о том,
#     # что значение не играет важной роли в данном контексте.
#     _ = button.location_once_scrolled_into_view
#
#     button.click()
#     assert True
# finally:
#     time.sleep(8)
#     driver.quit()

    # воспроизводим ошибку, при которой требуемый элемент нельзя кликнуть, т.к. он перекрывается другим элементом
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
button.click()