from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class FindElements():
    def testMethod(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        # Instantiate the FF browser command
        driver = webdriver.Chrome()
        # Open the provided URL
        driver.get(baseUrl)
        elementsByClassName = driver.find_elements(By.CLASS_NAME,"inputs")
        lenght = len(elementsByClassName)
        if elementsByClassName is not None:
            print("We found an element By Class name "+ str(lenght))

        elementsByTagName = driver.find_elements(By.TAG_NAME,"a")
        lenght2 = len(elementsByTagName)
        if elementsByTagName is not None:
            print("We found an element By Tag Name " + str(lenght2))


ff = FindElements()
ff.testMethod()