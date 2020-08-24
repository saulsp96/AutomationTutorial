from selenium import webdriver

class FindByXpathCss():
    def testMethod(self):
        baseUrl = "https://letskodeit.teachable.com/"
        #Instantiate the FF browser command
        driver = webdriver.Chrome()
        #Open the provided URL
        driver.get(baseUrl)
        elementByText = driver.find_element_by_link_text("Login")

        if elementByText is not None:
            print("We found an element by Link Text")

        elementBypartialText = driver.find_element_by_partial_link_text("Prac")

        if elementBypartialText is not None:
            print("We found an element by Partial text")



ff = FindByXpathCss()
ff.testMethod()