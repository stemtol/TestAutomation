from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

text_says = driver.find_element(By.XPATH, "//a[normalize-space()='Mangalore Refine']/parent::td").text
text_says2 = driver.find_elements(By.XPATH, "//a[normalize-space()='Chennai Petro.']/ancestor::tr/descendant::*")

text_says1 = driver.find_elements(By.XPATH, "//a[normalize-space()='Chennai Petro.']/ancestor::tr/child::td")

print(text_says)
print(len(text_says2))
print(len(text_says1))
driver.quit()
