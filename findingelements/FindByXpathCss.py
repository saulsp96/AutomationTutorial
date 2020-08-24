from selenium import webdriver

class FindByXpathCss():
    def testMethod(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        #Instantiate the FF browser command
        driver = webdriver.Firefox()
        #Open the provided URL
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")

        if elementByXpath is not None:
            print("We found an element by Xpath")

        elementByCss = driver.find_element_by_css_selector("#displayed-text")

        if elementByCss is not None:
            print("We found an element by CSS selector")



ff = FindByXpathCss()
ff.testMethod()