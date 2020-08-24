from selenium import webdriver
import time

class FindByXpathCss():
    def testMethod(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        #Instantiate the FF browser command
        driver = webdriver.Chrome()
        #Open the provided URL
        driver.get(baseUrl)
        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Test tool")

        if elementByClassName is not None:
            print("We found an element by Class name")

        elementByTagName = driver.find_element_by_tag_name("a")
        

        if elementByTagName is not None:
            print("We found an element by Tag Name")




ff = FindByXpathCss()
ff.testMethod()