import time
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker")
driver.maximize_window()

driver.switch_to.frame(0)



year = "2026"
month = "July"
day = "23"
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

while True:
    mth = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mth == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]").click()

daydates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in daydates:
    if ele.text == day:
        ele.click()
        break

time.sleep(5)
driver.switch_to.default_content()

driver.quit()



