from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from appium.webdriver.common.mobileby import MobileBy


def find_my_element(Driver, type, val):
    try:
        if type == "ID":
            item = WebDriverWait(Driver, 20).until(
                EC.element_to_be_clickable((AppiumBy.ID, val))
            )
        elif type == "XPATH":
            item = WebDriverWait(Driver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, val))
            )
        elif type == "LINK_TEXT":
            item = WebDriverWait(Driver, 20).until(
                EC.presence_of_element_located((AppiumBy.LINK_TEXT, val))
            )
        elif type == "CLASS":
            item = WebDriverWait(Driver, 20).until(
                EC.presence_of_element_located((AppiumBy.CLASS_NAME, val))
            )
        elif type == "AID":
            item = WebDriverWait(Driver, 20).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, val))
            )
        else:
            return None
    except:
        # print("Element not found.")
        return None
    return item

def check_not_found(driver, element, message):
    if element == None:
        # print(message)
        assert element != None, message
        # driver.close()
        # exit()

def find_my_elements(Driver, type, val):
    try:
        if type == "XPATH":
            items = WebDriverWait(Driver, 30).until(
                EC.presence_of_all_elements_located((AppiumBy.XPATH, val))
            )
        elif type == "LINK_TEXT":
            items = WebDriverWait(Driver, 20).until(
                EC.presence_of_all_elements_located((AppiumBy.LINK_TEXT, val))
            )
        elif type == "CLASS":
            items = WebDriverWait(Driver, 20).until(
                EC.presence_of_all_elements_located((AppiumBy.CLASS_NAME, val))
            )
        elif type == "AID":
            items = WebDriverWait(Driver, 20).until(
                EC.presence_of_all_elements_located((AppiumBy.ACCESSIBILITY_ID, val))
            )
        else:
            return None
    except:
        # print("Elements not found.")
        return None
    return items