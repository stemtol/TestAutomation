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

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
time.sleep(5)

alertwindow = driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("anything i want to type")
alertwindow.accept()