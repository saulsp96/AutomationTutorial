from selenium import webdriver

class RunFFTests():
    def testMethod(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        #Instantiate the FF browser command
        driver = webdriver.Firefox()
        #Open the provided URL
        driver.get(baseUrl)
    
ff = RunFFTests()
ff.testMethod()