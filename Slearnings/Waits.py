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

driver.get("http://google.com")
driver.maximize_window()
gsearch = driver.find_element(By.XPATH, "//input[@title='Search']")
gsearch.send_keys("selenium")
gsearch.submit()
driver.find_element(By.XPATH, "//a[@aria-label='Page 3']").click()
driver.find_element(By.XPATH, "//a[@aria-label='Page 1']").click()

searchlink = exwait.until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Selenium - Uses, Side Effects, and More - WebMD']")))
searchlink.click
driver.quit()
