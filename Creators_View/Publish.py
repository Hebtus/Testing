# To give us access to the enter key, escape key...etc. ex: when I write something in the search bar and want to press enter:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.wait import WebDriverWait

import sys
sys.path.append(".") # To access modules in sibling directories

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

        def Radiobuttons_Enabled_Test(driver):
            PublicRadio = find_my_element(driver,"ID",PUBLIC_RADIOBUTTON)
            PrivateRadio = find_my_element(driver,"ID",PRIVATE_RADIOBUTTON)
            PublishNowRadio = find_my_element(driver,"ID",PUBLISH_NOW_RADIOBUTTON)
            ScheduleLaterRadio = find_my_element(driver,"ID",SCHEDULE_LATER_RADIOBUTTON)
            if(PublicRadio.is_enabled == False):
                print("Error: Public radio button is not enabled")
            if(PrivateRadio.is_enabled == False):
                print("Error: Private radio button is not enabled")
            if(PublishNowRadio.is_enabled == False):
                print("Error: Publish now radio button is not enabled")
            if(ScheduleLaterRadio.is_enabled == False):
                print("Error: Schedule later radio button is not enabled")

        Navigation_Test(driver)
        Validate_Event_Details(driver)
        Radiobuttons_Enabled_Test(driver)
