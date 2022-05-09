import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
serv_obj = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
#driver.find_element(By.XPATH, "//input[@id='monday']").click()
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))
for i in range(len(checkboxes)):
    if i < 5:
        checkboxes[i].click()
time.sleep(5)
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
driver.quit()

