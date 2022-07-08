from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r'C:\Users\stemt\Documents\SeleniumDrivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("http://amazon.com")

def test_amazon():
    searchshoes = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    searchshoes.send_keys("shoes")

    driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
    pagetitle = driver.title
    if pagetitle == "Amazon.com : shoes":
        print(pagetitle)

    selectshoe = driver.find_element(By.XPATH, "//*[@id='search']/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div/div[1]/span/a/div/img[1]")
    selectshoe.click()
    shoepagetitle = driver.title
    if shoepagetitle == "Amazon.com: Amazon Essentials Women's Loafer Flat, Charcoal, 5 B US : Clothing, Shoes & Jewelry":
        print(shoepagetitle)

    driver.quit()