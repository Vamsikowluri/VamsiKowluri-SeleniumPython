import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

time.sleep(2)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

time.sleep(2)
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break
time.sleep(5)

