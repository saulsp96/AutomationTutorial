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


        nameTB = hw.getElement("name")
        nameTB.send_keys("Saul")
        alertBtn = hw.getElement("alertbtn")
        alertBtn.click()
        time.sleep(2)
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(2)
        confirmBtn = hw.getElement("confirmbtn")
        nameTB.send_keys("Saul")
        confirmBtn.click()
        time.sleep(2)
        alert2 = driver.switch_to.alert
        alert2.dismiss()
        # Idle and Close
        time.sleep(5)
        driver.quit()


pp = SwitchToFrame()
pp.testMethod()