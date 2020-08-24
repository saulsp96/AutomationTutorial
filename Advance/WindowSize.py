from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.handyWrappers import handyWrappers

class WindowSize():
    def testMethod(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument("user-data-dir=C:\\Users\\Arkus\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        # Instantiate the FF browser command
        driver = webdriver.Chrome(options=opt)
        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        hw = handyWrappers(driver)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")

        print("Height: " + str(height))
        print("Width: " + str(width))

        #Idle and Close
        time.sleep(5)
        driver.quit()



pp = WindowSize()
pp.testMethod()