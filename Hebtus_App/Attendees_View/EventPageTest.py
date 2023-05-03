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

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains


def event_page(driver):
    sign_in_valid(driver, "ayausamakhalifa@gmail.com", "123456789")
    # events_info_test(driver)
    GetEvents(driver)


# * Phase 4
def sign_in_valid(driver, Email, Password):
    # ---------------------------------------------- Testing valid log in ---------------------------------------------- #
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
    # check if landing page is reached
    LandingPage = find_my_element(driver, "XPATH", LANDING_PAGE)
    check_not_found(driver, LandingPage, "Landing page not reached")
    print("signed in successfuly")


# content_desc = element.get_attribute("content-desc")


# ? Phase 5
def GetEvents(driver):
    # Get the screen dimensions
    screen_width = driver.get_window_size()["width"]
    screen_height = driver.get_window_size()["height"]
    ContentSet = set()
    old_page_source = None
    for j in range(10):
        # Scroll down using TouchAction
        swipe_action = TouchAction(driver)
        swipe_action.press(x=screen_width * 0.5, y=screen_height * 0.8).move_to(
            x=screen_width * 0.5, y=screen_height * 0.2
        ).release().perform()
        time.sleep(3)
        # Scroll down using TouchAction
        swipe_action = TouchAction(driver)
        swipe_action.press(x=screen_width * 0.5, y=screen_height * 0.8).move_to(
            x=screen_width * 0.5, y=screen_height * 0.2
        ).release().perform()
        time.sleep(3)
        for i in range(6):
            EVENT = EVENT_1 + str(i) + EVENT_2
            Event = find_my_element(driver, "XPATH", EVENT)
            check_not_found(driver, Event, "Event Not FOUNDDDDDDDDDD")
            time.sleep(2)
            ContentSet.add(Event.get_attribute("content-desc"))
            print(Event.get_attribute("content-desc"))
            print(str(i) + ": ------------------------------")
        if old_page_source is not None and driver.page_source == old_page_source:
            break
        old_page_source = driver.page_source
    print(ContentSet)
    DateSet = set()
    for event in ContentSet:
        EventsInfo = event.split("\n")
        Date = EventsInfo[1].split(" ")[0]
        DateSet.add(Date)

    exit()
    # Get the screen dimensions
    screen_width = driver.get_window_size()["width"]
    screen_height = driver.get_window_size()["height"]
    # Scroll down using TouchAction
    swipe_action = TouchAction(driver)
    swipe_action.press(x=screen_width * 0.5, y=screen_height * 0.8).move_to(
        x=screen_width * 0.5, y=screen_height * 0.2
    ).release().perform()

    # for i in range(5):
    time.sleep(3)
    # EVENT = EVENT1 + str(i) + EVENT2
    Event = find_my_element(driver, "XPATH", EVENT1)
    check_not_found(driver, Event, "Event Not FOUNDDDDDDDDDD")
    time.sleep(2)
    print(Event.get_attribute("content-desc"))
    print("------------------------------")
    time.sleep(2)
    Event = find_my_element(driver, "XPATH", EVENT2)
    check_not_found(driver, Event, "Event Not FOUNDDDDDDDDDD")
    time.sleep(2)
    print(Event.get_attribute("content-desc"))
    print("------------------------------")
    # Scroll down using TouchAction
    swipe_action = TouchAction(driver)
    swipe_action.press(x=screen_width * 0.5, y=screen_height * 0.8).move_to(
        x=screen_width * 0.5, y=screen_height * 0.2
    ).release().perform()
    time.sleep(3)
    Event = find_my_element(driver, "XPATH", EVENT3)
    check_not_found(driver, Event, "Event Not FOUNDDDDDDDDDD")
    time.sleep(2)
    print(Event.get_attribute("content-desc"))
    print("------------------------------")
    time.sleep(2)
    Event = find_my_element(driver, "XPATH", EVENT4)
    check_not_found(driver, Event, "Event Not FOUNDDDDDDDDDD")
    time.sleep(2)
    print(Event.get_attribute("content-desc"))
    print("------------------------------")
    time.sleep(2)
    Event = find_my_element(driver, "XPATH", EVENT5)
    check_not_found(driver, Event, "Event Not FOUNDDDDDDDDDD")
    time.sleep(2)
    print(Event.get_attribute("content-desc"))
    print("------------------------------")
    time.sleep(2)
    Event = find_my_element(driver, "XPATH", EVENT6)
    check_not_found(driver, Event, "Event Not FOUNDDDDDDDDDD")
    time.sleep(2)
    print(Event.get_attribute("content-desc"))
    print("------------------------------")
    # Scroll down using TouchAction
    swipe_action = TouchAction(driver)
    swipe_action.press(x=screen_width * 0.5, y=screen_height * 0.8).move_to(
        x=screen_width * 0.5, y=screen_height * 0.2
    ).release().perform()
    time.sleep(3)
    # driver.quit()
    exit()

    Event = find_my_element(driver, "XPATH", EVENT)
    check_not_found(driver, Event, "Event Not FOUNDDDDDDDDDD")
    time.sleep(10)
    print("Event found")
    print(Event.get_attribute("content-desc"))
    driver.quit()
    exit()
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


