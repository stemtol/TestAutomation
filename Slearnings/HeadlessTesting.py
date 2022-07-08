from selenium import webdriver


def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service(r"C:\Users\stemt\Documents\SeleniumDrivers\chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver


def test_headless():
    driver = headless_chrome()
    driver.get("https://www.nopcommerce.com/en")
    if driver.title == "Free and open-source eCommerce platform. ASP.NET Core based shopping cart. - nopCommerce":
        print(driver.title)
        driver.close()
