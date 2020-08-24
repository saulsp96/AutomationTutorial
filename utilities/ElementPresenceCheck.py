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
        #Handy Wrappers Object Creation
        hw = handyWrappers(driver)

        elementresult = hw.isElementPresent("name",By.ID)
        print(str(elementresult))

        elementresult2 = hw.elementPresenceCheck("//input[@id='name']",By.XPATH)
        print(str(elementresult2))


        # Browser Close
        time.sleep(5)
        driver.quit()

ff = UsingWrappers()
ff.testMethod()