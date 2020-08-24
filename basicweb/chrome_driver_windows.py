from selenium import webdriver

class RunChromeTests():
    def testMethod(self):
        #Instantiate the FF browser command
        driver = webdriver.Chrome(executable_path="..//..//drivers//chromedriver.exe")
        #Open the provided URL
        driver.get("https://www.google.com")

ss = RunChromeTests()
ss.testMethod()