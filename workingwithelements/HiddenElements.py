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
        #Find the state of the text box
        textBoxElement = driver.find_element_by_id("displayed-text")
        textBoxElementState = textBoxElement.is_displayed()
        print("Text is visible?: " + str(textBoxElementState))

        # Click the Hide button
        hidetextbox = driver.find_element_by_id("hide-textbox").click()
        # Find the state of the text box
        textBoxElementState = textBoxElement.is_displayed()
        print("Text is visible?: " + str(textBoxElementState))

        #Click the Show button
        showtextbox = driver.find_element_by_id("show-textbox").click()
        # Find the state of the text box
        textBoxElementState = textBoxElement.is_displayed()
        print("Text is visible?: " + str(textBoxElementState))



        # Browser Close
        time.sleep(5)
        driver.quit()

ff = HiddenElements()
ff.testMethod()