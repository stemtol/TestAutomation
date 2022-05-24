import time
import requests as requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://jumia.com.ng/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[normalize-space()='Supermarket']")

slider_min = driver.find_element(By.NAME, "x")
slider_max = driver.find_element(By.NAME, "y")

print(slider_max.location)
print(slider_min.location)

act = ActionChains(driver)

act.drag_and_drop_by_offset(slider_min,59,0)
act.drag_and_drop_by_offset(slider_max,-45,0)
