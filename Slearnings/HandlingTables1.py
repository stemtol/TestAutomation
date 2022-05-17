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

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text


noofrow =len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))

noofcol = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//th"))

for col in range(1,noofcol+1):
    for row in range (2, noofrow+1):
        rc = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td["+str(col)+"]").text
        print(rc)
    print()

for row in range (2, noofrow+1):
    authorname = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[2]").text
    if authorname == "Amit":
        bookname = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[1]").text
        print(authorname,"is the author and ",bookname, " is the book")
#print(noofcol, noofrow)
#print(data)