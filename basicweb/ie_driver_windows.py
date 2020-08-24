from selenium import webdriver

class IEDriverWindows():
    def testMethod(self):
        driver = webdriver.Ie(executable_path="..//..//drivers//iedriver.exe")
        driver.get("https://google.com")

ie = IEDriverWindows()
ie.testMethod()