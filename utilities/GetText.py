from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetText():
    def testMethod(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        # Instantiate the FF browser command
        driver = webdriver.Chrome()
        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        #Implicit wait
        driver.implicitly_wait(5)

        openTabElement = driver.find_element_by_id("opentab")
        opentabText = openTabElement.text
        print("Text on the element is: " + opentabText)




        # Browser Close
        time.sleep(5)
        driver.quit()

ff = GetText()
ff.testMethod()