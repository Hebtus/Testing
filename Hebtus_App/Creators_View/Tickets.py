# To give us access to the enter key, escape key...etc. ex: when I write something in the search bar and want to press enter:
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

sys.path.append(".")  # To access modules in sibling directories

from Common_Files.Utilities import *
from Common_Files.RealReferences_App import *

# # import Action chains
from selenium.webdriver.common.action_chains import ActionChains

def tickets(driver):
    touch = TouchAction(driver)
    # in add tickets swipe to date and time
    touch.press(x=228, y=565).move_to(x=235,y=105).release().perform()
    time.sleep(2)

    # outer swipe down to refresh
    touch.press(x=225, y=690).move_to(x=441,y=286).release().perform()
    time.sleep(2)

    

