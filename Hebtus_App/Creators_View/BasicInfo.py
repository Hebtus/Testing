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

# App:
# ayausamakhalifa@gmail.com
# 123456789

F = open("./Test_Cases/EventTitleTestCases.txt", "r")
EventTitles = [EventTitle.rstrip("\n") for EventTitle in F.readlines()]
F.close()

F = open("./Test_Cases/TagsTestCases.txt", "r")
Tags = [Tag.rstrip("\n") for Tag in F.readlines()]
F.close()

def basic_info(driver):
    # Go to basic info page
    CreateEvent = find_my_element(driver,"XPATH",CREATE_EVENT_BUTTON)
    CreateEvent.click()
    time.sleep(3)

    # ---------------------------------------------- Empty Fields Test ---------------------------------------------- #
    SaveButton = find_my_element(driver, "XPATH", SAVE_BUTTON)
    check_not_found(driver, SaveButton, "Save Button not found")
    SaveButton.click()
    time.sleep(3)

    # ---------------------------------------------- Testing Event Title Field ---------------------------------------------- #

    # Test 1: Empty string 
    try:
        EventNameErrorMsg = driver.find_element(By.XPATH,EVENT_NAME_ERROR_MSG)
    except:
        print("Error: Event name Error message not displayed when event name field is empty")
    time.sleep(2)

    # Test 2: Error message goes away when we input a text and save
    EventName = find_my_element(driver, "XPATH", EVENT_NAME_FIELD)
    check_not_found(driver, EventName, "Event name not found")
    EventName.click()
    time.sleep(1)
    EventName = find_my_element(driver, "XPATH", EVENT_NAME_FIELD)
    check_not_found(driver, EventName, "Event name not found 2")
    EventName.send_keys(EventTitles[0])
    time.sleep(1)
    driver.hide_keyboard()
    SaveButton.click()
    time.sleep(3)
    #try:
    #    EventNameErrorMsg = driver.find_element(By.XPATH,EVENT_NAME_ERROR_MSG)
    #except:
    #    print("Success! Event name error message not found after entering an event name")
    #time.sleep(2)

    # Test 3: Entering more than 75 characters
    #EventName = find_my_element(driver, "XPATH", EVENT_NAME_FIELD)
    #check_not_found(driver, EventName, "Event name not found")
    #EventName.click()
    #time.sleep(1)
    #EventName = find_my_element(driver, "XPATH", EVENT_NAME_FIELD)
    #check_not_found(driver, EventName, "Event name not found 2")
    #EventName.set_text("")
    #time.sleep(1)
    #EventName.send_keys(EventTitles[1])
    #time.sleep(1)
    #driver.hide_keyboard()
    #EventNameRetrieved = EventName.get_attribute("text")
    #if len(str(EventNameRetrieved)) != 75:
    #    print(
    #            "Error: Case of 75 character as maximum limit for Event Title field not handled"
    #    )
    #time.sleep(2)

    # Finally enter valid Event name
    EventName = find_my_element(driver, "XPATH", EVENT_NAME_FIELD)
    check_not_found(driver, EventName, "Event name not found")
    EventName.click()
    time.sleep(1)
    EventName = find_my_element(driver, "XPATH", EVENT_NAME_FIELD)
    check_not_found(driver, EventName, "Event name not found 2")
    EventName.set_text("")
    time.sleep(1)
    EventName.send_keys(EventTitles[9])
    time.sleep(1)
    driver.hide_keyboard()
    SaveButton.click()


    # -------------------------------------------------- Testing Tags Field ------------------------------------------------- #
    # swipe from basic info to tags
    touch = TouchAction(driver)
    touch.press(x=241, y=640).move_to(x=258,y=250).release().perform()
    time.sleep(2)

    # ---------- Test 1: Entering more than 25 characters ---------- #

    #TagsField = find_my_element(driver,"XPATH",EVENT_TAGS_FIELD)
    #check_not_found(driver, TagsField, "Tags field not found")
    #TagsField.click()
    #time.sleep(1)
    #TagsField = find_my_element(driver, "XPATH", EVENT_TAGS_FIELD)
    #check_not_found(driver, TagsField, "Tags field not found 2")
    #TagsField.send_keys(Tags[0])
    #time.sleep(1)
    #driver.hide_keyboard()
    #TagsFieldRetrieved = TagsField.get_attribute("text")
#
    #if len(str(TagsFieldRetrieved)) != 25:
    #    print(
    #            "Error: Case of 25 character as maximum limit for Tags field not handled"
    #    )
    #time.sleep(2)
    #TagsField.click()
    #TagsField.set_text("")
