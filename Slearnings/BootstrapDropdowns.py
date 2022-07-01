import time
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service(r"C:\Users\stemt\Documents\SeleniumDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
countrylist = driver.find_elements(By.XPATH, "//*[@id='select2-billing_country-results']/li")

print(len(countrylist))

for country in countrylist:
    if country.text == "Nigeria":
        country.click()
        break


driver.close()