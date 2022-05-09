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

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
alllinks = driver.find_elements(By.XPATH, "//a")
count = 0
count1 = 0

for links in alllinks:
    url = links.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url, " is broken")
        count += 1
    else:
        print(url, "isnt broken")
        count1 += 1
print("total number of broken link is", count)
print("total number of broken link is", count1)



driver.quit()
