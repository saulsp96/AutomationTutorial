from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.handyWrappers import handyWrappers

class SwitchToWindow():
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

        #Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent handle: " + parentHandle)
        #Find open window and click it
        element = hw.getElement("openwindow")
        element.click()
        time.sleep(2)
        #Find all handles, there should be two handles after clicking open window button
        allHandles = driver.window_handles
        for handle in allHandles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                # Switch to window and search course
                driver.switch_to.window(handle)
                print("Switched to window: " + handle)
                searchBox = hw.getElement("search-courses")
                searchBox.send_keys("python")
                time.sleep(3)
                driver.close()
                break



        #Switch back to the parent handle
        driver.switch_to.window(parentHandle)
        element2 = hw.getElement("name")
        element2.send_keys("Loop")

        #Idle and Close
        time.sleep(5)
        driver.quit()



pp = SwitchToWindow()
pp.testMethod()