# To give us access to the enter key, escape key...etc. ex: when I write something in the search bar and want to press enter:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.wait import WebDriverWait

import sys
sys.path.append(".") # To access modules in sibling directories
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

from Common_Files.Utilities import *
from Common_Files.RealReferences import *

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
            DateTitle = find_my_element(driver,"XPATH",PUBLISH_DATE_TITLE)
            print("Title HTML: ",EventTitle.get_attribute("innerHTML"))
            print("Title value: ",EventTitle.get_attribute("value"))
            print("Title text: ",EventTitle.text)

            print("DateTitle HTML: ",DateTitle.get_attribute("innerHTML"))
            print("DateTitle value: ",DateTitle.get_attribute("value"))
            print("DateTitle text: ",DateTitle.text)

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
            Element=find_my_element(driver,"XPATH",ACCOUNT_NAVBAR)
            driver.execute_script("arguments[0].scrollIntoView();",Element)
            time.sleep(2)
            Element.click()
            Element=find_my_element(driver,"XPATH",MANAGE_MY_EVENTS_PUBLISH)
            time.sleep(2)
            Element.click()
            time.sleep(3)
            # Check in EventList
            Element=find_my_element(driver,"XPATH",FIRST_EVENT_EVENTLIST)
            print(Element.get_attribute("innerHTML"))
            if(Element.get_attribute("innerHTML") != MY_EVENT_NAME):
                print("Error! Event not present in eventlist")
             # Check in Landing page
            Element=find_my_element(driver,"XPATH",HEBTUS_LOGO)
            print(Element.get_attribute("innerHTML"))
            if(Element.get_attribute("innerHTML") != MY_EVENT_NAME):
                print("Error! Event not present in eventlist")
            

        # PrivateRadio = find_my_element(driver,"ID",PRIVATE_RADIOBUTTON)
        # ScheduleLaterRadio = find_my_element(driver,"ID",SCHEDULE_LATER_RADIOBUTTON)

        Navigation_Test(driver)
        Validate_Event_Details(driver)
        Public_And_Publish_Now(driver)
