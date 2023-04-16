# To give us access to the enter key, escape key...etc. ex: when I write something in the search bar and want to press enter:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import sys

sys.path.append(".")  # To access modules in sibling directories

from Common_Files.Utilities import *
from Common_Files.RealReferences_Hebtus import *

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains


def event_page(driver):
    # login(driver, "testereventbrite@gmail.com", "eventbritetester")
    GetEvents(driver)


def GetEvents(driver):
    driver.get("https://www.hebtus.me/#")
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(5)
    EventsList = driver.find_elements(
        By.CLASS_NAME,
        "col",
    )
    if EventsList == None:
        print("No events in the today list")
        driver.close()
        exit()
    else:
        print(len(EventsList))

    # EventsNum = len(EventsList)
    EventsNum = 5
    for i in range(1, EventsNum):
        time.sleep(5)
        EVENT = EVENT_LIST_1 + str(i) + EVENT_LIST_2
        Event = find_my_element(driver, "XPATH", EVENT)
        if Event != None:
            driver.execute_script("arguments[0].scrollIntoView();", Event)
            time.sleep(5)
            # create action chain object
            action = ActionChains(driver)
            # perform the operation
            action.move_to_element(Event).click().perform()
            time.sleep(10)
            # Test EventPage
            events_info_test(driver)
            driver.back()
        else:
            print("No event")
    driver.close()


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


def events_info_test(driver):
    # ---------------------------------------------- Testing Events info ---------------------------------------------- #
    # Image
    check_displayed(driver, "XPATH", IMAGE, "Image not displayed")
    # Start date
    check_displayed(driver, "XPATH", START_DATE, "Start date not displayed")
    # Event title
    check_displayed(driver, "XPATH", EVENT_TITLE, "Event title not displayed")
    # Date and time
    check_displayed(driver, "XPATH", DATE_TIME, "Date and time not displayed")
    # Location
    check_displayed(driver, "XPATH", LOCATION, "Location not displayed")
    # About this event
    check_displayed(driver, "XPATH", EVENTS_DETAILS, "Event's details not displayed")

    # Tickets
    check_displayed(driver, "XPATH", TICKETS_INFO, "Tickets info not displayed")
    # Scroll down
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(30)

    BookTicketButton = find_my_element(driver, "XPATH", GET_TICKET_BUTTON)
    check_not_found(driver, BookTicketButton, "Reserve your spot button not found")

    print("Info displayed")
