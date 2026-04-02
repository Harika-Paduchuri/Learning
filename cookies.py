from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
time.sleep(5)
driver.maximize_window()


driver.add_cookie({"name":"Harika","value":"2010"})
cookies = driver.get_cookies()
print(len(cookies))
# hP=happy new year
for cookie in cookies:
    print(cookie)
    print(cookie.get('name'),':',cookie.get('value'))
#secind try for commit message
driver.delete_cookie("Harika")
driver.delete_all_cookies()
driver.get_cookies()
print(len(cookies))
driver.quit()