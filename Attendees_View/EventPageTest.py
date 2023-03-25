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


def event_page(driver):
    login(driver, "testereventbrite@gmail.com", "eventbritetester")


def login(driver, Email, Password):
    # Open eventbrite
    driver.get("https://www.eventbrite.com/signin")
    driver.maximize_window()
    driver.implicitly_wait(5)
    # login with email and password
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
    # Scroll down to laod
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(30)
    # try:
    #     EventsList = WebDriverWait(driver, 20).until(
    #         EC.presence_of_element_located(
    #             (
    #                 By.CLASS_NAME,
    #                 "feed-events-bucket__content__cards-container",
    #             )
    #         )
    #     )
    # except:
    #     print("Element not found.")
    #     exit()
    # Get list of events
    EventsList = driver.find_elements(
        By.CLASS_NAME,
        EVENT_ELEMENT,
    )
    if len(EventsList) == 0:
        print("No events in the list")
        driver.close()
        exit()
    EventsURLList = []
    EventsList = EventsList[0:9]
    # Get URLs of events page
    for element in EventsList:
        try:
            link = element.find_element(By.TAG_NAME, "a")
            EventsURLList.append(link.get_attribute("href"))
            print(link.get_attribute("href"))
        except:
            print("No Data Available!")

    events_info_test(driver, EventsURLList)


def check_displayed(driver, type, value, message):
    # ---------------------------------------------- Auxiliary function to check if element is displayed ---------------------------------------------- #
    element = find_my_element(driver, type, value)
    check_not_found(driver, element, message)
    if element.is_displayed() == False:
        print(message)


def events_info_test(driver, URLList):
    # ---------------------------------------------- Testing Events info ---------------------------------------------- #
    for i in range(2):
        Link = URLList[i]
        driver.get(Link)
        driver.implicitly_wait(5)
        # Image
        check_displayed(driver, "XPATH", IMAGE, "Image not displayed")
        # Start date
        check_displayed(driver, "XPATH", START_DATE, "Start date not displayed")
        # Event title
        check_displayed(driver, "XPATH", EVENT_TITLE, "Event title not displayed")
        # Event Summary
        check_displayed(driver, "XPATH", EVENT_SUMMARY, "Event summary not displayed")
        # Simplified Organizer info
        check_displayed(
            driver,
            "XPATH",
            SIMPLIDIED_ORGANIZER_INFO,
            "Simplified organizer info not displayed",
        )
        # Tickets
        check_displayed(driver, "XPATH", TICKETS_INFO, "Tickets info not displayed")
        # Date and time
        check_displayed(driver, "XPATH", DATE_TIME, "Date and time not displayed")
        # Location
        check_displayed(driver, "XPATH", LOCATION, "Location not displayed")
        # About this event
        check_displayed(
            driver, "XPATH", EVENTS_DETAILS, "Event's details not displayed"
        )
        # Scroll down
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(30)
        # About the organizer
        check_displayed(driver, "XPATH", ORGANIZER_INFO, "Organizer info not displayed")
        # BookTicketButton = find_my_element(driver, "XPATH", RESERVE_SPOT_BUTTON)
        # if BookTicketButton == None:
        #     BookTicketButton = find_my_element(driver, "XPATH", TICKETS_BUTTON)
        #     check_not_found(
        #         driver, BookTicketButton, "Reserve your spot button not found"
        #     )
        # BookTicketButton.click()
        # time.sleep(30)
        # RegisterWindow = find_my_element(driver, "XPATH", REGISTER_PAGE)
        # if RegisterWindow == None:
        #     RegisterWindow = find_my_element(driver, "XPATH", CHECKOUT_BUTTON)
        #     check_not_found(driver, RegisterWindow, "Register window not found")
        time.sleep(20)
        print("Info displayed")
        driver.close()
