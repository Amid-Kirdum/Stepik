import unittest

# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
#
#     def test_abs2(self):
#         self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
#
#
# if __name__ == "__main__":
#     unittest.main()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# def test_1
# try:
#     link = "https://suninjuly.github.io/registration2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required]")
#     input3.send_keys("email")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
#     time.sleep(1)
#
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     welcome_text = welcome_text_elt.text
#
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     time.sleep(10)
#     browser.quit()
#
