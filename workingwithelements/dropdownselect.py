from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class Dropdownselect():
    def testMethod(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        # Instantiate the FF browser command
        driver = webdriver.Chrome()
        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        element = driver.find_element_by_id("carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Select benz by value")
        time.sleep(2)
        sel.select_by_index("2")
        print("Select honda by index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select bmw by visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select honda by index")


        time.sleep(5)
        driver.quit()


pp = Dropdownselect()
pp.testMethod()