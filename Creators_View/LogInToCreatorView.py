from selenium.webdriver.common.by import By
import time
import sys
sys.path.append(".") # Adds higher directory to python modules path
from Common_Files.Utilities import find_my_element
from Common_Files.RealReferences import *

def creator_view(driver):

    # Start at log-in page:
    driver.get("https://hebtus.me/")
    time.sleep(4)

    # Navigate to creator's view from landing page
    NavBarDropDown = find_my_element(driver,"ID",NAV_BAR_DROP_DOWN)
    NavBarDropDown.click()

    LogIn = find_my_element(driver, "XPATH", DROPDOWN_LOGIN_CHOICE)
    LogIn.click()
    time.sleep(3)

    Email = find_my_element(driver,"ID",EMAIL_FIELD)
    Email.send_keys("Marwan62x@gmail.com")

    Password = find_my_element(driver,"ID",PASSWORD_FIELD)
    Password.send_keys("marwan123")

    time.sleep(1)

    LogInBtn = find_my_element(driver,"ID",LOG_IN_BUTTON)
    LogInBtn.click()

    time.sleep(3)

    ManageEvents = find_my_element(driver,"XPATH",MANAGE_MY_EVENTS)
    ManageEvents.click()



