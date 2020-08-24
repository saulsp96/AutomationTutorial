from selenium import webdriver
import time


class ElementState():
    def testMethod(self):
        baseUrl = "https://www.google.com"
        # Instantiate the FF browser command
        driver = webdriver.Chrome()
        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        """e1 = driver.find_element_by_id("gs_htif0")
        e1State =  e1.is_enabled()
        print(e1State)

        e2 = driver.find_element_by_id("gs_taif0")
        e2State = e2.is_enabled()
        print(e2State)"""

        e3 = driver.find_element_by_name("q")
        e3State = e3.is_enabled()
        print(e3State)
        e3.send_keys("letskodeit")
        
        time.sleep(5)


        driver.quit()


ff = ElementState()
ff.testMethod()