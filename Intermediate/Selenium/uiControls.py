import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

sleep(2)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
time.sleep(2)

radiobutton = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radiobutton))

for radio in radiobutton:
    if radio.get_attribute("value") == "radio2":
        radio.click()
        assert radio.is_selected()
time.sleep(2)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(5)
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.CSS_SELECTOR, ".example").text)













