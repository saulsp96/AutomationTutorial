from selenium.webdriver.common.by import By
import time

class handyWrappers():

    def __init__(self,driver):
        self.driver = driver

    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " is not correct or supported")
        return False

    def getElement(self,locator,locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            bytype = self.getByType(locatorType)
            element = self.driver.find_element(bytype,locator)
            elemento = element.text
            print("Element: " + elemento + " Found")
        except:
            print("Element not Found")
        return element
    def isElementPresent(self,locator,bytype):
        try:
            element = self.driver.find_element(bytype, locator)
            if element is not None:
                print("Element Found")
                return True
            else: return False
            print("Element Found")
        except:
            print("Element not Found")
        return False
    def elementPresenceCheck(self,locator,bytype):
        try:
            elementsList = self.driver.find_elements(bytype, locator)
            if len(elementsList) > 0:
                print("Element Found")
                return True
            else:
                return False
            print("Element Found")
        except:
            print("Element not Found")
        return False
    def takeScreenshot(self,driver):
        """
        Takes a screenshot of the current open web page
        :param driver:
        :return:
        """
        filename = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "C:\\Users\\Arkus\\Documents\\workspace_python\\AutomationTutorial\\screenshots\\"
        destinationFile = screenshotDirectory + filename
        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved: " + destinationFile)

        except NotADirectoryError:
            print("Directory issue")


