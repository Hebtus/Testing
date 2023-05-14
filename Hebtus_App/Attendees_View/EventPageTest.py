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
from selenium.common.exceptions import NoSuchElementException


def event_page(driver):
    sign_in_valid(driver, "hebtususer@gmail.com", "123456789")

    # events_info_test(driver)
    # Invalid
    # GetEvents(driver, 1)
    # Valid
    # GetEvents(driver, 2)
    time.sleep(30)
    # invalid_booking_test(driver)
    valid_booking_test(driver, "Neon NightScape11")
    # no_tickets_test(driver)


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


# ? phase 5
def invalid_booking_test(driver):
    # click on get ticket button
    GetTicketButton = find_my_element(driver, "XPATH", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    GetTicketButton.click()
    time.sleep(1)
    # ------------------ Invalid tests ---------------------
    # 1) Cick on book tickets wihtout choosing a ticket
    BookTicketButton = find_my_element(driver, "XPATH", BOOK_TICKET_BUTTON)
    check_not_found(driver, BookTicketButton, "Book ticket button not found")
    BookTicketButton.click()
    time.sleep(1)
    # Check alert message
    Alert = find_my_element(driver, "XPATH", CHOOSE_TICKET_ALERT)
    check_not_found(driver, Alert, "Alert message not found")
    # Close alert message
    CloseButton = find_my_element(driver, "XPATH", CLOSE_ALERT)
    check_not_found(driver, CloseButton, "Close alert message button not found")
    CloseButton.click()
    time.sleep(1)

    # 2) Click on minus button and make sure nothing changed
    MinusButton1 = find_my_element(driver, "XPATH", MINUS_BUTTON_1)
    check_not_found(driver, MinusButton1, "Minus button not found")
    MinusButton1.click()

    # Check if the number of tickets is still zero
    TicketInfo = find_my_element(driver, "XPATH", TICKET_TYPE_1)
    TicketsNum = int(TicketInfo.get_attribute("content-desc").split("\n")[1])
    assert TicketsNum == 0, "Tickets minus button test failed"
    print(TicketsNum)

    # 3) Click on plus button 6 times and make sure tickets number is updated to 5 only
    PlusButton1 = find_my_element(driver, "XPATH", PLUS_BUTTON_1)
    check_not_found(driver, PlusButton1, "Plus button not found")
    PlusButton1.click()
    PlusButton1.click()
    PlusButton1.click()
    PlusButton1.click()
    PlusButton1.click()
    PlusButton1.click()
    # Check if the number of tickets is still zero
    TicketInfo = find_my_element(driver, "XPATH", TICKET_TYPE_1)
    TicketsNum = int(TicketInfo.get_attribute("content-desc").split("\n")[1])
    assert TicketsNum == 5, "Tickets plus button test failed"
    print(TicketsNum)

    # 4) Click on back button
    TicketsType = find_my_element(driver, "XPATH", TICKETS_TYPES)
    check_not_found(driver, TicketsType, "Tickets type section not found")
    # click back button to return
    location = TicketsType.location
    # Get the X and Y coordinates of the top-left corner of the element
    x = location["x"]
    y = location["y"]
    # Create a TouchAction object
    action = TouchAction(driver)
    # Perform a tap at the specified position
    action.tap(x=x, y=y).perform()
    time.sleep(1)

    # click on stay button
    StayButton = find_my_element(driver, "XPATH", STAY_BUTTON)
    check_not_found(driver, StayButton, "Stay button not found")
    StayButton.click()
    time.sleep(1)

    # 5) Click on back button
    # Perform a tap at the specified position
    action.tap(x=x, y=y).perform()
    time.sleep(1)

    # click on leave button
    LeaveButton = find_my_element(driver, "XPATH", LEAVE_BUTTON)
    check_not_found(driver, LeaveButton, "Leave button not found")
    LeaveButton.click()
    time.sleep(1)
    # check event page is reached
    GetTicketButton = find_my_element(driver, "XPATH", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Events page not reached")
    GetTicketButton.click()
    time.sleep(1)
    invalid_tests_checkout_page(driver)


# ? phase 5
def invalid_tests_checkout_page(driver):
    # add 1 ticket
    PlusButton1 = find_my_element(driver, "XPATH", PLUS_BUTTON_1)
    check_not_found(driver, PlusButton1, "Plus button 1 not found")
    PlusButton1.click()
    # click book tickets button
    BookTicketButton = find_my_element(driver, "XPATH", BOOK_TICKET_BUTTON)
    check_not_found(driver, BookTicketButton, "Book ticket button not found")
    BookTicketButton.click()
    time.sleep(1)
    # * 1)
    # Check done button not enabled
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    assert not (DoneButton.is_enabled()), "Check done button enabled"
    # add first name
    FirstNameTB = find_my_element(driver, "XPATH", B_FIRST_NAME_TB)
    check_not_found(driver, FirstNameTB, "Last name textbox not found")
    FirstNameTB.click()
    time.sleep(1)
    FirstNameTB.send_keys("FirstName")
    time.sleep(1)
    driver.hide_keyboard()
    time.sleep(1)
    # Check done button not enabled
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    assert not (DoneButton.is_enabled()), "Check done button enabled"
    # add last name
    LastNameTB = find_my_element(driver, "XPATH", B_LAST_NAME_TB)
    check_not_found(driver, LastNameTB, "First name textbox not found")
    LastNameTB.click()
    time.sleep(1)
    LastNameTB.send_keys("LastName")
    time.sleep(1)
    driver.hide_keyboard()
    time.sleep(1)
    # Check done button not enabled
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    assert not (DoneButton.is_enabled()), "Check done button enabled"
    # add email
    EmailTB = find_my_element(driver, "XPATH", B_EMAIL_TB)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    EmailTB.click()
    time.sleep(1)
    EmailTB.send_keys("user@gmail.com")
    time.sleep(1)
    driver.hide_keyboard()
    time.sleep(1)
    # Check done button not enabled
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    assert not (DoneButton.is_enabled()), "Check done button enabled"
    # add phone number
    PhoneNumTB = find_my_element(driver, "XPATH", B_PHONE_NUM_TB)
    check_not_found(driver, PhoneNumTB, "Phone number textbox not found")
    PhoneNumTB.click()
    time.sleep(1)
    PhoneNumTB.send_keys("12345678974")
    time.sleep(1)
    driver.hide_keyboard()
    time.sleep(1)
    # Check done button not enabled
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    assert not (DoneButton.is_enabled()), "Check done button enabled"
    # add gender
    GenderTB = find_my_element(driver, "XPATH", B_GENDER_TB)
    check_not_found(driver, GenderTB, "Gender textbox not found")
    GenderTB.click()
    time.sleep(1)
    GenderTB.send_keys("Female")
    time.sleep(1)
    driver.hide_keyboard()
    time.sleep(1)
    # Check done button enabled
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    assert DoneButton.is_enabled(), "Check done button is not enabled"

    # * 2)
    # Invalid name: contains spaces
    FirstNameTB = find_my_element(driver, "XPATH", B_FIRST_NAME_TB)
    check_not_found(driver, FirstNameTB, "Last name textbox not found")
    FirstNameTB.click()
    time.sleep(1)
    FirstNameTB.set_text("")
    FirstNameTB.send_keys("First  Name")
    time.sleep(1)
    driver.hide_keyboard()
    time.sleep(1)
    # Click on done button
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    DoneButton.click()
    time.sleep(1)
    # Check alert message
    Alert = find_my_element(driver, "XPATH", ALERT_BACK_BUTTON)
    check_not_found(driver, Alert, "Alert message not found")
    Alert.click()
    # Correct name
    FirstNameTB = find_my_element(driver, "XPATH", B_FIRST_NAME_TB)
    check_not_found(driver, FirstNameTB, "Last name textbox not found")
    FirstNameTB.click()
    time.sleep(1)
    FirstNameTB.set_text("FirstName")
    time.sleep(1)
    driver.hide_keyboard()

    # Invalid email
    EmailTB = find_my_element(driver, "XPATH", B_EMAIL_TB)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    EmailTB.click()
    time.sleep(1)
    EmailTB.set_text("user")
    time.sleep(1)
    driver.hide_keyboard()
    time.sleep(1)
    # click done button
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    DoneButton.click()
    # Check alert message
    Alert = find_my_element(driver, "XPATH", ALERT_BACK_BUTTON)
    check_not_found(driver, Alert, "Alert message not found")
    Alert.click()
    # Correct email
    EmailTB = find_my_element(driver, "XPATH", B_EMAIL_TB)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    EmailTB.click()
    time.sleep(1)
    EmailTB.set_text("user@gmail.com")
    time.sleep(1)
    driver.hide_keyboard()
    time.sleep(1)
    # Invalid phone number: contain characters
    PhoneNumTB = find_my_element(driver, "XPATH", B_PHONE_NUM_TB)
    check_not_found(driver, PhoneNumTB, "Phone number textbox not found")
    PhoneNumTB.click()
    time.sleep(1)
    PhoneNumTB.set_text("number")
    time.sleep(1)
    driver.hide_keyboard()
    # click done button
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    DoneButton.click()
    time.sleep(1)
    # check alert message
    Alert = find_my_element(driver, "XPATH", ALERT_BACK_BUTTON)
    check_not_found(driver, Alert, "Alert message not found")
    Alert.click()
    # Invalid phone number: less than 11 digits
    PhoneNumTB = find_my_element(driver, "XPATH", B_PHONE_NUM_TB)
    check_not_found(driver, PhoneNumTB, "Phone number textbox not found")
    PhoneNumTB.click()
    time.sleep(1)
    PhoneNumTB.set_text("12345678")
    time.sleep(1)
    driver.hide_keyboard()
    # click done button
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    DoneButton.click()
    time.sleep(1)
    # check alert message
    Alert = find_my_element(driver, "XPATH", ALERT_BACK_BUTTON)
    check_not_found(driver, Alert, "Alert message not found")
    Alert.click()
    # correct number
    PhoneNumTB = find_my_element(driver, "XPATH", B_PHONE_NUM_TB)
    check_not_found(driver, PhoneNumTB, "Phone number textbox not found")
    PhoneNumTB.click()
    time.sleep(1)
    PhoneNumTB.set_text("12345678974")
    time.sleep(1)
    driver.hide_keyboard()

    # Invalid gender
    GenderTB = find_my_element(driver, "XPATH", B_GENDER_TB)
    check_not_found(driver, GenderTB, "Gender textbox not found")
    GenderTB.click()
    time.sleep(1)
    GenderTB.set_text("Gender")
    time.sleep(1)
    driver.hide_keyboard()
    # click done button
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    DoneButton.click()
    time.sleep(1)
    # check alert message
    Alert = find_my_element(driver, "XPATH", ALERT_BACK_BUTTON)
    check_not_found(driver, Alert, "Alert message not found")
    Alert.click()
    # correct gender
    GenderTB = find_my_element(driver, "XPATH", B_GENDER_TB)
    check_not_found(driver, GenderTB, "Gender textbox not found")
    GenderTB.click()
    time.sleep(1)
    GenderTB.set_text("Male")
    time.sleep(1)
    driver.hide_keyboard()

    # Invalid promocode
    PromocodeTB = find_my_element(driver, "XPATH", B_PROMOCODE_TB)
    check_not_found(driver, PromocodeTB, "Promocode textbox not found")
    PromocodeTB.click()
    time.sleep(1)
    PromocodeTB.send_keys("Promocode")
    time.sleep(1)
    driver.hide_keyboard()
    # click done button
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    DoneButton.click()
    time.sleep(1)
    # check alert message
    Alert = find_my_element(driver, "XPATH", ALERT_BACK_BUTTON)
    check_not_found(driver, Alert, "Alert message not found")
    Alert.click()
    # delete promocode
    PromocodeTB = find_my_element(driver, "XPATH", B_PROMOCODE_TB)
    check_not_found(driver, PromocodeTB, "Promocode textbox not found")
    PromocodeTB.click()
    time.sleep(1)
    PromocodeTB.set_text("")
    time.sleep(1)
    driver.hide_keyboard()
    # * 3)
    # click back button
    BackButton = find_my_element(driver, "XPATH", B_BACK_BUTTON)
    check_not_found(driver, BackButton, "Back button not found")
    BackButton.click()
    # click on stay button
    StayButton = find_my_element(driver, "XPATH", STAY_BUTTON)
    check_not_found(driver, StayButton, "Stay button not found")
    StayButton.click()
    time.sleep(1)
    # check checkout page reached
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Checkout page not reached")

    # # wait for 30 minutes
    # # Start the timer
    # start_time = time.time()
    # # Wait for the time limit reached alert to appear for up to 30 minutes
    # wait_time = 1800  # 30 minutes in seconds
    # wait = WebDriverWait(driver, wait_time)
    # Alert = wait.until(
    #     EC.presence_of_element_located((AppiumBy.XPATH, TIME_LIMIT_ALERT))
    # )
    # assert Alert != None, "Time limit reached alert not found"
    # # End the timer
    # end_time = time.time()
    # # Calculate the time taken to find the element
    # time_taken = end_time - start_time
    # print(time_taken)
    # assert 1500 < time_taken < 2000, "The timer ended in a wrong"
    # check_not_found(driver, Alert, "Time limit reached alert not found")
    # # go back to choose tickets page
    # Alert.click()
    # # check the choose tickets page is reached
    # BookTicketButton = find_my_element(driver, "XPATH", BOOK_TICKET_BUTTON)
    # check_not_found(driver, BookTicketButton, "Choose ticket page not reached")

    # click back button
    BackButton = find_my_element(driver, "XPATH", B_BACK_BUTTON)
    check_not_found(driver, BackButton, "Back button not found")
    BackButton.click()
    # click on stay button
    LeaveButton = find_my_element(driver, "XPATH", LEAVE_BUTTON)
    check_not_found(driver, LeaveButton, "Leave button not found")
    LeaveButton.click()
    time.sleep(1)
    # check the choose tickets page is reached
    BookTicketButton = find_my_element(driver, "XPATH", BOOK_TICKET_BUTTON)
    check_not_found(driver, BookTicketButton, "Choose ticket page not reached")


# ? phase 5
def valid_booking_test(driver, EventName):
    booking_test_1(driver, EventName)
    booking_test_2(driver, EventName)
    booking_test_3(driver, EventName)
    booking_test_4(driver, EventName)
    booking_test_5(driver, EventName)


# ? Phase 5
def booking_test_1(driver, EventName):
    # click on get ticket button
    GetTicketButton = find_my_element(driver, "XPATH", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    GetTicketButton.click()
    time.sleep(1)
    # 1) get 2 tickets of type 1
    PlusButton1 = find_my_element(driver, "XPATH", PLUS_BUTTON_1)
    check_not_found(driver, PlusButton1, "Plus button 1 not found")
    PlusButton1.click()
    PlusButton1.click()
    # get 1 ticket of type 2
    PlusButton2 = find_my_element(driver, "XPATH", PLUS_BUTTON_2)
    check_not_found(driver, PlusButton2, "Plus button 2 not found")
    PlusButton2.click()
    # click book tickets button
    BookTicketButton = find_my_element(driver, "XPATH", BOOK_TICKET_BUTTON)
    check_not_found(driver, BookTicketButton, "Book ticket button not found")
    BookTicketButton.click()
    time.sleep(1)

    # check order summary page
    SummaryButton = find_my_element(driver, "XPATH", B_SUMMARY_BUTTON)
    check_not_found(driver, SummaryButton, "Order Summary button not found")
    SummaryButton.click()
    time.sleep(1)
    # check that 2 tickets exist
    SummaryTicket1 = find_my_element(driver, "XPATH", SUMMARY_TICKET_1)
    check_not_found(driver, SummaryTicket1, "Ticket 1 info not found")
    Info1 = SummaryTicket1.get_attribute("content-desc")
    Info1 = Info1.split(" ")[0]
    print(Info1)
    assert int(Info1) == 2, "Tickets 1 info is incorrect"
    SummaryTicket2 = find_my_element(driver, "XPATH", SUMMARY_TICKET_2)
    check_not_found(driver, SummaryTicket2, "Ticket 2 info not found")
    Info2 = SummaryTicket2.get_attribute("content-desc")
    Info2 = Info2.split(" ")[0]
    print(Info2)
    assert int(Info2) == 1, "Tickets 2 info is incorrect"

    # click back button
    BackButton = find_my_element(driver, "XPATH", B_BACK_BUTTON)
    check_not_found(driver, BackButton, "Back button not found")
    BackButton.click()
    time.sleep(1)
    # click on stay button
    StayButton = find_my_element(driver, "XPATH", STAY_BUTTON)
    check_not_found(driver, StayButton, "Stay button not found")
    StayButton.click()
    time.sleep(1)

    # Add info
    # add first name
    FirstNameTB = find_my_element(driver, "XPATH", B_FIRST_NAME_TB)
    check_not_found(driver, FirstNameTB, "Last name textbox not found")
    FirstNameTB.click()
    time.sleep(1)
    FirstNameTB.send_keys("FirstName")
    time.sleep(1)
    driver.hide_keyboard()
    # add last name
    LastNameTB = find_my_element(driver, "XPATH", B_LAST_NAME_TB)
    check_not_found(driver, LastNameTB, "First name textbox not found")
    LastNameTB.click()
    time.sleep(1)
    LastNameTB.send_keys("LastName")
    time.sleep(1)
    driver.hide_keyboard()
    # add email
    EmailTB = find_my_element(driver, "XPATH", B_EMAIL_TB)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    EmailTB.click()
    time.sleep(1)
    EmailTB.send_keys("user@gmail.com")
    time.sleep(1)
    driver.hide_keyboard()
    # add phone number
    PhoneNumTB = find_my_element(driver, "XPATH", B_PHONE_NUM_TB)
    check_not_found(driver, PhoneNumTB, "Phone number textbox not found")
    PhoneNumTB.click()
    time.sleep(1)
    PhoneNumTB.send_keys("12345678974")
    time.sleep(1)
    driver.hide_keyboard()
    # add gender
    GenderTB = find_my_element(driver, "XPATH", B_GENDER_TB)
    check_not_found(driver, GenderTB, "Gender textbox not found")
    GenderTB.click()
    time.sleep(1)
    GenderTB.send_keys("Female")
    time.sleep(1)
    driver.hide_keyboard()
    # add promocode 1
    PromocodeTB = find_my_element(driver, "XPATH", B_PROMOCODE_TB)
    check_not_found(driver, PromocodeTB, "Promocode textbox not found")
    PromocodeTB.click()
    time.sleep(1)
    PromocodeTB.send_keys(EventName + " PromoCode1")
    time.sleep(1)
    driver.hide_keyboard()
    # click done button
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    DoneButton.click()
    time.sleep(1)
    # check if successfully booked
    Alert = find_my_element(driver, "XPATH", ALERT_BACK_BUTTON)
    check_not_found(driver, Alert, "Alert message not found")
    Alert.click()
    # go back events pages
    # click back button
    BackButton = find_my_element(driver, "XPATH", B_BACK_BUTTON)
    check_not_found(driver, BackButton, "Back button not found")
    BackButton.click()
    # click on leave button
    LeaveButton = find_my_element(driver, "XPATH", LEAVE_BUTTON)
    check_not_found(driver, LeaveButton, "Leave button not found")
    LeaveButton.click()
    time.sleep(1)
    # Click on back button
    TicketsType = find_my_element(driver, "XPATH", TICKETS_TYPES)
    check_not_found(driver, TicketsType, "Tickets type section not found")
    # click back button to return
    location = TicketsType.location
    # Get the X and Y coordinates of the top-left corner of the element
    x = location["x"]
    y = location["y"]
    # Create a TouchAction object
    action = TouchAction(driver)
    # Perform a tap at the specified position
    action.tap(x=x, y=y).perform()
    time.sleep(1)
    LeaveButton = find_my_element(driver, "XPATH", LEAVE_BUTTON)
    check_not_found(driver, LeaveButton, "Leave button not found")
    LeaveButton.click()
    time.sleep(1)
    # Check event page reached
    GetTicketButton = find_my_element(driver, "XPATH", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Events page not reached")


# ? Phase 5
def booking_test_2(driver, EventName):
    # click on get ticket button
    GetTicketButton = find_my_element(driver, "XPATH", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    GetTicketButton.click()
    time.sleep(1)

    # 2) get 4 tickets of type 2
    PlusButton2 = find_my_element(driver, "XPATH", PLUS_BUTTON_2)
    check_not_found(driver, PlusButton2, "Plus button 2 not found")
    PlusButton2.click()
    PlusButton2.click()
    PlusButton2.click()
    PlusButton2.click()
    # click book tickets button
    BookTicketButton = find_my_element(driver, "XPATH", BOOK_TICKET_BUTTON)
    check_not_found(driver, BookTicketButton, "Book ticket button not found")
    BookTicketButton.click()
    time.sleep(1)

    # Add info
    # add first name
    FirstNameTB = find_my_element(driver, "XPATH", B_FIRST_NAME_TB)
    check_not_found(driver, FirstNameTB, "Last name textbox not found")
    FirstNameTB.click()
    time.sleep(1)
    FirstNameTB.send_keys("FirstName")
    time.sleep(1)
    driver.hide_keyboard()
    # add last name
    LastNameTB = find_my_element(driver, "XPATH", B_LAST_NAME_TB)
    check_not_found(driver, LastNameTB, "First name textbox not found")
    LastNameTB.click()
    time.sleep(1)
    LastNameTB.send_keys("LastName")
    time.sleep(1)
    driver.hide_keyboard()
    # add email
    EmailTB = find_my_element(driver, "XPATH", B_EMAIL_TB)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    EmailTB.click()
    time.sleep(1)
    EmailTB.send_keys("user@gmail.com")
    time.sleep(1)
    driver.hide_keyboard()
    # add phone number
    PhoneNumTB = find_my_element(driver, "XPATH", B_PHONE_NUM_TB)
    check_not_found(driver, PhoneNumTB, "Phone number textbox not found")
    PhoneNumTB.click()
    time.sleep(1)
    PhoneNumTB.send_keys("12345678974")
    time.sleep(1)
    driver.hide_keyboard()
    # add gender
    GenderTB = find_my_element(driver, "XPATH", B_GENDER_TB)
    check_not_found(driver, GenderTB, "Gender textbox not found")
    GenderTB.click()
    time.sleep(1)
    GenderTB.send_keys("Male")
    time.sleep(1)
    driver.hide_keyboard()
    # add promocode 2
    PromocodeTB = find_my_element(driver, "XPATH", B_PROMOCODE_TB)
    check_not_found(driver, PromocodeTB, "Promocode textbox not found")
    PromocodeTB.click()
    time.sleep(1)
    PromocodeTB.send_keys(EventName + " PromoCode2")
    time.sleep(1)
    driver.hide_keyboard()
    # click done button
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    DoneButton.click()
    time.sleep(1)
    # check if successfully booked
    Alert = find_my_element(driver, "XPATH", ALERT_BACK_BUTTON)
    check_not_found(driver, Alert, "Alert message not found")
    Alert.click()
    # go back events pages
    # click back button
    BackButton = find_my_element(driver, "XPATH", B_BACK_BUTTON)
    check_not_found(driver, BackButton, "Back button not found")
    BackButton.click()
    # click on leave button
    LeaveButton = find_my_element(driver, "XPATH", LEAVE_BUTTON)
    check_not_found(driver, LeaveButton, "Leave button not found")
    LeaveButton.click()
    time.sleep(1)
    # Click on back button
    TicketsType = find_my_element(driver, "XPATH", TICKETS_TYPES)
    check_not_found(driver, TicketsType, "Tickets type section not found")
    # click back button to return
    location = TicketsType.location
    # Get the X and Y coordinates of the top-left corner of the element
    x = location["x"]
    y = location["y"]
    # Create a TouchAction object
    action = TouchAction(driver)
    # Perform a tap at the specified position
    action.tap(x=x, y=y).perform()
    time.sleep(1)
    LeaveButton = find_my_element(driver, "XPATH", LEAVE_BUTTON)
    check_not_found(driver, LeaveButton, "Leave button not found")
    LeaveButton.click()
    time.sleep(1)
    # Check event page reached
    GetTicketButton = find_my_element(driver, "XPATH", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Events page not reached")


# ? Phase 5
def booking_test_3(driver, EventName):
    # add promocode 1

    # click on get ticket button
    GetTicketButton = find_my_element(driver, "XPATH", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    GetTicketButton.click()
    time.sleep(1)
    # 3) get 1 ticket of type 1
    PlusButton1 = find_my_element(driver, "XPATH", PLUS_BUTTON_1)
    check_not_found(driver, PlusButton1, "Plus button 1 not found")
    PlusButton1.click()
    # ticket of type 2 should not be visibile

    # try:
    #     element = driver.find_element(AppiumBy.XPATH, PLUS_BUTTON_2)
    #     print("Ticket type 2 is visible after its capacity limit is reached")
    # except:
    #     print("Tickets type 2 is not visibility visible after its capacity limit is reached")

    BookTicketButton = find_my_element(driver, "XPATH", BOOK_TICKET_BUTTON)
    check_not_found(driver, BookTicketButton, "Book ticket button not found")
    BookTicketButton.click()
    time.sleep(1)

    # check order summary page
    SummaryButton = find_my_element(driver, "XPATH", B_SUMMARY_BUTTON)
    check_not_found(driver, SummaryButton, "Order Summary button not found")
    SummaryButton.click()
    time.sleep(1)
    # check that 2 tickets exist
    SummaryTicket1 = find_my_element(driver, "XPATH", SUMMARY_TICKET_1)
    check_not_found(driver, SummaryTicket1, "Ticket 1 info not found")
    Info1 = SummaryTicket1.get_attribute("content-desc")
    Info1 = Info1.split(" ")[0]
    print(Info1)
    assert int(Info1) == 1, "Tickets info is incorrect"

    # click back button
    BackButton = find_my_element(driver, "XPATH", B_BACK_BUTTON)
    check_not_found(driver, BackButton, "Back button not found")
    BackButton.click()
    time.sleep(1)
    # click on stay button
    StayButton = find_my_element(driver, "XPATH", STAY_BUTTON)
    check_not_found(driver, StayButton, "Stay button not found")
    StayButton.click()
    time.sleep(1)

    # Add info
    # add first name
    FirstNameTB = find_my_element(driver, "XPATH", B_FIRST_NAME_TB)
    check_not_found(driver, FirstNameTB, "Last name textbox not found")
    FirstNameTB.click()
    time.sleep(1)
    FirstNameTB.send_keys("FirstName")
    time.sleep(1)
    driver.hide_keyboard()
    # add last name
    LastNameTB = find_my_element(driver, "XPATH", B_LAST_NAME_TB)
    check_not_found(driver, LastNameTB, "First name textbox not found")
    LastNameTB.click()
    time.sleep(1)
    LastNameTB.send_keys("LastName")
    time.sleep(1)
    driver.hide_keyboard()
    # add email
    EmailTB = find_my_element(driver, "XPATH", B_EMAIL_TB)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    EmailTB.click()
    time.sleep(1)
    EmailTB.send_keys("user@gmail.com")
    time.sleep(1)
    driver.hide_keyboard()
    # add phone number
    PhoneNumTB = find_my_element(driver, "XPATH", B_PHONE_NUM_TB)
    check_not_found(driver, PhoneNumTB, "Phone number textbox not found")
    PhoneNumTB.click()
    time.sleep(1)
    PhoneNumTB.send_keys("12345678974")
    time.sleep(1)
    driver.hide_keyboard()
    # add gender
    GenderTB = find_my_element(driver, "XPATH", B_GENDER_TB)
    check_not_found(driver, GenderTB, "Gender textbox not found")
    GenderTB.click()
    time.sleep(1)
    GenderTB.send_keys("Female")
    time.sleep(1)
    driver.hide_keyboard()
    # add promocode 1
    PromocodeTB = find_my_element(driver, "XPATH", B_PROMOCODE_TB)
    check_not_found(driver, PromocodeTB, "Promocode textbox not found")
    PromocodeTB.click()
    time.sleep(1)
    PromocodeTB.send_keys(EventName + " PromoCode1")
    time.sleep(1)
    driver.hide_keyboard()
    # click done button
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    DoneButton.click()
    time.sleep(1)
    # check if successfully booked
    Alert = find_my_element(driver, "XPATH", ALERT_BACK_BUTTON)
    check_not_found(driver, Alert, "Alert message not found")
    Alert.click()
    # go back events pages
    # click back button
    BackButton = find_my_element(driver, "XPATH", B_BACK_BUTTON)
    check_not_found(driver, BackButton, "Back button not found")
    BackButton.click()
    # click on leave button
    LeaveButton = find_my_element(driver, "XPATH", LEAVE_BUTTON)
    check_not_found(driver, LeaveButton, "Leave button not found")
    LeaveButton.click()
    time.sleep(1)
    # Click on back button
    TicketsType = find_my_element(driver, "XPATH", TICKETS_TYPES)
    check_not_found(driver, TicketsType, "Tickets type section not found")
    # click back button to return
    location = TicketsType.location
    # Get the X and Y coordinates of the top-left corner of the element
    x = location["x"]
    y = location["y"]
    # Create a TouchAction object
    action = TouchAction(driver)
    # Perform a tap at the specified position
    action.tap(x=x, y=y).perform()
    time.sleep(1)
    LeaveButton = find_my_element(driver, "XPATH", LEAVE_BUTTON)
    check_not_found(driver, LeaveButton, "Leave button not found")
    LeaveButton.click()
    time.sleep(1)
    # Check event page reached
    GetTicketButton = find_my_element(driver, "XPATH", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Events page not reached")


# ? Phase 5
def booking_test_4(driver, EventName):
    # click on get ticket button
    GetTicketButton = find_my_element(driver, "XPATH", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    GetTicketButton.click()
    time.sleep(1)
    # 4) get 1 ticket of type 1
    PlusButton1 = find_my_element(driver, "XPATH", PLUS_BUTTON_1)
    check_not_found(driver, PlusButton1, "Plus button 1 not found")
    PlusButton1.click()
    # click book tickets button
    BookTicketButton = find_my_element(driver, "XPATH", BOOK_TICKET_BUTTON)
    check_not_found(driver, BookTicketButton, "Book ticket button not found")
    BookTicketButton.click()
    time.sleep(1)
    # Add info
    # add first name
    FirstNameTB = find_my_element(driver, "XPATH", B_FIRST_NAME_TB)
    check_not_found(driver, FirstNameTB, "Last name textbox not found")
    FirstNameTB.click()
    time.sleep(1)
    FirstNameTB.send_keys("FirstName")
    time.sleep(1)
    driver.hide_keyboard()
    # add last name
    LastNameTB = find_my_element(driver, "XPATH", B_LAST_NAME_TB)
    check_not_found(driver, LastNameTB, "First name textbox not found")
    LastNameTB.click()
    time.sleep(1)
    LastNameTB.send_keys("LastName")
    time.sleep(1)
    driver.hide_keyboard()
    # add email
    EmailTB = find_my_element(driver, "XPATH", B_EMAIL_TB)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    EmailTB.click()
    time.sleep(1)
    EmailTB.send_keys("user@gmail.com")
    time.sleep(1)
    driver.hide_keyboard()
    # add phone number
    PhoneNumTB = find_my_element(driver, "XPATH", B_PHONE_NUM_TB)
    check_not_found(driver, PhoneNumTB, "Phone number textbox not found")
    PhoneNumTB.click()
    time.sleep(1)
    PhoneNumTB.send_keys("12345678974")
    time.sleep(1)
    driver.hide_keyboard()
    # add gender
    GenderTB = find_my_element(driver, "XPATH", B_GENDER_TB)
    check_not_found(driver, GenderTB, "Gender textbox not found")
    GenderTB.click()
    time.sleep(1)
    GenderTB.send_keys("Female")
    time.sleep(1)
    driver.hide_keyboard()
    # add promocode 1
    PromocodeTB = find_my_element(driver, "XPATH", B_PROMOCODE_TB)
    check_not_found(driver, PromocodeTB, "Promocode textbox not found")
    PromocodeTB.click()
    time.sleep(1)
    PromocodeTB.send_keys(EventName + " PromoCode1")
    time.sleep(1)
    driver.hide_keyboard()
    # click done button
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    DoneButton.click()
    time.sleep(1)
    # check if successfully booked
    Alert = find_my_element(driver, "XPATH", ALERT_BACK_BUTTON)
    check_not_found(driver, Alert, "Alert message not found")
    Alert.click()
    # go back events pages
    # click back button
    BackButton = find_my_element(driver, "XPATH", B_BACK_BUTTON)
    check_not_found(driver, BackButton, "Back button not found")
    BackButton.click()
    # click on leave button
    LeaveButton = find_my_element(driver, "XPATH", LEAVE_BUTTON)
    check_not_found(driver, LeaveButton, "Leave button not found")
    LeaveButton.click()
    time.sleep(1)
    # Check event page reached
    # Click on back button
    TicketsType = find_my_element(driver, "XPATH", TICKETS_TYPES)
    check_not_found(driver, TicketsType, "Tickets type section not found")
    # click back button to return
    location = TicketsType.location
    # Get the X and Y coordinates of the top-left corner of the element
    x = location["x"]
    y = location["y"]
    # Create a TouchAction object
    action = TouchAction(driver)
    # Perform a tap at the specified position
    action.tap(x=x, y=y).perform()
    time.sleep(1)
    LeaveButton = find_my_element(driver, "XPATH", LEAVE_BUTTON)
    check_not_found(driver, LeaveButton, "Leave button not found")
    LeaveButton.click()
    time.sleep(1)
    GetTicketButton = find_my_element(driver, "XPATH", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Events page not reached")


# ? Phase 5
def booking_test_5(driver, EventName):
    # go back and check that there are no more tcikets available for this event

    # click on get ticket button
    GetTicketButton = find_my_element(driver, "XPATH", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    GetTicketButton.click()
    time.sleep(1)
    # 5) get 1 ticket of type 1
    PlusButton1 = find_my_element(driver, "XPATH", PLUS_BUTTON_1)
    check_not_found(driver, PlusButton1, "Plus button 1 not found")
    PlusButton1.click()
    # click book tickets button
    BookTicketButton = find_my_element(driver, "XPATH", BOOK_TICKET_BUTTON)
    check_not_found(driver, BookTicketButton, "Book ticket button not found")
    BookTicketButton.click()
    time.sleep(1)

    # Add info
    # add first name
    FirstNameTB = find_my_element(driver, "XPATH", B_FIRST_NAME_TB)
    check_not_found(driver, FirstNameTB, "Last name textbox not found")
    FirstNameTB.click()
    time.sleep(1)
    FirstNameTB.send_keys("FirstName")
    time.sleep(1)
    driver.hide_keyboard()
    # add last name
    LastNameTB = find_my_element(driver, "XPATH", B_LAST_NAME_TB)
    check_not_found(driver, LastNameTB, "First name textbox not found")
    LastNameTB.click()
    time.sleep(1)
    LastNameTB.send_keys("LastName")
    time.sleep(1)
    driver.hide_keyboard()
    # add email
    EmailTB = find_my_element(driver, "XPATH", B_EMAIL_TB)
    check_not_found(driver, LastNameTB, "Email textbox not found")
    EmailTB.click()
    time.sleep(1)
    EmailTB.send_keys("user@gmail.com")
    time.sleep(1)
    driver.hide_keyboard()
    # add phone number
    PhoneNumTB = find_my_element(driver, "XPATH", B_PHONE_NUM_TB)
    check_not_found(driver, PhoneNumTB, "Phone number textbox not found")
    PhoneNumTB.click()
    time.sleep(1)
    PhoneNumTB.send_keys("12345678974")
    time.sleep(1)
    driver.hide_keyboard()
    # add gender
    GenderTB = find_my_element(driver, "XPATH", B_GENDER_TB)
    check_not_found(driver, GenderTB, "Gender textbox not found")
    GenderTB.click()
    time.sleep(1)
    GenderTB.send_keys("Female")
    time.sleep(1)
    driver.hide_keyboard()
    # add promocode 1 (invalid)
    PromocodeTB = find_my_element(driver, "XPATH", B_PROMOCODE_TB)
    check_not_found(driver, PromocodeTB, "Promocode textbox not found")
    PromocodeTB.click()
    time.sleep(1)
    PromocodeTB.send_keys(EventName + " PromoCode1")
    time.sleep(1)
    driver.hide_keyboard()
    # click done button
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    DoneButton.click()
    time.sleep(1)
    # check alert message
    Alert = find_my_element(driver, "XPATH", ALERT_BACK_BUTTON)
    check_not_found(driver, Alert, "Alert message not found")
    Alert.click()
    # delete promocode
    PromocodeTB = find_my_element(driver, "XPATH", B_PROMOCODE_TB)
    check_not_found(driver, PromocodeTB, "Promocode textbox not found")
    PromocodeTB.click()
    time.sleep(1)
    PromocodeTB.set_text("")
    time.sleep(1)
    driver.hide_keyboard()
    # click done button
    DoneButton = find_my_element(driver, "XPATH", B_DONE_BUTTON)
    check_not_found(driver, DoneButton, "Check done button not found")
    DoneButton.click()
    time.sleep(1)

    # check if successfully booked
    Alert = find_my_element(driver, "XPATH", ALERT_BACK_BUTTON)
    check_not_found(driver, Alert, "Alert message not found")
    Alert.click()
    # go back events pages
    # click back button
    BackButton = find_my_element(driver, "XPATH", B_BACK_BUTTON)
    check_not_found(driver, BackButton, "Back button not found")
    BackButton.click()
    # click on leave button
    LeaveButton = find_my_element(driver, "XPATH", LEAVE_BUTTON)
    check_not_found(driver, LeaveButton, "Leave button not found")
    LeaveButton.click()
    time.sleep(1)
    # Click on back button
    TicketsType = find_my_element(driver, "XPATH", TICKETS_TYPES)
    check_not_found(driver, TicketsType, "Tickets type section not found")
    # click back button to return
    location = TicketsType.location
    # Get the X and Y coordinates of the top-left corner of the element
    x = location["x"]
    y = location["y"]
    # Create a TouchAction object
    action = TouchAction(driver)
    # Perform a tap at the specified position
    action.tap(x=x, y=y).perform()
    time.sleep(1)
    LeaveButton = find_my_element(driver, "XPATH", LEAVE_BUTTON)
    check_not_found(driver, LeaveButton, "Leave button not found")
    LeaveButton.click()
    time.sleep(1)
    # check if event page is reached
    GetTicketButton = find_my_element(driver, "XPATH", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Events page not reached")

    # check that there is no more tickets avaialable
    # Click on home page
    HomeButton = find_my_element(driver, "XPATH", HEBTUS_BUTTON)
    check_not_found(driver, HomeButton, "Hebtus home button not found")
    HomeButton.click()
    time.sleep(2)
    GetEvents(driver, 3)


# ? Phase 5
def no_tickets_test(driver):
    NoTickets = find_my_element(driver, "XPATH", NO_TICKETS)
    check_not_found(driver, NoTickets, "No tickets avaialbe is not")


# ? Phase 5
def GetEvents(driver, choice):
    # Get the screen dimensions
    screen_width = driver.get_window_size()["width"]
    screen_height = driver.get_window_size()["height"]
    ContentSet = set()
    old_page_source = None
    end = False
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
        count = 6
        for i in range(count):
            EVENT = EVENT_1 + str(i) + EVENT_2
            Event = find_my_element(driver, "XPATH", EVENT)
            check_not_found(driver, Event, "Event Not Found")
            time.sleep(2)
            EventInfo = Event.get_attribute("content-desc").split("\n")
            EventName = EventInfo[0]
            if "NightScape4" in EventName:
                print(EventName)
                Event.click()
                if choice == 1:
                    invalid_booking_test(driver)
                elif choice == 2:
                    valid_booking_test(driver, EventName)
                elif choice == 3:
                    no_tickets_test(driver)
                end = True
                break
        if (
            old_page_source is not None and driver.page_source == old_page_source
        ) or end:
            break
        old_page_source = driver.page_source

    print("Booking Test Passed")
    time.sleep(2)
    driver.quit()


# * Phase 4
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
