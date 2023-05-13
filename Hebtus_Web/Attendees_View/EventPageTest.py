# To give us access to the enter key, escape key...etc. ex: when I write something in the search bar and want to press enter:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import sys
from math import ceil

sys.path.append(".")  # To access modules in sibling directories

from Common_Files.Utilities import *
from Common_Files.RealReferences_Hebtus import *

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains


def event_page(driver):
    login(driver, "hebtususer@gmail.com", "123456789")
    # GetEvents(driver)
    get_event_booking(driver)


# * Phase 4
def GetEvents(driver):
    time.sleep(20)
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
    EventsNum = 3
    for i in range(1, EventsNum):
        time.sleep(5)
        EVENT = EVENT_LIST_1 + str(i) + EVENT_LIST_2
        Event = find_my_element(driver, "XPATH", EVENT)
        if Event != None:
            # Scroll the element into view
            driver.execute_script("arguments[0].scrollIntoView();", Event)
            time.sleep(15)
            driver.execute_script("arguments[0].click();", Event)
            time.sleep(10)
            # Test EventPage
            events_info_test(driver)
            driver.back()
        else:
            print("No event")
    driver.close()


# ? Phase 5
def login(driver, Email, Password):
    # ---------------------------------------------- Testing valid log in ---------------------------------------------- #
    driver.get("https://www.hebtus.me/login")
    driver.maximize_window()
    driver.implicitly_wait(60)
    time.sleep(12)
    # enter email and password
    EmailTextbox = find_my_element(driver, "ID", EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.send_keys(Email)
    PasswordTextbox = find_my_element(driver, "ID", PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.send_keys(Password)
    time.sleep(3)
    LoginButton = find_my_element(driver, "ID", LOGIN_BUTTON)
    check_not_found(driver, LoginButton, "Login button not found")
    LoginButton.click()
    time.sleep(15)
    # check if landing page is reached
    LandingPage = find_my_element(driver, "ID", LANDING_PAGE)
    check_not_found(driver, LandingPage, "Landing page not reached")
    time.sleep(5)
    print("signed in successfuly")


# * Phase 4
def check_displayed(driver, type, value, message):
    # ---------------------------------------------- Auxiliary function to check if element is displayed ---------------------------------------------- #
    element = find_my_element(driver, type, value)
    check_not_found(driver, element, message)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    if element.is_displayed() == False:
        print(message)


# * Phase 4
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


# ? phase 5
def invalid_booking_test(driver):
    GetTicketButton = find_my_element(driver, "ID", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    driver.execute_script("arguments[0].scrollIntoView();", GetTicketButton)
    GetTicketButton.click()
    time.sleep(1)
    BackToEvent = find_my_element(driver, "ID", "page--button")
    check_not_found(driver, BackToEvent, "Back To Event button not found")
    BackToEvent.click()
    time.sleep(1)
    GetTicketButton = find_my_element(driver, "ID", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    GetTicketButton.click()
    time.sleep(1)
    # checkout without choosing a ticket
    Checkout_Button = find_my_element(driver, "ID", CHECKOUT_BUTTON)
    check_not_found(driver, Checkout_Button, "Checkout button not found")
    Checkout_Button.click()
    time.sleep(1)
    Alert = find_my_element(driver, "ID", CHECKOUT_ALERT)
    check_not_found(driver, Alert, "Choose tickets Alert not found")

    # More than 5 tickets plus is disabled
    PlusButton1 = find_my_element(driver, "XPATH", PLUS_BUTTON_1)
    check_not_found(driver, PlusButton1, "Plus button not found")
    PlusButton1.click()
    PlusButton1.click()
    PlusButton1.click()
    PlusButton1.click()
    PlusButton1.click()
    PlusButton1.click()
    Quantity = find_my_element(driver, "XPATH", TICKET_QUANTITY_1)
    check_not_found(driver, Quantity, "Quantity not found")
    assert int(Quantity.text) == 5, "Wrong Quantity"
    CheckoutButton = find_my_element(driver, "ID", CHECKOUT_BUTTON)
    check_not_found(driver, CheckoutButton, "Checkout Button button not found")
    CheckoutButton.click()
    # add first name
    FirstNameTB = find_my_element(driver, "ID", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTB, "First name textbox not found")
    FirstNameTB.send_keys("FirstName")
    time.sleep(1)
    # add last name
    LastNameTB = find_my_element(driver, "ID", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTB, "Last name textbox not found")
    LastNameTB.send_keys("LastName")
    time.sleep(1)
    # add email
    EmailTB = find_my_element(driver, "ID", EMAIL_TEXTBOX)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    EmailTB.send_keys("user@gmail.com")
    time.sleep(1)
    # Confirm email
    EmailTB = find_my_element(driver, "ID", CONFIRM_EMAIL)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    EmailTB.send_keys("user@gmail.com")
    time.sleep(1)
    # add gender
    GenderTB = find_my_element(driver, "XPATH", FEMALE_RADIO_BUTTON)
    check_not_found(driver, GenderTB, "Gender textbox not found")
    GenderTB.click()
    # * 1) Missing phone number
    # click register
    RegisterButton = find_my_element(driver, "ID", REGISTER_BUTTON)
    check_not_found(driver, RegisterButton, "Register button not found")
    RegisterButton.click()
    # check alert found
    Alert = find_my_element(driver, "ID", "phone-helper-text")
    check_not_found(driver, Alert, "Phone Alert message not found")

    PhoneNumTB = find_my_element(driver, "ID", PHONE_TEXTBOX)
    check_not_found(driver, PhoneNumTB, "Phone number textbox not found")
    PhoneNumTB.send_keys("01221993665")
    time.sleep(1)
    # * 2) Missing first name
    FirstNameTB = find_my_element(driver, "ID", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTB, "First name textbox not found")
    clear_textbox(FirstNameTB)
    time.sleep(1)
    # click register
    RegisterButton = find_my_element(driver, "ID", REGISTER_BUTTON)
    check_not_found(driver, RegisterButton, "Register button not found")
    RegisterButton.click()
    # check alert found
    Alert = find_my_element(driver, "ID", "firstName-helper-text")
    check_not_found(driver, Alert, "First name Alert message not found")
    # add first name
    FirstNameTB = find_my_element(driver, "ID", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTB, "First name textbox not found")
    FirstNameTB.send_keys("FirstName")
    time.sleep(1)
    # * 3) Missing last name
    LastNameTB = find_my_element(driver, "ID", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTB, "Last name textbox not found")
    clear_textbox(LastNameTB)

    time.sleep(1)
    # click register
    RegisterButton = find_my_element(driver, "ID", REGISTER_BUTTON)
    check_not_found(driver, RegisterButton, "Register button not found")
    RegisterButton.click()
    # check alert found
    Alert = find_my_element(driver, "ID", "lastName-helper-text")
    check_not_found(driver, Alert, "Last name Alert message not found")
    # add last name
    LastNameTB = find_my_element(driver, "ID", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTB, "Last name textbox not found")
    LastNameTB.send_keys("LastName")
    time.sleep(1)
    # * 3) Invalid email, wrong confirmation email
    EmailTB = find_my_element(driver, "ID", EMAIL_TEXTBOX)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    clear_textbox(EmailTB)
    EmailTB.send_keys("user")
    time.sleep(1)
    # click register
    RegisterButton = find_my_element(driver, "ID", REGISTER_BUTTON)
    check_not_found(driver, RegisterButton, "Register button not found")
    RegisterButton.click()
    # check alert found
    Alert = find_my_element(driver, "ID", "email-helper-text")
    check_not_found(driver, Alert, "Invalid email alert message not found")
    Alert = find_my_element(driver, "ID", "confirmEmail-helper-text")
    check_not_found(driver, Alert, "Wrong confirmation lert message not found")
    # add last name
    EmailTB = find_my_element(driver, "ID", EMAIL_TEXTBOX)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    clear_textbox(EmailTB)
    EmailTB.send_keys("user@gmail.com")
    time.sleep(1)

    # * 3) Invalid phone , wrong confirmation email
    PhoneNumTB = find_my_element(driver, "ID", PHONE_TEXTBOX)
    check_not_found(driver, PhoneNumTB, "Phone number textbox not found")
    clear_textbox(PhoneNumTB)
    PhoneNumTB.send_keys("123")
    time.sleep(1)
    # click register
    RegisterButton = find_my_element(driver, "ID", REGISTER_BUTTON)
    check_not_found(driver, RegisterButton, "Register button not found")
    RegisterButton.click()
    # check alert found
    Alert = find_my_element(driver, "ID", "phone-helper-text")
    check_not_found(driver, Alert, "invalid phone alert message not found")
    # add last name
    PhoneNumTB = find_my_element(driver, "ID", PHONE_TEXTBOX)
    check_not_found(driver, PhoneNumTB, "Phone number textbox not found")
    clear_textbox(PhoneNumTB)
    PhoneNumTB.send_keys("01221993665")
    time.sleep(1)
    # click close button
    CloseButton = find_my_element(driver, "ID", GET_TICKET_BUTTON)
    check_not_found(driver, CloseButton, "Close button not found")
    driver.execute_script("arguments[0].click();", CloseButton)
    time.sleep(1)
    # check event page reached
    GetTicketButton = find_my_element(driver, "ID", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Event page not found")
    print("Invalid booking test passed")


# ? phase 5
def timer_test(driver):
    GetTicketButton = find_my_element(driver, "ID", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    driver.execute_script("arguments[0].scrollIntoView();", GetTicketButton)
    GetTicketButton.click()
    time.sleep(1)
    BackToEvent = find_my_element(driver, "ID", "page--button")
    check_not_found(driver, BackToEvent, "Back To Event button not found")
    BackToEvent.click()
    time.sleep(1)
    GetTicketButton = find_my_element(driver, "ID", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    GetTicketButton.click()
    time.sleep(1)

    # * 1)
    PlusButton1 = find_my_element(driver, "XPATH", PLUS_BUTTON_1)
    check_not_found(driver, PlusButton1, "Plus button not found")
    PlusButton1.click()
    PlusButton1.click()

    CheckoutButton = find_my_element(driver, "ID", CHECKOUT_BUTTON)
    check_not_found(driver, CheckoutButton, "Checkout Button button not found")
    CheckoutButton.click()

    # wait for 5 minutes
    time.sleep(310)
    TimerAlert = find_my_element(driver, "ID", TIMER_ALERT)
    check_not_found(driver, TimerAlert, "Timer limit reached alert not reached")
    TimerAlert.click()
    # check event page reached
    GetTicketButton = find_my_element(driver, "ID", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Event page not found")
    print("Invalid booking test passed")


# ? phase 5
def valid_booking_test_1(driver):
    GetTicketButton = find_my_element(driver, "ID", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    driver.execute_script("arguments[0].scrollIntoView();", GetTicketButton)
    GetTicketButton.click()
    time.sleep(1)
    BackToEvent = find_my_element(driver, "ID", "page--button")
    check_not_found(driver, BackToEvent, "Back To Event button not found")
    BackToEvent.click()
    time.sleep(1)
    GetTicketButton = find_my_element(driver, "ID", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    GetTicketButton.click()
    time.sleep(1)

    # * 1)
    PlusButton1 = find_my_element(driver, "XPATH", PLUS_BUTTON_1)
    check_not_found(driver, PlusButton1, "Plus button not found")
    PlusButton1.click()
    PlusButton1.click()
    PlusButton1.click()
    PlusButton1.click()
    PlusButton1.click()

    PlusButton2 = find_my_element(driver, "XPATH", PLUS_BUTTON_2)
    check_not_found(driver, PlusButton2, "Plus button not found")
    PlusButton2.click()
    PlusButton2.click()

    CheckoutButton = find_my_element(driver, "ID", CHECKOUT_BUTTON)
    check_not_found(driver, CheckoutButton, "Checkout Button button not found")
    CheckoutButton.click()

    # 🎉 Write Info 🎉
    # add first name
    FirstNameTB = find_my_element(driver, "ID", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTB, "First name textbox not found")
    FirstNameTB.send_keys("FirstName")
    time.sleep(1)
    # add last name
    LastNameTB = find_my_element(driver, "ID", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTB, "Last name textbox not found")
    LastNameTB.send_keys("LastName")
    time.sleep(1)
    # add email
    EmailTB = find_my_element(driver, "ID", EMAIL_TEXTBOX)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    EmailTB.send_keys("user@gmail.com")
    time.sleep(1)
    # Confirm email
    EmailTB = find_my_element(driver, "ID", CONFIRM_EMAIL)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    EmailTB.send_keys("user@gmail.com")
    time.sleep(1)
    # add number
    PhoneNumTB = find_my_element(driver, "ID", PHONE_TEXTBOX)
    check_not_found(driver, PhoneNumTB, "Phone number textbox not found")
    PhoneNumTB.send_keys("01221993665")
    time.sleep(1)
    # add gender
    GenderTB = find_my_element(driver, "XPATH", MALE_RADIO_BUTTON)
    check_not_found(driver, GenderTB, "Gender textbox not found")
    GenderTB.click()
    time.sleep(1)
    # check first checkbox
    Checkbox1 = find_my_element(driver, "ID", BE_INFORMED_CB)
    check_not_found(driver, Checkbox1, "Checkbox 1 not found")
    Checkbox1.click()
    time.sleep(1)
    # check second checkbox
    Checkbox2 = find_my_element(driver, "ID", SEND_EMAIL_CB)
    check_not_found(driver, Checkbox2, "Checkbox 2 not found")
    Checkbox2.click()
    time.sleep(1)
    # click register
    RegisterButton = find_my_element(driver, "ID", REGISTER_BUTTON)
    check_not_found(driver, RegisterButton, "Register button not found")
    RegisterButton.click()
    time.sleep(1)
    # check booking succeeded
    Booked = find_my_element(driver, "ID", "page--button")
    check_not_found(driver, Booked, "Booked successfully message not found")
    Booked.click()
    # check event page reached
    GetTicketButton = find_my_element(driver, "ID", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Event page not found")


# ? phase 5
def valid_booking_test_2(driver):
    GetTicketButton = find_my_element(driver, "ID", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    driver.execute_script("arguments[0].scrollIntoView();", GetTicketButton)
    GetTicketButton.click()
    time.sleep(1)
    BackToEvent = find_my_element(driver, "ID", "page--button")
    check_not_found(driver, BackToEvent, "Back To Event button not found")
    BackToEvent.click()
    time.sleep(1)
    GetTicketButton = find_my_element(driver, "ID", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    GetTicketButton.click()
    time.sleep(1)

    # * 1)
    # check first ticket not avaialble
    PlusButton1 = find_my_element(driver, "XPATH", PLUS_BUTTON_1)
    check_not_found(driver, PlusButton1, "Plus button not found")
    PlusButton1.click()

    PlusButton2 = find_my_element(driver, "XPATH", PLUS_BUTTON_2)
    check_not_found(driver, PlusButton2, "Plus button not found")
    PlusButton2.click()
    PlusButton2.click()
    PlusButton2.click()

    CheckoutButton = find_my_element(driver, "ID", CHECKOUT_BUTTON)
    check_not_found(driver, CheckoutButton, "Checkout Button button not found")
    CheckoutButton.click()

    # 🎉 Write Info 🎉
    # add first name
    FirstNameTB = find_my_element(driver, "ID", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTB, "First name textbox not found")
    FirstNameTB.send_keys("FirstName")
    time.sleep(1)
    # add last name
    LastNameTB = find_my_element(driver, "ID", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTB, "Last name textbox not found")
    LastNameTB.send_keys("LastName")
    time.sleep(1)
    # add email
    EmailTB = find_my_element(driver, "ID", EMAIL_TEXTBOX)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    EmailTB.send_keys("user@gmail.com")
    time.sleep(1)
    # Confirm email
    EmailTB = find_my_element(driver, "ID", CONFIRM_EMAIL)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    EmailTB.send_keys("user@gmail.com")
    time.sleep(1)
    # add number
    PhoneNumTB = find_my_element(driver, "ID", PHONE_TEXTBOX)
    check_not_found(driver, PhoneNumTB, "Phone number textbox not found")
    PhoneNumTB.send_keys("01221993665")
    time.sleep(1)
    # add gender
    GenderTB = find_my_element(driver, "XPATH", MALE_RADIO_BUTTON)
    check_not_found(driver, GenderTB, "Gender textbox not found")
    GenderTB.click()
    time.sleep(1)
    # check first checkbox
    Checkbox1 = find_my_element(driver, "ID", BE_INFORMED_CB)
    check_not_found(driver, Checkbox1, "Checkbox 1 not found")
    Checkbox1.click()
    time.sleep(1)
    # check second checkbox
    Checkbox2 = find_my_element(driver, "ID", SEND_EMAIL_CB)
    check_not_found(driver, Checkbox2, "Checkbox 2 not found")
    Checkbox2.click()
    time.sleep(1)
    # click register
    RegisterButton = find_my_element(driver, "ID", REGISTER_BUTTON)
    check_not_found(driver, RegisterButton, "Register button not found")
    RegisterButton.click()
    time.sleep(1)
    # check booking succeeded
    Booked = find_my_element(driver, "ID", "page--button")
    check_not_found(driver, Booked, "Booked successfully message not found")
    Booked.click()
    # check event page reached
    GetTicketButton = find_my_element(driver, "ID", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Event page not found")

    # check no more tickets available
    GetTicketButton = find_my_element(driver, "ID", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    driver.execute_script("arguments[0].scrollIntoView();", GetTicketButton)
    GetTicketButton.click()
    time.sleep(1)
    Alert = find_my_element(driver, "ID", "page--button")
    check_not_found(driver, Alert, "No tickets available alert not found")
    Alert.click()
    # check event page reached
    GetTicketButton = find_my_element(driver, "ID", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Event page not found")


# ? phsae 5
def booking_test(driver):
    # invalid_booking_test(driver)
    # timer_test(driver)
    valid_booking_test_1(driver)
    # valid_booking_test_2(driver)


# ? phase 5
def get_event_booking(driver):
    # Get list of elements
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
    Num = len(EventsList)
    if Num == 0:
        print("No events in the today list")
        exit()

    for i in range(1, ceil(Num / 12) + 1):
        for j in range(1, 13):
            time.sleep(1)
            EVENT = EVENT_NAME_1 + str(j) + EVENT_NAME_2
            Event = find_my_element(driver, "XPATH", EVENT)
            if Event != None:
                driver.execute_script("arguments[0].scrollIntoView();", Event)
                time.sleep(2)
                EventName = Event.text
                if "NightScape4" in EventName:
                    print(EventName)
                    driver.execute_script("arguments[0].click();", Event)
                    booking_test(driver)
                    print("Booking test passed")
                    driver.close()
                    exit()
            else:
                print("None")
                # break
        # check if more pages
        NextPageButton = find_my_element(driver, "ID", NEXT_PAGE_BUTTON)
        check_not_found(driver, NextPageButton, "Next page button not found")
        if NextPageButton.is_enabled():
            driver.execute_script("arguments[0].click();", NextPageButton)
