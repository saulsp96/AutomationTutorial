from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.handyWrappers import handyWrappers


class UsingWrappers():
    def testMethod(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        # Instantiate the FF browser command
        driver = webdriver.Chrome()
        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        hw = handyWrappers(driver)

        textField = hw.getElement("name")
        textField.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']","xpath")
        textField2.clear()
        # Browser Close
        time.sleep(5)
        driver.quit()

ff = UsingWrappers()
ff.testMethod()