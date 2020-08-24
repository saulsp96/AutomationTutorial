from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class FindByXpathCss():
    def testMethod(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        # Instantiate the FF browser command
        driver = webdriver.Chrome()
        # Open the provided URL
        driver.get(baseUrl)
        elementByClassName = driver.find_element(By.CLASS_NAME,"displayed-class")
        elementByClassName.send_keys("Test tool")

        if elementByClassName is not None:
            print("We found an element By Class name")

        elementByTagName = driver.find_element(By.TAG_NAME,"a")

        if elementByTagName is not None:
            print("We found an element By Tag Name")


ff = FindByXpathCss()
ff.testMethod()