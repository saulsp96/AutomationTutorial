from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ElementsList():
    def testMethod(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        # Instantiate the FF browser command
        driver = webdriver.Chrome()
        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        radioButtonslist = driver.find_elements(By.XPATH,"//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radioButtonslist)
        print("Size of the list: " + str(size))

        for radioButton in radioButtonslist:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
        time.sleep(5)
        driver.quit()


pp = ElementsList()
pp.testMethod()