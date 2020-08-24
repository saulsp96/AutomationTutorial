from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.handyWrappers import handyWrappers
from selenium.webdriver import ActionChains


class DragDrop():
    def testMethod(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument("user-data-dir=C:\\Users\\Arkus\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        baseUrl = "https://jqueryui.com/droppable/"
        # Instantiate the FF browser command
        driver = webdriver.Chrome(options=opt)
        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        hw = handyWrappers(driver)

        driver.switch_to.frame(0)
        time.sleep(2)
        fromElement = hw.getElement("draggable")
        toElement = hw.getElement("droppable")
        time.sleep(2)

        try:
            actions = ActionChains(driver)
            #actions.drag_and_drop(fromElement,toElement).perform()
            actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print("Drag and Drop element successful")
            time.sleep(2)

            print("Item clicked")
        except:
            print("Mouse Hover failed on element")

        # Idle and Close
        time.sleep(5)
        driver.quit()


pp = DragDrop()
pp.testMethod()