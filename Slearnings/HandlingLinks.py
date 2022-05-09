import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
serv_obj = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://demo.nopcommerce.com")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Digital downloads").click()
nooflinks = driver.find_elements(By.TAG_NAME, "a")
print(len(nooflinks))
for links in nooflinks:
    print(links.text)
driver.quit()
