from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.handyWrappers import handyWrappers
from selenium.webdriver import ActionChains


class Slider():
    def testMethod(self):
        #opt = webdriver.ChromeOptions()
        #opt.add_argument("user-data-dir=C:\\Users\\Arkus\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        baseUrl = "https://jqueryui.com/slider/"
        # Instantiate the FF browser command
        driver = webdriver.Chrome()#options=opt)
        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        hw = handyWrappers(driver)

        driver.switch_to.frame(0)
        time.sleep(2)
        Slider = hw.getElement("//div[@id='slider']//span","xpath")


        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(Slider,100,0).perform()
            print("Sliding element successful")
            time.sleep(2)

            print("Item clicked")
        except:
            print("Sliding failed on element")

        # Idle and Close
        time.sleep(5)
        driver.quit()


pp = Slider()
pp.testMethod()