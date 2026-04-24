from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome browser using Selenium WebDriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# Print page title and current URL for verification
print(driver.title)
print(driver.current_url)

# RADIO BUTTON SECTION -Locate all radio buttons using CSS selector
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")

# Click the third radio button (index starts from 0)
radiobuttons[0].click()
assert radiobuttons[0].is_selected()

# AUTO-SUGGESTION DROPDOWN
driver.find_element(By.ID, 'autocomplete').send_keys('ind')
time.sleep(5)

# Locate all dropdown suggestion elements
countries = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item-wrapper")

# Print number of suggestions found
print(len(countries))

# Loop through suggestions and select 'India'
for country in countries:
    if country.text == 'India':
        country.click()
        break

driver.find_element(By.XPATH, "//option[@value='option2']").click()

# CHECKBOX SECTION
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

# Loop through checkboxes to find the one with value 'option2'
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option3":
        checkbox.click()

        # Verify the checkbox is selected
        assert checkbox.is_selected()
        break
time.sleep(7)

driver.find_element(By.ID, "openwindow").click()

parent_window = driver.current_window_handle

all_windows = driver.window_handles

for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        break
driver.maximize_window()
time.sleep(5)

time.sleep(5)

elements = driver.find_elements(By.XPATH, "//input[@type='text']")

if elements:
    ele = elements[0]
    ele.send_keys("Playwright with AI")
    driver.execute_script("arguments[0].scrollIntoView();", ele)
else:
    print("No input box found in new window")

time.sleep(5)


