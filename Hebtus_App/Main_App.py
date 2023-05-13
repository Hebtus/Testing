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

from Creators_View.Navigation import *
from Creators_View.BasicInfo import basic_info
from Creators_View.Tickets import *
from Creators_View.Publish import *
from Creators_View.Dashboard import *


import time

desired_cap = {
    "deviceName": "Nexus S API 33_mydevice2",
    "udid": "emulator-5554",
    "platformName": "Android",
    "platformVersion": "13.0",
    "appActivity": "com.example.hebtus_crossplatform.MainActivity",
    "appPackage": "com.example.hebtus_crossplatform"
}


driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(120)
# ---------------------------------------------------------------- Start ---------------------------------------------------------------- #
# ------------- Attendee's view web pages testing ------------- #
#sign_up(driver)
# sign_in(driver)
# event_page(driver)
# landing_page(driver)
# ----- Navigation from Attendee's view to Creator's view ----- #

# ------------- Creator's view web pages testing -------------- #
# creator_view(driver)  # temporary
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



#To_Event_List(driver)
#To_Dashboard_Second_Event(driver)
#To_Main_Menu_First_Event(driver)


#basic_info(driver)
