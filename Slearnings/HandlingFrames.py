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

driver.get("https://selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()

driver.switch_to.default_content()
