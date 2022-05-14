import time

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
# driver.implicitly_wait(10)
exwait = WebDriverWait(driver, 2, poll_frequency=2, ignored_exceptions=[exceptions])

driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()
windowIDs = driver.window_handles

parentwindow = windowIDs[0]
childwindow = windowIDs[1]

driver.switch_to.window(childwindow)
check = driver.find_element(By.XPATH, "//input[@id='linkadd']")
print(check.is_displayed())

for wind in windowIDs:
    print(wind)
driver.quit()