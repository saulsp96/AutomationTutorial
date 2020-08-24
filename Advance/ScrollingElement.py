from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.handyWrappers import handyWrappers

class WindowSize():
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

        #Scroll down
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        #Scroll up
        driver.execute_script("window.scrollBy(0,-1000)")
        time.sleep(5)
        #Scroll element into view
        element = hw.getElement("mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);",element)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-350);")
        time.sleep(3)
        #Native way to scroll element into view
        driver.execute_script("window.scrollBy(0,-1000);")
        location = element.location_once_scrolled_into_view
        print("Location:" + str(location))

        #Idle and Close
        time.sleep(5)
        driver.quit()



pp = WindowSize()
pp.testMethod()