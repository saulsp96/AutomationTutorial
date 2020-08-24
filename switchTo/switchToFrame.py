from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.handyWrappers import handyWrappers


class SwitchToFrame():
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
        driver.execute_script("window.scrollBy(0,1800);")

        #Switch to frame using Id
        #driver.switch_to.frame("courses-iframe")
        #time.sleep(3)
        #Switch to frame using name
        #driver.switch_to.frame("iframe-name")
        #time.sleep(3)
        #Switch to frame using numbers
        driver.switch_to.frame(0)
        time.sleep(3)
        #Search courses
        searchBox = hw.getElement("search-courses")
        searchBox.send_keys("python")
        time.sleep(2)
        #Switch back to parent handle
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-1800);")
        element = hw.getElement("name")
        element.send_keys("Tester")
        # Idle and Close
        time.sleep(5)
        driver.quit()


pp = SwitchToFrame()
pp.testMethod()