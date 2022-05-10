import time
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)


driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()
country_ele = driver.find_element(By.XPATH, "//select[@id='input-country']")

country = Select(country_ele)
alloptions = country.options
country.select_by_visible_text("Nigeria")
#or
#for options in alloptions:
 #   if options == "Brazil":
  #      options.click
  #      break

print(len(alloptions))

for options in alloptions:
    print(options.text)