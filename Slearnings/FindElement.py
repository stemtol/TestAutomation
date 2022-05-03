from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://demo.nopcommerce.com")

elesearch = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(elesearch[4].text)
for ele in elesearch:
    print(ele.text)
driver.quit()
