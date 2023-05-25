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

def publish(driver):
    touch = TouchAction(driver)
    # swipe down
    touch.press(x=470, y=779).move_to(x=465,y=301).release().perform()
    time.sleep(2)

    touch.press(x=464, y=747).move_to(x=460,y=224).release().perform()
    time.sleep(2)

    # Press publish
    Btn = find_my_element(driver,"XPATH",PUBLISH_THE_EVENT)
    Btn.click()
    # Check for alert box
    Published = find_my_element(driver,"XPATH",EVENT_PUBLISHED) 
    if(Published == None):
        print("Error! Failed to publish event (Alert box not shown)")


    # Check that make event public/private are enabled
    Btn = find_my_element(driver,"XPATH",MAKE_EVENT_PRIVATE)
    if(Btn.get_attribute("clickable") == False):
        print("Error: Private event option cannot be chosen")
    time.sleep(2)

    Btn = find_my_element(driver,"XPATH",MAKE_EVENT_PUBLIC)
    if(Btn.get_attribute("clickable") == False):
        print("Error: Public event option cannot be chosen")
    time.sleep(2)
    Btn.click()
    time.sleep(2)

    # swipe back up
    touch.press(x=473, y=136).move_to(x=463,y=776).release().perform()
    time.sleep(2)