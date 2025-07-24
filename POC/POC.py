import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service()
driver = webdriver.ChromiumDriver(service=service_obj)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
time.sleep(2)