from selenium import webdriver
import time


class Browserinteraction():
    def testMethod(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        # Instantiate the FF browser command
        driver = webdriver.Chrome()
        # Open the provided URL
        driver.get(baseUrl)
        #Window maximize
        driver.maximize_window()
        #Get title
        title = driver.title
        print("Title of the webpage is"+title)
        #get current url
        currentUrl = driver.current_url
        print("Current Url of the web page is:" + currentUrl)
        #Browser Refresh
        driver.refresh()
        print("Browser refreshed 1st time")
        driver.get(currentUrl)
        print("Browser refreshed 2nd time")
        #open another url
        driver.get("https://www.google.com")
        #Browser back
        driver.back()
        print("Go one step back in browser")
        # Browser forward
        driver.forward()
        print("Go one step forward in browser")
        # Get page source
        pageSource = driver.page_source
        # Browser Close / Quit
        #driver.close()
        driver.quit()


ff = Browserinteraction()
ff.testMethod()