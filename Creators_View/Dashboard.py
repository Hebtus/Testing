# To give us access to the enter key, escape key...etc. ex: when I write something in the search bar and want to press enter:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pyperclip

from selenium.webdriver.support.wait import WebDriverWait

import sys
sys.path.append(".") # To access modules in sibling directories

from Common_Files.Utilities import *
from Common_Files.RealReferences import *



def dashboard(driver):
    # Go to event list
    Btn = find_my_element(driver,"XPATH",GO_TO_EVENTLIST)
    Btn.click()
    time.sleep(4)
# ----- PAST EVENTS: ----- #
    FilterButton = find_my_element(driver,"ID",FILTER_EVENTS_BUTTON) 
    FilterButton.click()
    time.sleep(1)
    PastEventsButton = find_my_element(driver,"ID", FILTER_PAST_EVENTS)
    PastEventsButton.click()
    FilterButton.click()
    time.sleep(8)
    TestEvent=find_my_element(driver,"ID",EVENT_TO_TEST)
    driver.execute_script("arguments[0].scrollIntoView();",TestEvent)
    time.sleep(2)
    TestEvent=find_my_element(driver,"XPATH",TEST_EVENT_PROFIT_EVENTLIST)
    PriceInEventlist = TestEvent.get_attribute("innerHTML")
    PriceInEventlistList=PriceInEventlist.split("$")
    EventListPrice = PriceInEventlistList[1].split(".")
    TestEvent = find_my_element(driver,"ID",EVENT_TO_TEST_EDIT)
    TestEvent.click()
    time.sleep(4)
    Btn = find_my_element(driver,"XPATH",GO_TO_DASHBOARD)
    Btn.click()
    time.sleep(4)

    # Event URL Copy
    CopyURLChoice=find_my_element(driver,"ID",DASHBOARD_URL)
    CopyURLChoice.click()
    time.sleep(3)
    URL = pyperclip.paste()
    # Check if copied URL is a valid URL:
    if "https://hebtus.me/events" not in  URL:
        print("Error: clicking on Copy URL does not provide a valid URL")

    # Check if navigates to Review your publish settings
    Element = find_my_element(driver,"ID",PUBLISH_HYPERLINK)
    Element.click()
    time.sleep(4)
    Element = find_my_element(driver,"XPATH",PUBLISH_YOUR_EVENT_IDENTIFIER)
    if(Element == None):
        print("Error! Did not navigate to publish settings when clicking Review your publish settings")
    else: # go back
        Btn = find_my_element(driver,"XPATH",GO_TO_DASHBOARD)
        Btn.click()
        time.sleep(4)

    # check if Open page views report works
    Element = find_my_element(driver,"XPATH",PAGE_VIEW_REPORTS_HYPERLINK)
    Element.click()
    if(find_my_element(driver,"XPATH",DASHBOARD_TITLE) != None):
        print("Error! did not go to page views report")

    # check if Attendee summary report works
    Element = find_my_element(driver,"XPATH",ATTENDEE_SUMMARY_REPORT_HYPERLINK)
    Element.click()
    if(find_my_element(driver,"XPATH",DASHBOARD_TITLE) != None):
        print("Error! did not go to Attendee summary report")

    # Check if price of sold tickets matches the one in eventlist$0.00
    # scroll to recent orders
    Title=find_my_element(driver,"ID",DASHBOARD_RECENT_ORDER)
    driver.execute_script("arguments[0].scrollIntoView();",Title)
    time.sleep(2)

    TestEvent=find_my_element(driver,"XPATH",RECENT_ORDERS_PRICE)
    PriceOneTicket = TestEvent.get_attribute("innerHTML")
    TestEvent=find_my_element(driver,"XPATH",RECENT_ORDERS_QUANTITY)
    AmountOfTickets = TestEvent.get_attribute("innerHTML")

    if((int(PriceOneTicket)*int(AmountOfTickets)) != int(EventListPrice[0])):
        print("Error! Amount of sold tickets in eventlist does not match the one in dashboard")


