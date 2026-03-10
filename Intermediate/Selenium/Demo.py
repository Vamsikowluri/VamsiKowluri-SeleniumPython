import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/client")

# Text visible in the web screen
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
time.sleep(5)

# Using the parent to child tags
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.XPATH, "//type=password").send_keys("Hello@1234")

# In CSS for id we can use #
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
time.sleep(5)
driver.find_element(By.XPATH, "//button[@type='submit']").click()