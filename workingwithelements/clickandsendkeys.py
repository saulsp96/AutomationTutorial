from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Browserinteraction():
    def testMethod(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument("user-data-dir=C:\\Users\\Arkus\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        baseUrl = "https://letskodeit.teachable.com/"
        # Instantiate the FF browser command
        driver = webdriver.Chrome(options=opt)
        #Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        login_link = driver.find_element(By.XPATH,"//div[@class='collapse navbar-collapse navbar-header-collapse']//a[contains(text(),'Login')]")
        login_link.click()

        username = driver.find_element(By.ID,"user_email")
        username.send_keys("test")

        user_password = driver.find_element(By.ID,"user_password")
        user_password.send_keys("test")

        time.sleep(10)

        username.clear()

        username.send_keys("testing")
        time.sleep(10)
        driver.quit()


ff = Browserinteraction()
ff.testMethod()