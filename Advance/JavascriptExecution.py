from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.handyWrappers import handyWrappers

class JavaScriptExecution():
    def testMethod(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument("user-data-dir=C:\\Users\\Arkus\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        # Instantiate the FF browser command
        driver = webdriver.Chrome(options=opt)
        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        #driver.get(baseUrl)
        driver.implicitly_wait(5)
        hw = handyWrappers(driver)
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")

        element =  driver.execute_script("return document.getElementById('name');")
        element.send_keys("Tester")


        #Idle and Close
        time.sleep(10)
        driver.quit()



pp = JavaScriptExecution()
pp.testMethod()