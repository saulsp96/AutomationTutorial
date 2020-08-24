from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class HiddenElements():
    def testMethod(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        # Instantiate the FF browser command
        driver = webdriver.Chrome()
        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("type")

        print("The attribute of the element is: " + str(result) )
        # Browser Close
        time.sleep(5)
        driver.quit()

ff = HiddenElements()
ff.testMethod()