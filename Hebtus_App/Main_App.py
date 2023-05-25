from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ----- Includes for Attendee's view web pages ----- #
from Attendees_View.SignUpTest import sign_up
from Attendees_View.SignInTest import sign_in
from Attendees_View.EventPageTest import event_page
from Attendees_View.LandingPageTest import landing_page

# ----- Includes for Attendee's view web pages ----- #
from Creators_View.Navigation import *
from Creators_View.BasicInfo import basic_info
from Creators_View.Tickets import *
from Creators_View.Publish import *
from Creators_View.Dashboard import *

import time

choice = int(input("Enter \n (1) For Attendee's View \n (2) For Creator's View \n"))

desired_cap = {
    "deviceName": "MyDevice",
    "udid": "emulator-5554",
    "platformName": "Android",
    "platformVersion": "10.0",
    "appActivity": "com.example.hebtus_crossplatform.MainActivity",
    "appPackage": "com.example.hebtus_crossplatform",
    "newCommandTimeout": 1000,
}


driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(120)
time.sleep(20)
# ---------------------------------------------------------------- Start ---------------------------------------------------------------- #
if(choice == 1):
    # ------------- Attendee's view web pages testing ------------- #
    # sign_up(driver)
    # sign_in(driver)
    # event_page(driver)
    landing_page(driver)

elif(choice == 2):
    # ------------- Creator's view web pages testing -------------- #
    log_in(driver, "ayausamakhalifa@gmail.com", "123456789")
    Skip_Location(driver)
    basic_info(driver)
    Main_Menu_Button(driver)
    Main_Menu_Tickets(driver)
    tickets(driver)
    Main_Menu_Button(driver)
    Main_Menu_Publish(driver)
    publish(driver)
    Main_Menu_Button(driver)
    Main_Menu_Dashboard(driver)
    dashboard(driver)