from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.handyWrappers import handyWrappers

class Screenshot():
    def testMethod(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument("user-data-dir=C:\\Users\\Arkus\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        baseUrl = "https://letskodeit.teachable.com/"
        # Instantiate the FF browser command
        driver = webdriver.Chrome(options=opt)
        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        hw = handyWrappers(driver)
        #Login
        login_link = hw.getElement("//div[@class='collapse navbar-collapse navbar-header-collapse']//a[contains(text(),'Login')]","XPATH")
        login_link.click()
        username = hw.getElement("user_email")
        username.send_keys("abc@email.com")
        user_password = hw.getElement("user_password")
        user_password.send_keys("abc")
        Loginbtn = hw.getElement("commit","name")
        Loginbtn.click()
        destinationFilename = "C:\\Users\\Arkus\\Documents\\workspace_python\\AutomationTutorial\\test.png"
        try:
            driver.save_screenshot(destinationFilename)
            print("Screenshot saved: " + destinationFilename)

        except NotADirectoryError:
            print("Directory issue")

pp = Screenshot()
pp.testMethod()