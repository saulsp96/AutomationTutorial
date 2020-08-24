from selenium import webdriver
import time


class RadiobuttonandCheckboxes():
    def testMethod(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        # Instantiate the FF browser command
        driver = webdriver.Chrome()
        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        bmwRadiobtn = driver.find_element_by_id("bmwradio")
        bmwRadiobtn.click()

        time.sleep(3)

        benzRadiobtn = driver.find_element_by_id("benzradio")
        benzRadiobtn.click()

        time.sleep(5)

        bmwCheckbox = driver.find_element_by_id("bmwcheck")
        bmwCheckbox.click()

        time.sleep(3)

        benzCheckbox = driver.find_element_by_id("benzcheck")
        benzCheckbox.click()
        time.sleep(3)

        driver.quit()


ff = RadiobuttonandCheckboxes()
ff.testMethod()