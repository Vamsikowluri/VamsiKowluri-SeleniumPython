import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
time.sleep(2)
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[class='btn btn-success']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
time.sleep(2)
print(message)
assert "Success" in message

#need to push

