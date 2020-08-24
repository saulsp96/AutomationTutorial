from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.handyWrappers import handyWrappers


class UsingWrappers():
    def testMethod(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument("user-data-dir=C:\\Users\\Arkus\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        baseUrl = "https://letskodeit.teachable.com"
        # Instantiate the FF browser command
        driver = webdriver.Chrome(options=opt)
        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        #Handy Wrappers Object Creation
        hw = handyWrappers(driver)

        #Login ->
        time.sleep(2)
        LoginPresence = hw.isElementPresent("Login",By.LINK_TEXT)
        if LoginPresence:
            Loginlink = hw.getElement("Login","LINKTEXT")
            Loginlink.click()
            email = hw.getElement("user_email")
            password = hw.getElement("user_password")
            email.send_keys("test@email.com")
            password.send_keys("abcabc")
            loginbtn = hw.getElement("commit","name")
            loginbtn.click()
            #return True


        # Search for courses
        time.sleep(2)
        AllCourses = hw.getElement("All Courses","LINKTEXT")
        AllCourses.click()
        time.sleep(2)
        searchBox = hw.getElement("search-courses")



        # Select course
        _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        course_name = input("Please enter the name of the course: ")
        _course_locator = _course.format(str(course_name))
        searchBox.send_keys(course_name)
        course_box = hw.getElement(_course_locator,"xpath")
        course_box.click()

        # Browser Close
        time.sleep(10)
        #driver.quit()

ff = UsingWrappers()
ff.testMethod()