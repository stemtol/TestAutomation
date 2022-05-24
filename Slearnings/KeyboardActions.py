import time
import requests as requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('C:\Drivers\chromedriver.exe')
driver.implicitly_wait(15)

driver.get("https://text-compare.com/")
driver.maximize_window()


driver.find_element(By.XPATH,"//textarea[@id='inputText1']").click()
driver.find_element(By.XPATH,"//textarea[@id='inputText1']").send_keys("clean this up")
act = ActionChains(driver)
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

