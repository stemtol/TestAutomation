import time
import requests as requests
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(20)

driver.get("https://text-compare.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[@id='ez-video-ez-stuck-close']").click()

driver.find_element(By.XPATH,"//textarea[@id='inputText1']").click()
driver.find_element(By.XPATH,"//textarea[@id='inputText1']").send_keys("clean this up")
act = ActionChains(driver)
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