def check_displayed(driver, type, value, message):
    # ---------------------------------------------- Auxiliary function to check if element is displayed ---------------------------------------------- #
    element = find_my_element(driver, type, value)
    check_not_found(driver, element, message)
    if element.is_displayed() == False:
        print(message)


# * Phase 4
def events_info_test(driver):
    # Get the screen dimensions
    screen_width = driver.get_window_size()["width"]
    screen_height = driver.get_window_size()["height"]
    swipe_action = TouchAction(driver)
    swipe_action.press(x=screen_width * 0.5, y=screen_height * 0.8).move_to(
        x=screen_width * 0.5, y=screen_height * 0.2
    ).release().perform()

    # EVENT2 = "']//android.widget.ImageView[@index='0'and @class='android.widget.ImageView'][1]"
    # Scroll down using TouchAction
    Event = find_my_element(driver, "XPATH", EVENT)
    check_not_found(driver, Event, "Event Not Found")
    Event.click()
    time.sleep(3)
    # ---------------------------------------------- Testing Events info ---------------------------------------------- #
    # Image
    check_displayed(driver, "XPATH", IMAGE, "Image not displayed")
    # Tickets
    check_displayed(driver, "XPATH", TICKETS_INFO, "Tickets info not displayed")

    BookTicketButton = find_my_element(driver, "XPATH", GET_TICKET_BUTTON)
    check_not_found(driver, BookTicketButton, "Reserve your spot button not found")

    PlusButton = find_my_element(driver, "XPATH", PLUS_BUTTON)
    check_not_found(driver, PlusButton, "+ button not found")

    MinusButton = find_my_element(driver, "XPATH", MINUS_BUTTON)
    check_not_found(driver, MinusButton, "- button not found")

    # Scroll down
    # Get the screen dimensions
    screen_width = driver.get_window_size()["width"]
    screen_height = driver.get_window_size()["height"]
    swipe_action = TouchAction(driver)
    swipe_action.press(x=screen_width * 0.5, y=screen_height * 0.7).move_to(
        x=screen_width * 0.5, y=screen_height * 0.2
    ).release().perform()

    # Start date
    check_displayed(driver, "XPATH", START_DATE, "Start date not displayed")
    element = find_my_element(driver, "XPATH", START_DATE)
    print(element.get_attribute("content-desc"))

    # Event title
    check_displayed(driver, "XPATH", EVENT_TITLE, "Event title not displayed")
    # Date and time
    check_displayed(driver, "XPATH", DATE_TIME, "Date and time not displayed")
    # Location
    check_displayed(driver, "XPATH", LOCATION, "Location not displayed")

    # Scroll down
    # Get the screen dimensions
    screen_width = driver.get_window_size()["width"]
    screen_height = driver.get_window_size()["height"]
    swipe_action = TouchAction(driver)
    swipe_action.press(x=screen_width * 0.5, y=screen_height * 0.7).move_to(
        x=screen_width * 0.5, y=screen_height * 0.2
    ).release().perform()

    # About this event
    check_displayed(driver, "XPATH", EVENTS_DETAILS_1, "Event's details not displayed")
    check_displayed(driver, "XPATH", EVENTS_DETAILS_2, "Event's details not displayed")

    time.sleep(3)
    print("Info displayed")
    driver.quit()
