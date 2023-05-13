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
    # Validate Navigation (check if "Tickets" title is present)
    TicketsTitle = find_my_element(driver,"XPATH",TICKETS_TITLE)
    check_not_found(driver,TicketsTitle,"Did not navigate to Tickets page")

    time.sleep(2)
    touch = TouchAction(driver)

    # Click on add more tickets
    AddTicket = find_my_element(driver,"XPATH",ADD_MORE_TICKETS)
    AddTicket.click()
    time.sleep(2)

    # Fill fields for adding ticket
    # Name
    Textbox = find_my_element(driver, "XPATH", ADD_TICKETS_NAME)
    check_not_found(driver, Textbox, "Name textbox not found")
    Textbox.click()
    time.sleep(1)
    Textbox.send_keys("Silver tickets")
    time.sleep(1)
    # Price
    Textbox = find_my_element(driver, "XPATH", ADD_TICKETS_PRICE)
    check_not_found(driver, Textbox, "Price textbox not found")
    Textbox.click()
    time.sleep(1)
    Textbox.send_keys("150")
    time.sleep(1)
    # Quantity
    Textbox = find_my_element(driver, "XPATH", ADD_TICKETS_QUANTITY)
    check_not_found(driver, Textbox, "Quantity textbox not found")
    Textbox.click()
    time.sleep(1)
    Textbox.send_keys("20")
    time.sleep(1)
    # Swipe to date and time
    touch.press(x=228, y=565).move_to(x=235,y=105).release().perform()
    time.sleep(2)
    # Date and time
    StartDate = find_my_element(driver, "XPATH", ADD_TICKETS_EVENT_STARTS)
    check_not_found(driver, StartDate, "Start date not found")
    StartDate.click()
    time.sleep(1)
    StartDate = find_my_element(driver, "XPATH", ADD_TICKETS_EVENT_STARTS)
    check_not_found(driver, StartDate, "Start date not found 2")
    StartDate.send_keys("2023-05-16")
    time.sleep(2)
    driver.hide_keyboard()
    time.sleep(2)
    
    EndDate = find_my_element(driver, "XPATH", ADD_TICKETS_EVENT_ENDS)
    check_not_found(driver, EndDate, "End date not found")
    EndDate.click()
    time.sleep(1)
    EndDate = find_my_element(driver, "XPATH", ADD_TICKETS_EVENT_ENDS)
    check_not_found(driver, EndDate, "End date not found 2")
    EndDate.send_keys("2023-05-17")
    time.sleep(1)
    driver.hide_keyboard()
    time.sleep(2)

    # Add ticket
    AddTicketBtn = find_my_element(driver, "XPATH", ADD_TICKET_BTN)
    check_not_found(driver, AddTicketBtn, "Add ticket button not found")
    AddTicketBtn.click()
    time.sleep(3)
    # Go back
    GoBack = find_my_element(driver, "XPATH", ADD_TICKETS_GO_BACK)
    check_not_found(driver, GoBack, "Go back button not found")
    GoBack.click()
    time.sleep(3)

    # outer swipe down to refresh
    touch.press(x=225, y=690).move_to(x=441,y=286).release().perform()
    time.sleep(2)

    # refresh
    Refresh = find_my_element(driver, "XPATH", REFRESH)
    check_not_found(driver, Refresh, "Go back button not found")
    Refresh.click()
    time.sleep(3)

    # Initial swipe to get frame of ticket cards
    touch.press(x=472, y=385).move_to(x=463,y=222).release().perform()
    time.sleep(2)

    # retrieve data for all ticket cards
    # outer loop that swipes
    while(True):
        # retrieve cards
        Cards = find_my_elements(driver,"XPATH",TICKET_CARDS)
        
    
    # Check if a ticket card has been added

    Card = find_my_element(driver, "XPATH", TICKET_CARD)
    check_not_found(driver, Card, "Failed to add ticket! No ticket card has been added.")





    

