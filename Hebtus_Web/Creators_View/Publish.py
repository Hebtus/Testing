# To give us access to the enter key, escape key...etc. ex: when I write something in the search bar and want to press enter:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

import math

from selenium.webdriver.support.wait import WebDriverWait

import sys
sys.path.append(".") # To access modules in sibling directories
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

from Common_Files.Utilities import *
from Common_Files.RealReferences_Hebtus import *

def publish(driver, mode = 0):
    if mode == 0: # Normal operation
        pass
    else:
        def Navigation_Test(driver):
            PublishTitle = find_my_element(driver,"XPATH",PUBLISH_TITLE)
            if(PublishTitle == None):
                print("Failed to navigate correctly to publish page")
            time.sleep(2)

        def Validate_Event_Details(driver):
            EventTitle = find_my_element(driver,"XPATH",PUBLISH_EVENT_TITLE)
            if(MY_EVENT_NAME not in EventTitle.get_attribute("innerHTML")):
                print("Error! Event to be published does not match title chosen")

        def RadioButtons_Enabled(driver):
            if(find_my_element(driver,"ID",PUBLIC_RADIOBUTTON).is_enabled() == False):
                print("Error! Public Radio button is not enabled")
            if(find_my_element(driver,"ID",PRIVATE_RADIOBUTTON).is_enabled() == False):
                print("Error! Private Radio button is not enabled")
            if(find_my_element(driver,"ID",PUBLISH_NOW_RADIOBUTTON).is_enabled() == False):
                print("Error! Publish now Radio button is not enabled")
            if(find_my_element(driver,"ID",SCHEDULE_LATER_RADIOBUTTON).is_enabled() == False):
                print("Error! Public later button is not enabled")

        # function taken from attendee's view
        def GetEvents(driver):
            try:
                for i in range(1, math.ceil(96 / 12) + 1):
                    for j in range(1, 13):
                        time.sleep(1)
                        EVENT = EVENT_NAME_1 + str(j) + EVENT_NAME_2
                        Event = find_my_element(driver, "XPATH", EVENT)
                        if Event != None:
                            driver.execute_script("arguments[0].scrollIntoView();", Event)
                            time.sleep(2)
                            EventName = Event.text
                            if MY_EVENT_NAME in EventName:
                                return True
                            # break
                    # check if more pages
                    NextPageButton = find_my_element(driver, "ID", NEXT_PAGE_BUTTON)
                    check_not_found(driver, NextPageButton, "Next page button not found")
                    if NextPageButton.is_enabled():
                        driver.execute_script("arguments[0].click();", NextPageButton)
            except:
                return False
            

        def To_EventList(driver):
            # Navigate to event list to check if it was added
            # Account from navbar
            Element=find_my_element(driver,"XPATH",ACCOUNT_NAVBAR)
            driver.execute_script("arguments[0].scrollIntoView();",Element)
            time.sleep(2)
            Element.click()
            Element=find_my_element(driver,"XPATH",MANAGE_MY_EVENTS_PUBLISH)
            time.sleep(2)
            Element.click()
            time.sleep(3)
        
        def To_EventList2(driver):
            # Navigate to event list to check if it was added
            # Account from navbar
            Element=find_my_element(driver,"ID",ACCOUNT_NAVBAR2)
            driver.execute_script("arguments[0].scrollIntoView();",Element)
            time.sleep(2)
            Element.click()
            Element=find_my_element(driver,"XPATH",MANAGE_MY_EVENTS2)
            time.sleep(2)
            Element.click()
            time.sleep(3)

        def Public_And_Publish_Now(driver):
            PublicRadio = find_my_element(driver,"ID",PUBLIC_RADIOBUTTON)
            PublishNowRadio = find_my_element(driver,"ID",PUBLISH_NOW_RADIOBUTTON)
            if(PublicRadio.is_enabled == False):
                print("Error: Public radio button is not enabled")
            else:
                PublicRadio.click()
                time.sleep(1)
            if(PublishNowRadio.is_enabled == False):
                print("Error: Publish now radio button is not enabled")
            else:
                PublishNowRadio.click()
                time.sleep(2)
            # Save and continue
            Btn = find_my_element(driver,"XPATH",SAVE_AND_CONTINUE_PUBLISH)
            driver.execute_script("arguments[0].scrollIntoView();",Btn)
            time.sleep(2)
            Btn.click()
            time.sleep(2)
            # Navigate to event list to check if it was added
            # Account from navbar
            To_EventList(driver)
            # Check in EventList
            SearchBar = find_my_element(driver,"ID",EVENTS_SEARCH_BAR)
            SearchBar.clear()
            SearchBar.send_keys(MY_EVENT_NAME)
            time.sleep(4)
            SearchedEvents=find_my_elements(driver,"XPATH",EVENTS_LIST)
            SearchedEventsCount = len(SearchedEvents) -1
            if(SearchedEventsCount == 0):
                print("Error! Event not present in eventlist")
            # Check in Landing page
            Element=find_my_element(driver,"XPATH",HEBTUS_LOGO)
            Element.click()
            time.sleep(5)
            if(not GetEvents(driver)):
                print("Error! Public Event is not present in Landing page")
            
            
        def Private_Event(driver):
            SearchBar = find_my_element(driver,"ID",EVENTS_SEARCH_BAR)
            SearchBar.clear()
            SearchBar.send_keys(MY_EVENT_NAME)
            time.sleep(4)
            Btn = find_my_element(driver,"XPATH",EDIT_FIRST_EVENTLIST)
            Btn.click()
            time.sleep(3)
            PublishButton = find_my_element(driver,"XPATH",GO_TO_PUBLISH)
            PublishButton.click()
            time.sleep(4)
            PrivateRadio = find_my_element(driver,"ID",PRIVATE_RADIOBUTTON)
            PrivateRadio.click()
            time.sleep(2)
            # Check in Landing page
            Element=find_my_element(driver,"XPATH",HEBTUS_LOGO)
            driver.execute_script("arguments[0].scrollIntoView();",Element)
            time.sleep(2)
            Element.click()
            time.sleep(5)
            if(GetEvents(driver)):
                print("Error! Private event is present in Landing page")

        # ScheduleLaterRadio = find_my_element(driver,"ID",SCHEDULE_LATER_RADIOBUTTON)

        Navigation_Test(driver)
        RadioButtons_Enabled(driver)
        Validate_Event_Details(driver)
        Public_And_Publish_Now(driver)
        To_EventList2(driver)
        Private_Event(driver)
