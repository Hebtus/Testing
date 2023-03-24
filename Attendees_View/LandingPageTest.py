# To give us access to the enter key, escape key...etc. ex: when I write something in the search bar and want to press enter:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import sys

sys.path.append(".")  # To access modules in sibling directories

from Common_Files.Utilities import *
from Common_Files.RealReferences import *

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains


def landing_page(driver):
    login(driver, "testereventbrite@gmail.com", "eventbritetester")


def categories_test(driver):
    print("")


def tabs_test(driver):
    print("")


def location_nearby_events_test(driver):
    print("")


def login(driver, Email, Password):
    driver.get("https://www.eventbrite.com/signin")
    driver.maximize_window()
    driver.implicitly_wait(5)
    EmailTextbox = find_my_element(driver, "ID", EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.send_keys(Email)
    PasswordTextbox = find_my_element(driver, "ID", PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.send_keys(Password)
    time.sleep(10)
    LoginButton = find_my_element(driver, "XPATH", LOGIN_BUTTON)
    check_not_found(driver, LoginButton, "Login button not found")
    LoginButton.click()
    time.sleep(30)
    AdExitButton = find_my_element(driver, "XPATH", AD_EXIT_BUTTON)
    if AdExitButton != None:
        AdExitButton.click()
        time.sleep(10)
        LeaveButton = find_my_element(driver, "XPATH", AD_WANT_TO_LEAVE_BUTTON)
        if LeaveButton != None:
            LeaveButton.click()
            time.sleep(10)
    LandingPage = find_my_element(driver, "XPATH", LANDING_PAGE)
    check_not_found(driver, LandingPage, "Landing page not reached")
    time.sleep(30)
    see_more_test(driver)


def see_more_test(driver):
    # Scroll down
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(30)
    SeeMoreButton = find_my_element(driver, "XPATH", SEE_MORE_BUTTON)
    check_not_found(driver, SeeMoreButton, "See more button not found")
    SeeMoreButton.click()
    time.sleep(30)
    SeeMorePge = find_my_element(driver, "XPATH", SEE_MORE_PAGE)
    check_not_found(driver, SeeMoreButton, "See more page not reached")
    time.sleep(10)
    print("See more test passed")
    driver.close()
