import time
import requests as requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#serv_obj = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(r"C:\Users\stemt\Documents\SeleniumDrivers\chromedriver.exe")
#service=serv_obj
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

uname = driver.find_element(By.XPATH, "//input[@id='txtUsername']")
uname.click()
uname.send_keys("Admin")

upassword = driver.find_element(By.XPATH,"//input[@id='txtPassword']")
upassword.click()
upassword.send_keys("admin123")

driver.find_element(By.XPATH, "//input[@id='btnLogin']").click()

admin = driver.find_element(By.XPATH, "//b[normalize-space()='Admin']")
umgt = driver.find_element(By.XPATH, "//a[@id='menu_admin_UserManagement']")
users = driver.find_element(By.XPATH,"//a[@id='menu_admin_viewSystemUsers']")

act = ActionChains(driver)
act.move_to_element(admin).move_to_element(umgt).move_to_element(users).click().perform()
