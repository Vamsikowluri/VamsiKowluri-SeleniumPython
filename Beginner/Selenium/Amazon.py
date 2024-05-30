import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window().
driver.maximize_window()

wait_time = 5

driver.get("https://www.amazon.in/")

time.sleep(wait_time)

print(driver.title)

driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Headset")

driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()

time.sleep(wait_time)

driver.find_element(By.XPATH, "//*[@id='p_89/JBL']/span/a").click()

time.sleep(wait_time)

driver.find_element(By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']").click()

time.sleep(wait_time)

windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])

message = driver.find_element(By.XPATH, "//span[@id='productTitle']").text

time.sleep(wait_time)

print(message)

# page = input("Product name \n")
# if page == message:
#     print(page)
#     driver.find_element(By.ID, "productTitle").click()
#     message2 = "Automated successfully"
#     print(message2)
# else:
#     message3 = "Fail"
#     print(message3)

driver.find_element(By.XPATH, "//td[@class='a-size-base']").click()

driver.find_element(By.XPATH, "//div[@id='cm_cr_dp_d_rating_histogram']").click()

time.sleep(wait_time)

message = "Automated succesfully"

print(message)

time.sleep(wait_time)
