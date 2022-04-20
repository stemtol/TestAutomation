from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://demo.nopcommerce.com")

driver.maximize_window()
ibox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print(ibox.is_displayed())
print(ibox.is_enabled())

print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
genderf_radio = driver.find_element(By.XPATH, "//input[@id='gender-female']")
print(genderf_radio.is_selected())
#print(driver.page_source)

driver.quit()