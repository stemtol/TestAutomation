from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

exp_obj = Service('C:\Drivers\chromedriver.exe')
exp_driver = webdriver.Chrome(service=exp_obj)
exp_driver.get("https://expedia.com")
exp_driver.maximize_window()
exp_driver.find_element(By.LINK_TEXT, "Flights").click()
exp_driver.find_element(By.XPATH, "//span[normalize-space()='Multi-city']").click()
exp_driver.find_element(By.XPATH, "//span[normalize-space()='Roundtrip']").click()
leg1 = exp_driver.find_element(By.XPATH, "//input[@id='location-field-leg1-origin']")
print(leg1.is_enabled())
leg1.click()
leg1.send_keys("newyork")


exp_driver.quit()
