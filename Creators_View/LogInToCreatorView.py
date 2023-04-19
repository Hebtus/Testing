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

    creatorView = find_my_element(driver, "XPATH", MANAGE_MY_EVENTS)
    creatorView.click()
    time.sleep(3)
