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

def dashboard(driver):
    touch = TouchAction(driver)
    # swipe down
    touch.press(x=427, y=672).move_to(x=424,y=232).release().perform()
    time.sleep(2)

    #click add attendee
    Btn = find_my_element(driver,"XPATH",ADD_ATTENDEE)
    Btn.click()
    time.sleep(2)

    # swipe down
    touch.press(x=459, y=699).move_to(x=442,y=223).release().perform()
    time.sleep(2)

    Field = find_my_element(driver,"XPATH",ATTENDEE_FIRST_NAME)
    Field.click()
    time.sleep(1)
    Field.send_keys("Malak")
    time.sleep(1)
    driver.hide_keyboard()

    Field = find_my_element(driver,"XPATH",ATTENDEE_LAST_NAME)
    Field.click()
    time.sleep(1)
    Field.send_keys("Mokhtar")
    time.sleep(1)
    driver.hide_keyboard()

    Field = find_my_element(driver,"XPATH",ATTENDEE_PHONE_NUMBER)
    Field.click()
    time.sleep(1)
    Field.send_keys("01020970040")
    time.sleep(1)
    driver.hide_keyboard()

    Field = find_my_element(driver,"XPATH",ATTENDEE_GENDER)
    Field.click()
    time.sleep(1)
    Field.send_keys("Female")
    time.sleep(1)
    driver.hide_keyboard()
    
    Field = find_my_element(driver,"XPATH",ATTENDEE_EMAIL)
    Field.click()
    time.sleep(1)
    Field.send_keys("malak.mokhtar@gmail.com")
    time.sleep(1)
    driver.hide_keyboard()

    Field = find_my_element(driver,"XPATH",ATTENDEE_PRICE)
    Field.click()
    time.sleep(1)
    Field.send_keys("50")
    time.sleep(1)
    driver.hide_keyboard()

    # swipe again
    touch.press(x=471, y=727).move_to(x=461,y=153).release().perform()
    time.sleep(2)

    Field = find_my_element(driver,"XPATH",ATTENDEE_QUANTITY)
    Field.click()
    time.sleep(1)
    Field.send_keys("3")
    time.sleep(1)
    driver.hide_keyboard()

    # add button
    Btn = find_my_element(driver,"XPATH",ADD_ATTENDEE_END_BTN)
    Btn.click()
    time.sleep(2)

    # refresh
    Btn = find_my_element(driver,"XPATH",DASHBOARD_REFRESH)
    Btn.click()
    time.sleep(2)

    #swipe up
    touch.press(x=376, y=280).move_to(x=367,y=756).release().perform()
    time.sleep(4)

    # horizontal swipe
    touch.press(x=461, y=516).move_to(x=50,y=512).release().perform()
    time.sleep(2)

    # tickets sold 0 error
    Row = find_my_element(driver,"XPATH",TICKET_ADDED_TABLE)
    if(Row != None):
        print("Added row for ticket in Dashboard for attendee")
    Text = find_my_element(driver,"XPATH",TICKETS_SOLD).get_attribute('content-desc')
    if(Text == '0'):
        print("Error! Sold tickets are 0 after adding attendee")

    time.sleep(2)
    