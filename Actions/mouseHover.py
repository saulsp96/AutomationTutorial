from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.handyWrappers import handyWrappers
from selenium.webdriver import ActionChains


class mouseHover():
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

        driver.execute_script("window.scrollBy(0,600);")
        time.sleep(2)
        mouseHoverbtn = hw.getElement("mousehover")
        Topbtn = hw.getElement(".//div[@class='mouse-hover-content']//a[text()='Top']","xpath")
        Refreshbtn = hw.getElement(".//div[@class='mouse-hover-content']//a[text()='Reload']","xpath")

        try:
            actions = ActionChains(driver)
            actions.move_to_element(mouseHoverbtn).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            actions.move_to_element(Topbtn).click().perform()
            print("Item clicked")
        except:
            print("Mouse Hover failed on element")

        # Idle and Close
        time.sleep(5)
        driver.quit()


pp = mouseHover()
pp.testMethod()