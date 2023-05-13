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

def log_in(driver, Email, Password):
    # enter email and password
    EmailTextbox = find_my_element(driver, "XPATH", EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.click()
    time.sleep(1)
    EmailTextbox = find_my_element(driver, "XPATH", EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found 2")
    EmailTextbox.send_keys(Email)
    time.sleep(1)

    PasswordTextbox = find_my_element(driver, "XPATH", PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.click()
    time.sleep(1)
    PasswordTextbox = find_my_element(driver, "XPATH", PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found 2")
    PasswordTextbox.send_keys(Password)
    time.sleep(1)
    LoginButton = find_my_element(driver, "XPATH", LOGIN_BUTTON)
    check_not_found(driver, LoginButton, "Login button not found")
    LoginButton.click()
    time.sleep(4)

def Skip_Location(driver):
    # Choose only once:
    Location = find_my_element(driver,"XPATH",ONLY_ONCE_LOCATION)
    Location.click()
    time.sleep(6)
    # check if landing page is reached
    LandingPage = find_my_element(driver, "XPATH", LANDING_PAGE)
    check_not_found(driver, LandingPage, "Landing page not reached")
    print("signed in successfuly")
    time.sleep(8)

def Main_Menu_Button(driver):
    # Choose only once:
    MainMenuBtn = find_my_element(driver,"XPATH",BASIC_INFO_MAIN_MENU_BTN)
    check_not_found(driver, MainMenuBtn, "MainMenuBtn not found")
    MainMenuBtn.click()
    time.sleep(4)

def To_Event_List(driver):
    # Click on account icon:
    Account = find_my_element(driver,"XPATH",ACCOUNT_ICON)
    Account.click()
    time.sleep(1)
    # Click on manage my events
    ManageEvents = find_my_element(driver,"XPATH",MANAGE_MY_EVENTS)
    ManageEvents.click()
    time.sleep(3)

def To_Dashboard_Second_Event(driver):
    # Validate navigation to event list
    Title = find_my_element(driver,"XPATH",EVENT_LIST_TITLE)
    check_not_found(driver,Title,"Failed to navigate to event list")
    # Click on first event in event list
    FirstEvent = find_my_element(driver,"XPATH",SECOND_EVENT)
    FirstEvent.click()
    time.sleep(3)

def To_Main_Menu_First_Event(driver):
    # Validate navigation to event list
    Title = find_my_element(driver,"XPATH",DASHBOARD_TITLE)
    check_not_found(driver,Title,"Failed to navigate to dashboard")
    # This gets the main menu of an event
    MainMenu = find_my_element(driver,"XPATH",MENU_DASHBOARD)
    MainMenu.click()
    time.sleep(3)

def Main_Menu_Tickets(driver):
    # This gets the main menu of an event
    MainMenuChoice = find_my_element(driver,"XPATH",MAIN_MENU_TICKETS)
    MainMenuChoice.click()
    time.sleep(3)

def Main_Menu_Publish(driver):
    # This gets the main menu of an event
    MainMenuChoice = find_my_element(driver,"XPATH",MAIN_MENU_PUBLISH)
    MainMenuChoice.click()
    time.sleep(3)

def Main_Menu_Dashboard(driver):
    # This gets the main menu of an event
    MainMenuChoice = find_my_element(driver,"XPATH",DASHBOARD_MENU_CHOICE)
    MainMenuChoice.click()
    time.sleep(3)

def Main_Menu_First_Event_Dashboard(driver):
    # This gets the main menu of an event
    MainMenuChoice = find_my_element(driver,"XPATH",MAIN_MENU_DASHBOARD)
    MainMenuChoice.click()
    time.sleep(3)





