from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
time.sleep(15)
driver.maximize_window()


driver.add_cookie({"name":"Harika","value":"20"})
cookies = driver.get_cookies()
print(len(cookies))

for cookie in cookies:
    print(cookie)
    print(cookie.get('name'),':',cookie.get('value'))

driver.delete_cookie("Harika")
driver.delete_all_cookies()
driver.get_cookies()
print(len(cookies))
driver.quit()