#
    ## ---------- Test 2 : Entering a tag  ---------- #
    #    
    #TagsField.click()
    #time.sleep(1)
    #TagsField.send_keys(Tags[1])
    #time.sleep(1)
    #driver.hide_keyboard()
    #time.sleep(1)
    #TagsFieldRetrieved = TagsField.get_attribute("text")
    #if len(TagsFieldRetrieved) != 0:
    #    print("Error: Unable to add a tag. Therefore cannot perform further tests")
    #time.sleep(2)

    # ------------------------------------------------- Testing Location Field ------------------------------------------------ #
    
    # swipe from tags to location
    touch.press(x=254, y=565).move_to(x=261,y=150).release().perform()
    time.sleep(2)

    # -------------- Venue option ---------------- #

    # Test 1: Error message is displayed since venue is mandatory
    try:
        VenueErrorMsg = find_my_element(driver,"XPATH",EVENT_VENUE_ERROR_MSG)
    except:
        print("Error: Venue Error message not displayed when venue field is not filled")
    time.sleep(2)

    # Test 2: Error message goes away when we input a text and save
    VenueField = find_my_element(driver, "XPATH", EVENT_VENUE_FIELD)
    check_not_found(driver, VenueField, "Venue textbox not found")
    VenueField.click()
    time.sleep(1)
    VenueField.send_keys("38 Mahmoud Khalil Al Housarei")
    time.sleep(1)
    driver.hide_keyboard()
    SaveButton.click()
    time.sleep(3)
    #try:
    #    VenueErrorMsg = driver.find_element(By.XPATH,EVENT_VENUE_ERROR_MSG)
    #except:
    #    print("Success! Venue field error message not found after filling venue field")
    #time.sleep(2)

    # -------------- Online option ---------------- #
    #OnlineButton = find_my_element(driver,"XPATH",EVENT_ONLINE_BUTTON)
    #check_not_found(driver, OnlineButton, "Online button not found")
    #OnlineButton.click()
    #time.sleep(2)
    #if(OnlineButton.get_attribute("clickable") == False):
    #    print("Error: Online event option cannot be chosen")
    #time.sleep(2)
       
    # -------------- To be announced option ---------------- #
    #ToBeAnnouncedButton = find_my_element(driver,"XPATH",EVENT_TO_BE_ANNOUNCED)
    #check_not_found(driver, ToBeAnnouncedButton, "To Be Announced button not found")
    #ToBeAnnouncedButton.click()
    #if(ToBeAnnouncedButton.get_attribute("clickable") == False):
    #    print("Error: To Be Announced event option cannot be chosen")
    #time.sleep(2)

    # ----------------------------------------- Testing Date and time Section -------------------------------- #
        
    # swipe from location to date and time part 1
    touch.press(x=462, y=500).move_to(x=462,y=147).release().perform()
    time.sleep(2)

    # Test 1: Error message is displayed start date is mandatory
    try:
        StartDateErrorMsg = find_my_element(driver,"XPATH",EVENT_START_DATE_ERROR_MSG)
    except:
        print("Error: Start event Error message not displayed when start time is not filled")
    time.sleep(2)

    # --------------- Single event --------------- #
    # swipe from date and time title to event starts and ends
    touch.press(x=462, y=490).move_to(x=462,y=147).release().perform()
    time.sleep(2)
    # Test 1: Normal two dates
    StartDate = find_my_element(driver, "XPATH", EVENT_START_DATE_FIELD)
    check_not_found(driver, StartDate, "Start date not found")
    StartDate.click()
    time.sleep(1)
    StartDate = find_my_element(driver, "XPATH", EVENT_START_DATE_FIELD)
    check_not_found(driver, StartDate, "Start date not found 2")
    StartDate.send_keys("2023-06-10")
    time.sleep(2)
    driver.hide_keyboard()
    time.sleep(2)
    
    EndDate = find_my_element(driver, "XPATH", EVENT_END_DATE_FIELD)
    check_not_found(driver, EndDate, "End date not found")
    EndDate.click()
    time.sleep(1)
    EndDate = find_my_element(driver, "XPATH", EVENT_END_DATE_FIELD)
    check_not_found(driver, EndDate, "End date not found 2")
    EndDate.send_keys("2023-06-12")
    time.sleep(1)
    driver.hide_keyboard()
    time.sleep(2)
    SaveButton.click()

    # Test 2: Start date after end date
    #StartDate = find_my_element(driver, "XPATH", EVENT_START_DATE_FIELD)
    #check_not_found(driver, StartDate, "Start date not found")
    #StartDate.click()
    #StartDate.set_text("")
    #time.sleep(2)
    #StartDate.click()
    #time.sleep(1)
    #StartDate = find_my_element(driver, "XPATH", EVENT_START_DATE_FIELD)
    #check_not_found(driver, StartDate, "Start date not found 2")
    #StartDate.send_keys("2023-06-20")
    #time.sleep(1)
    #driver.hide_keyboard()
    #time.sleep(2)
    #SaveButton.click()
    #time.sleep(3)
    #try:
    #    StartDateErrorMsg = find_my_element(driver,"XPATH",EVENT_START_DATE_ERROR_MSG)
    #except:
    #    print("Error: There is no message that displays start date is after end date")
    #time.sleep(2)

    # swipe to description
    touch.press(x=462, y=715).move_to(x=462,y=153).release().perform()
    time.sleep(2)
    #Description = find_my_element(driver, "XPATH", EVENT_DESCRIPTION_FIELD)
    #check_not_found(driver, Description, "Description field not found")
    #Description.click()
    #time.sleep(1)
    #Description.send_keys("A very awesome event that you do not want to miss!")
    #time.sleep(1)
    #driver.hide_keyboard()
    #DescriptionRetrieved = Description.get_attribute("text")
    #if(len(str(DescriptionRetrieved)) == 0):
    #   print("Error: Unable to write in description field")


    # swipe reverse from description to 
    #touch.press(x=462, y=167).move_to(x=462,y=692).release().perform()
    #time.sleep(2)
    #touch.press(x=466,y=140).move_to(x=463, y=710).release().perform()
    #time.sleep(2)
    #touch.press(x=462, y=148).move_to(x=461,y=705).release().perform()
    #time.sleep(2)
