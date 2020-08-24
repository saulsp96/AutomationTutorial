from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.handyWrappers import handyWrappers


class CalendarSelection():
    def testMethod(self):
        baseUrl = "https://www.expedia.mx/"
        # Instantiate the FF browser command
        driver = webdriver.Chrome()
        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        hw = handyWrappers(driver)

        flightsTab = hw.getElement("//div[contains(@class,'StorefrontWizardRegionBEX')]//li[2]//a[1]","xpath")
        flightsTab.click()

        datePicker1 = hw.getElement("//button[@id='d1-btn']","xpath")
        datePicker1.click()

        departureDate = hw.getElement("//tr[5]//td[6]//button[1]","xpath")
        departureDate.click()

        Listobtn = hw.getElement("//span[contains(text(),'Listo')]","xpath")
        Listobtn.click()


        # Browser Close
        time.sleep(5)
        driver.quit()
    def testMethod2(self):
        baseUrl = "https://www.expedia.mx/"
        # Instantiate the FF browser command
        driver = webdriver.Chrome()
        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        hw = handyWrappers(driver)

        flightsTab = hw.getElement("//div[contains(@class,'StorefrontWizardRegionBEX')]//li[2]//a[1]", "xpath")
        flightsTab.click()

        departureBox = hw.getElement("//div[@id='location-field-leg1-origin-menu']//button[@class='uitk-faux-input']","xpath")
        departureBox.send_keys("Tijuana")

        DepartureList = driver.find_element_by_xpath("//ul[@class='uitk-typeahead-results no-bullet']")
        Departures = DepartureList.find_elements(By.TAG_NAME,"strong")
        for dest in Departures:
            print(dest.text)
            if dest.text == "Tijuana (TIJ - A. Internacional General Abelardo L. Rodríguez)":
                dest.click()
                break
        destinationBox = hw.getElement("//div[@id='location-field-leg1-destination-menu']//button[@class='uitk-faux-input']","xpath")
        destinationBox.send_keys("Japon")

        DepartureList = driver.find_element_by_xpath("//div[@class='uitk-menu-container elevation-8 uitk-menu-open uitk-menu-pos-left']")
        Departures = DepartureList.find_elements(By.TAG_NAME, "strong")
        for dest in Departures:
            if dest.text == "Tokio (NRT - A. Internacional de Narita)":
                dest.click()
                break

        datePicker1 = hw.getElement("//button[@id='d1-btn']", "xpath")
        datePicker1.click()
        calMonth = driver.find_element_by_xpath("//div[@class='uitk-new-date-picker-desktop-months-container']//div[1]")
        allValidDates = calMonth.find_elements(By.CLASS_NAME,"uitk-new-date-picker-day")
        for date in allValidDates:
            #print(date.get_attribute("data-day"))
            if date.get_attribute("data-day") == "30":
                date.click()
                break
        Listobtn = hw.getElement("//span[contains(text(),'Listo')]", "xpath")
        Listobtn.click()

        Buscarbtn = hw.getElement("//button[@class='uitk-button uitk-button-large uitk-button-fullWidth uitk-button-has-text uitk-button-primary']","xpath")
        Buscarbtn.click()

        _currentUrl = driver.current_url
        print(str(_currentUrl))
        # Browser Close
        time.sleep(5)
        driver.quit()

ff = CalendarSelection()
ff.testMethod2()