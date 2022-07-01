import time
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

serv_obj = Service(r"C:\Users\stemt\Documents\SeleniumDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


driver.get("https://www.nopcommerce.com/en")
driver.switch_to.new_window('tab') #or windows in the place of tab to open address in a new window
driver.get("https://facebook.com")
driver.maximize_window()

driver.close()