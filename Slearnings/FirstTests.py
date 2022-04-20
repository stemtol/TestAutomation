from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

S = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=S)


driver.get("https://fantasy.premierleague.com/")
driver.maximize_window()

username = driver.find_element(By.ID, "loginUsername")
username.click()
username.send_keys("stemtol@gmail.com")
username.clear()
assert driver.title == "Fantasy Premier League, Official Fantasy Football Game of the Premier League"
no_of_links = driver.find_elements(By.TAG_NAME, 'a')
print(len(no_of_links))
driver.close()