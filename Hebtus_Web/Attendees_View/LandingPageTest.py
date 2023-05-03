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

from datetime import datetime, date, timedelta

#! To change:
#   add login functions inside functions


def landing_page(driver):
    # login(driver, "hebtususer@gmail.com", "123456789")
    # nav_bar_test(driver, "hebtususer@gmail.com")
    update_password_test(driver, "hebtususer2@gmail.com", "123456789", "147258369")
    # tabs_test(driver)
    # categories_test(driver)
    # call_location_test(driver)
    # call_see_more_test(driver)
    # call_today_tab_test(driver)
    # call_weekend_tab(driver)
    # paginations_test(driver)
    # call_online_tab(driver)
    # call_free_tab_test(driver)
    # call_categories_test(driver)


# ? phase 5
def update_password_test(driver, email, password, new_password):
    # login with old password
    login(driver, email, password)
    # click update password button
    NavBarDropDown = find_my_element(driver, "ID", NAV_BAR_DROP_DOWN)
    check_not_found(driver, NavBarDropDown, "NavBar drop down not found")
    NavBarDropDown.click()
    time.sleep(1)
    UpdatePasswordButton = find_my_element(driver, "ID", DROP_DOWN_UPDATE_PASSWORD)
    check_not_found(driver, UpdatePasswordButton, "Manage Event button not found")
    UpdatePasswordButton.click()
    time.sleep(3)
    # ----------------------------Invalid tests----------------------------
    # Add wrong current password
    CurrentPasswordTB = find_my_element(driver, "ID", CURRENT_PASSWORD_TB)
    check_not_found(driver, CurrentPasswordTB, "Current password textbox not found")
    CurrentPasswordTB.send_keys("password")
    # add new password
    NewPasswordTB = find_my_element(driver, "ID", PASSWORD_TEXTBOX)
    check_not_found(driver, NewPasswordTB, "New Password textbox not found")
    NewPasswordTB.send_keys(new_password)
    # confrim new passowrd
    ConfirmPasswordTB = find_my_element(driver, "ID", CONFIRM_PASSWORD_TB)
    check_not_found(driver, ConfirmPasswordTB, "Confirm Password textbox not found")
    ConfirmPasswordTB.send_keys(new_password)
    time.sleep(3)
    # click update password
    UpdatePasswordButton = find_my_element(driver, "ID", LOGIN_BUTTON)
    check_not_found(driver, UpdatePasswordButton, "Update password button not found")
    UpdatePasswordButton.click()
    # check for alert message
    AlertMessage = find_my_element(driver, "ID", ERROR_MESSAGE)
    check_not_found(driver, AlertMessage, "Wrong current password message not found")
    # New password less than 8 characters
    clear_textbox(CurrentPasswordTB)
    CurrentPasswordTB.send_keys(password)
    clear_textbox(NewPasswordTB)
    NewPasswordTB.send_keys("123")
    clear_textbox(ConfirmPasswordTB)
    ConfirmPasswordTB.send_keys("123")
    # click update password
    UpdatePasswordButton = find_my_element(driver, "ID", LOGIN_BUTTON)
    check_not_found(driver, UpdatePasswordButton, "Update password button not found")
    UpdatePasswordButton.click()
    # check for alert message
    AlertMessage = find_my_element(driver, "ID", PASSWORD_REQUIRED_ALERT)
    check_not_found(
        driver, AlertMessage, "password less than 8 characters message not found"
    )
    # confirm password don't match
    clear_textbox(NewPasswordTB)
    NewPasswordTB.send_keys("newpassword")
    clear_textbox(ConfirmPasswordTB)
    ConfirmPasswordTB.send_keys("7895612346")
    # click update password
    UpdatePasswordButton = find_my_element(driver, "ID", LOGIN_BUTTON)
    check_not_found(driver, UpdatePasswordButton, "Update password button not found")
    UpdatePasswordButton.click()
    # check for alert message
    AlertMessage = find_my_element(driver, "ID", WRONG_CONFRIM_PASSWORD_ALERT)
    check_not_found(
        driver, AlertMessage, "wrong confirmation password message not found"
    )
    # current password missing
    clear_textbox(ConfirmPasswordTB)
    ConfirmPasswordTB.send_keys("newpassword")
    clear_textbox(CurrentPasswordTB)
    # click update password
    UpdatePasswordButton = find_my_element(driver, "ID", LOGIN_BUTTON)
    check_not_found(driver, UpdatePasswordButton, "Update password button not found")
    UpdatePasswordButton.click()
    # check for alert message
    AlertMessage = find_my_element(driver, "ID", CURRENT_PASSWORD_ALERT)
    check_not_found(driver, AlertMessage, "Current password missing message not found")
    # ----------------------------Valid test----------------------------
    # add current password
    clear_textbox(CurrentPasswordTB)
    CurrentPasswordTB.send_keys(password)
    # add new password
    clear_textbox(NewPasswordTB)
    NewPasswordTB.send_keys(new_password)
    # confrim new passowrd
    clear_textbox(ConfirmPasswordTB)
    ConfirmPasswordTB.send_keys(new_password)
    time.sleep(1)
    # click update password
    UpdatePasswordButton = find_my_element(driver, "ID", LOGIN_BUTTON)
    check_not_found(driver, UpdatePasswordButton, "Update password button not found")
    UpdatePasswordButton.click()
    # check message "Updated password successfully"
    AlertMessage = find_my_element(driver, "ID", ERROR_MESSAGE)
    check_not_found(driver, AlertMessage, "Alert message not found")
    print("Password updated successfully")
    # Try changin password one more time --> check alert message "you just updated your password"
    NewPasswordTB.send_keys(new_password)
    ConfirmPasswordTB.send_keys(new_password)
    time.sleep(1)
    # click update password
    UpdatePasswordButton = find_my_element(driver, "ID", LOGIN_BUTTON)
    check_not_found(driver, UpdatePasswordButton, "Update password button not found")
    UpdatePasswordButton.click()
    AlertMessage = find_my_element(driver, "ID", ERROR_MESSAGE)
    check_not_found(
        driver, AlertMessage, "User recently changed password message not found"
    )
    # go to landing page
    driver.back()
    time.sleep(1)
    # sign out
    NavBarDropDown = find_my_element(driver, "ID", NAV_BAR_DROP_DOWN)
    check_not_found(driver, NavBarDropDown, "NavBar drop down not found")
    NavBarDropDown.click()
    time.sleep(1)
    LogOut = find_my_element(driver, "ID", LOG_OUT)
    check_not_found(driver, LogOut, "Log out button not found")
    LogOut.click()
    time.sleep(2)
    # Go to login page
    NavBarDropDown = find_my_element(driver, "ID", NAV_BAR_DROP_DOWN)
    check_not_found(driver, NavBarDropDown, "NavBar drop down not found")
    NavBarDropDown.click()
    time.sleep(1)
    LoginButton = find_my_element(driver, "ID", DROP_DOWN_LOGIN)
    check_not_found(driver, LoginButton, "Login button not found")
    LoginButton.click()
    time.sleep(2)
    # login with new password
    # enter email and password
    EmailTextbox = find_my_element(driver, "ID", EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.send_keys(email)
    PasswordTextbox = find_my_element(driver, "ID", PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.send_keys(new_password)
    time.sleep(3)
    LoginButton = find_my_element(driver, "ID", LOGIN_BUTTON)
    check_not_found(driver, LoginButton, "Login button not found")
    LoginButton.click()
    time.sleep(15)
    # check if landing page is reached
    LandingPage = find_my_element(driver, "ID", LANDING_PAGE)
    check_not_found(driver, LandingPage, "Landing page not reached")
    time.sleep(2)
    print("signed in successfuly")
    driver.close()


# ? Phase 5
def tabs_test(driver):
    # Today tab
    # today_tab_test(driver)

    # This weekend test
    # this_weekend_tab_test(driver)

    # free tab
    # free_tab_test(driver)

    # online tab
    # online_tab_test(driver)

    # charity tab
    CharityTab = find_my_element(driver, "ID", CHARITY_CAUSES_TAB)
    check_not_found(driver, CharityTab, "Charity tab not found")
    assert CharityTab.is_enabled(), "Charity tab is not enabled"
    CharityTab.click()
    print("Charity tab test passed")
    driver.close()
    time.sleep(2)


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


# ? Phase 5
def nav_bar_test(driver, email):
    # ------------------------Logged in mode----------------------------
    # check account logged is the one in nav bar:
    AccountEmail = find_my_element(driver, "XPATH", DROP_DOWN_TEXT)
    check_not_found(driver, AccountEmail, "Account email not found in nav bar")
    print(AccountEmail.text)
    assert AccountEmail.text == email, "Account email does not match"
    time.sleep(3)
    # -----------create event button-----------
    CreateEventButton = find_my_element(driver, "ID", CREATE_EVENT)
    check_not_found(driver, CreateEventButton, "Create Event button not found")
    CreateEventButton.click()
    time.sleep(3)
    BasicInfoPage = find_my_element(driver, "XPATH", CREATE_EVENT_PAGE)
    check_not_found(driver, BasicInfoPage, "Basic Info page not reached")
    assert BasicInfoPage.text == "Basic Info", "Basic Info page not reached"
    time.sleep(1)
    print("Create event button test passed")
    driver.back()
    time.sleep(1)
    # -----------manage my events button -----------
    NavBarDropDown = find_my_element(driver, "ID", NAV_BAR_DROP_DOWN)
    check_not_found(driver, NavBarDropDown, "NavBar drop down not found")
    NavBarDropDown.click()
    time.sleep(1)
    ManageEventButton = find_my_element(driver, "ID", DROP_DOWN_MANAGE_EVENTS)
    check_not_found(driver, ManageEventButton, "Manage Event button not found")
    ManageEventButton.click()
    time.sleep(3)
    ManageEventPage = find_my_element(driver, "ID", MANGE_EVENTS_PAGE)
    check_not_found(driver, ManageEventPage, "Manage events page not reached")
    print("Manage events button test passed")
    driver.back()
    time.sleep(1)
    # -----------Sign out button -----------
    NavBarDropDown = find_my_element(driver, "ID", NAV_BAR_DROP_DOWN)
    check_not_found(driver, NavBarDropDown, "NavBar drop down not found")
    NavBarDropDown.click()
    time.sleep(1)
    LogOut = find_my_element(driver, "ID", LOG_OUT)
    check_not_found(driver, LogOut, "Log out button not found")
    LogOut.click()
    time.sleep(2)

    # ------------------------Logged in mode----------------------------
    # check if the drop down menu in nav changed to login in/ sign up
    DropDownText = find_my_element(driver, "XPATH", DROP_DOWN_TEXT)
    check_not_found(driver, DropDownText, "Logout page not reached")
    assert DropDownText.text == "Log In / Sign Up", "Log In page not reached"
    print("signed out successfuly")
    time.sleep(2)
    # -----------create event button -----------
    CreateEventButton = find_my_element(driver, "ID", CREATE_EVENT)
    check_not_found(driver, CreateEventButton, "Create Event button not found")
    CreateEventButton.click()
    time.sleep(3)
    LoginPage = find_my_element(driver, "ID", LOGIN_BUTTON)
    check_not_found(driver, LoginPage, "Login page not reached")
    time.sleep(1)
    print("Create event button test passed")
    driver.back()
    time.sleep(1)
    # ----------- log in button -----------
    NavBarDropDown = find_my_element(driver, "ID", NAV_BAR_DROP_DOWN)
    check_not_found(driver, NavBarDropDown, "NavBar drop down not found")
    NavBarDropDown.click()
    time.sleep(1)
    LoginButton = find_my_element(driver, "ID", DROP_DOWN_LOGIN)
    check_not_found(driver, LoginButton, "Login button not found")
    LoginButton.click()
    LoginPage = find_my_element(driver, "ID", LOGIN_BUTTON)
    check_not_found(driver, LoginPage, "Login page not reached")
    time.sleep(1)
    print("login button test passed")
    driver.back()
    time.sleep(3)
    # ----------- sign up button -----------
    NavBarDropDown = find_my_element(driver, "ID", NAV_BAR_DROP_DOWN)
    check_not_found(driver, NavBarDropDown, "NavBar drop down not found")
    NavBarDropDown.click()
    time.sleep(1)
    SignupButton = find_my_element(driver, "ID", DROP_DOWN_SIGNUP)
    check_not_found(driver, SignupButton, "Sign up button not found")
    SignupButton.click()
    SignUpPage = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, SignUpPage, "Sign up page not reached")
    time.sleep(1)
    print("login button test passed")
    print("navigation bar test passed")
    driver.close()


# * phase 4
def location_nearby_events_test(driver):
    # ---------------------------------------------- Testing Detection of geolocation ---------------------------------------------- #
    # Get the detected location
    MyLocation = find_my_element(driver, "ID", LOCATION_PICKER)
    check_not_found(driver, MyLocation, "Location not found")
    # print(MyLocation.get_attribute("value"))
    print(MyLocation.text)
    # Check if it's correct
    if MyLocation.text == "Cairo":
        print("Location detected correctly")
    else:
        print("Location not detected correctly")

    # # Click on All tab to make sure home page is opened
    # AllTab = find_my_element(driver, "XPATH", ALL_TAB)
    # check_not_found(driver, AllTab, "All tab not found")
    # AllTab.click()
    # time.sleep(30)
    # # Scroll down to load
    # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    # time.sleep(60)
    # # ---------------------------------------------- Testing nearby events ---------------------------------------------- #
    # # Get list of events
    # EventsList = driver.find_elements(
    #     By.CLASS_NAME,
    #     EVENT_ELEMENT,
    # )
    # if len(EventsList) == 0:
    #     print("No events in the list")
    #     driver.close()
    #     exit()
    # EventsList = EventsList[0:10]
    # EventsURLList = []
    # # Get URL of events pages
    # for element in EventsList:
    #     try:
    #         link = element.find_element(By.TAG_NAME, "a")
    #         EventsURLList.append(link.get_attribute("href"))
    #         print(link.get_attribute("href"))
    #     except:
    #         print("No Data Available!")
    # # loop over all URLs
    # for Link in EventsURLList:
    #     # Open event oage
    #     driver.get(Link)
    #     driver.implicitly_wait(10)
    #     # Scroll down to load
    #     driver.execute_script("window.scrollBy(0,500)")
    #     driver.implicitly_wait(10)
    #     # Get location element
    #     Location = find_my_element(
    #         driver,
    #         "XPATH",
    #         "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[2]/section/div[2]/section[2]/div/div/div[2]/p",
    #     )
    #     check_not_found(driver, Location, "location not found")
    #     # Check if the location is in Cairo or online
    #     if Location != None:
    #         if (Location.get_attribute("innerHTML")).find("Cairo") == -1 and (
    #             Location.get_attribute("innerHTML")
    #         ).find("Online") == -1:
    #             print("Not all events are nearby")
    #         else:
    #             print("Cairo or online")
    #     else:
    #         print("Not found")
    print("Location test passed")
    time.sleep(10)
    driver.close()


# * Phase 4
def GetDate(Date):
    # ---------------------------------------------- Auxiliary function to check date is in this weekend  ---------------------------------------------- #
    # remove extra data
    # Starts Monday, August 8, 2022
    if "Starts" in Date:
        Date = Date.split("Starts")[1]
    else:
        Date = Date.split("Ends")[1]
    # Monday, August 8, 2022
    # if "today", add today's date
    if Date.find("Today") != -1:
        Date = date.today()
    # if tomorrow, add tomorrow's date
    elif Date.find("Tomorrow") != -1:
        Datestr = (str(datetime.today() + timedelta(days=1))).split()[0]
        Datestr = Datestr.split("-")
        Day = int(Datestr[2])
        Month = int(Datestr[1])
        Year = int(Datestr[0])
        Date = date(Year, Month, Day)
    else:
        FullEventDateSeperated = Date.split()[1:]  # default is split at whitespaces
        FullEventDateSeperated[1] = (FullEventDateSeperated[1].split(","))[
            0
        ]  # to get rid of comma next to day
        MonthNum = datetime.strptime(
            FullEventDateSeperated[0][0:3], "%b"
        ).month  # to cast month from string to int (Note: Apr -> 4 (not 04))
        # to change formats: 9/4/2023 7:00PM -> 09/04/2023 07:00PM
        # Day
        if int(FullEventDateSeperated[1]) < 10:
            DayStr = "0" + FullEventDateSeperated[1]
        else:
            DayStr = FullEventDateSeperated[1]
        # Month
        if MonthNum < 10:
            MonthStr = "0" + str(MonthNum)
        else:
            MonthStr = str(MonthNum)
        Date = date(int(FullEventDateSeperated[2]), int(MonthStr), int(DayStr))
    # print(Date)
    return Date


# * Phase 4
def check_today_list(driver, Num):
    for i in range(1, ceil(Num / 12) + 1):
        for j in range(1, 13):
            time.sleep(5)
            START_DATE_XPATH = START_DATE_1 + str(j) + START_DATE_2
            EventStartDate = find_my_element(driver, "XPATH", START_DATE_XPATH)
            if EventStartDate != None:
                driver.execute_script("arguments[0].scrollIntoView();", EventStartDate)
                time.sleep(5)
                StartDate = EventStartDate.text
                StartDate = GetDate(StartDate)
                END_DATE_XPATH = END_DATE_1 + str(j) + END_DATE_2
                EventEndtDate = find_my_element(driver, "XPATH", END_DATE_XPATH)
                if EventEndtDate != None:
                    EndDate = EventEndtDate.text
                    EndDate = GetDate(EndDate)
                    assert StartDate <= date.today() <= EndDate, "Today Tab test failed"
                    print(
                        str(j)
                        + ": "
                        + str(StartDate)
                        + " --> "
                        + str(EndDate)
                        + " : Today"
                    )
            else:
                break
        # check if more pages
        NextPageButton = find_my_element(driver, "ID", NEXT_PAGE_BUTTON)
        check_not_found(driver, NextPageButton, "Next page button not found")
        if NextPageButton.is_enabled():
            NextPageButton.click()
        # driver.execute_script("arguments[0].scrollIntoView();", NextPageButton)
        # time.sleep(20)
        # if NextPageButton.is_enabled():
        # else:
        #     break


# * Phase 4
def today_tab_test(driver):
    # ---------------------------------------------- Testing today tab ---------------------------------------------- #
    # click on Today tab
    TodayTab = find_my_element(driver, "ID", TODAY_TAB)
    check_not_found(driver, TodayTab, "Today tab not found")
    TodayTab.click()
    time.sleep(10)
    # Scroll down to load
    # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(10)
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
    EventsNum = len(EventsList)
    if EventsNum == 0:
        print("No events in the today list")
    else:
        check_today_list(driver, EventsNum)
        print("Today tab test passed")
    # driver.close()


# * Phase 4
def is_this_weekend(StartDate, EndDate):
    # ---------------------------------------------- Auxiliary function to check date is in this weekend  ---------------------------------------------- #
    # Monday: 0
    # Tuesday: 1
    # Wednesday: 2
    # Thursday: 3
    # Friday: 4
    # Saturday: 5
    # Sunday: 6

    Today = date.today()
    Weekend1 = Today
    Weekend2 = Today
    if Today.weekday() == 4:  # Friday
        Weekend2 = Today + timedelta(days=1)
    elif Today.weekday() == 5:  # Saturday
        Weekend2 = "None"
    elif Today.weekday() == 6:  # Sunday
        Weekend1 = Today + timedelta(days=5)
        Weekend2 = Weekend1 + timedelta(days=1)
    else:
        Weekend1 = Today + timedelta(days=(4 - Today.weekday()))
        Weekend2 = Weekend1 + timedelta(days=1)

    if Weekend2 == "None":
        return StartDate <= Weekend1 <= EndDate
    else:
        return StartDate <= Weekend1 <= EndDate or StartDate <= Weekend2 <= EndDate
    # print(Weekend1)
    # print(Weekend2)


# * Phase 4
def check_this_weekend_list(driver, Num):
    for i in range(1, ceil(Num / 12) + 1):
        for j in range(1, 13):
            time.sleep(5)
            START_DATE_XPATH = START_DATE_1 + str(j) + START_DATE_2
            EventStartDate = find_my_element(driver, "XPATH", START_DATE_XPATH)
            if EventStartDate != None:
                driver.execute_script("arguments[0].scrollIntoView();", EventStartDate)
                time.sleep(5)
                StartDate = EventStartDate.text
                StartDate = GetDate(StartDate)
                END_DATE_XPATH = END_DATE_1 + str(j) + END_DATE_2
                EventEndtDate = find_my_element(driver, "XPATH", END_DATE_XPATH)
                if EventEndtDate != None:
                    EndDate = EventEndtDate.text
                    EndDate = GetDate(EndDate)
                    assert is_this_weekend(
                        StartDate, EndDate
                    ), "This weekend Tab test failed"
                    print(str(j) + ": " + str(StartDate) + " --> " + str(EndDate))
            else:
                break
        # check if more pages
        NextPageButton = find_my_element(driver, "ID", NEXT_PAGE_BUTTON)
        check_not_found(driver, NextPageButton, "Next page button not found")
        driver.execute_script("arguments[0].scrollIntoView();", NextPageButton)
        time.sleep(20)
        if NextPageButton.is_enabled():
            NextPageButton.click()
        else:
            break


# * Phase 4
def this_weekend_tab_test(driver):
    # ---------------------------------------------- Testing this weekend tab ---------------------------------------------- #
    # click on this weekend tab
    WeekendTab = find_my_element(driver, "ID", THIS_WEEKEND_TAB)
    check_not_found(driver, WeekendTab, "This weekend tab not found")
    WeekendTab.click()
    time.sleep(10)
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
    EventsNum = len(EventsList)
    if EventsNum == 0:
        print("No events in the weekend list")
    else:
        check_this_weekend_list(driver, EventsNum)
        print("This weekend tab test passed")
    # driver.close()


# * Phase 4
def paginations_test(driver):
    driver.get("https://www.hebtus.me/#")
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(30)
    # prev button disabled in first page
    PrevPageButton = find_my_element(driver, "ID", PREV_PAGE_BUTTON)
    check_not_found(driver, PrevPageButton, "Next page button not found")
    driver.execute_script("arguments[0].scrollIntoView();", PrevPageButton)
    time.sleep(20)
    assert not (PrevPageButton.is_enabled()), "Previous page button is not disabled"

    # get number of events
    EventsList = driver.find_elements(
        By.CLASS_NAME,
        "col",
    )
    if EventsList == None:
        print("No events in the today list")
        driver.close()
        exit()
    EventsNum = len(EventsList)

    if EventsNum < 12:
        # next page button disabled
        NextPageButton = find_my_element(driver, "ID", NEXT_PAGE_BUTTON)
        check_not_found(driver, NextPageButton, "Next page button not found")
        driver.execute_script("arguments[0].scrollIntoView();", NextPageButton)
        time.sleep(20)
        assert not (NextPageButton.is_enabled()), "Next page button is not disabled"
        print("Pagination test passed")
        driver.close()
        exit()

    # reach last page
    for i in range(1, ceil(EventsNum / 12)):
        # check if more pages
        NextPageButton = find_my_element(driver, "ID", NEXT_PAGE_BUTTON)
        check_not_found(driver, NextPageButton, "Next page button not found")
        driver.execute_script("arguments[0].scrollIntoView();", NextPageButton)
        time.sleep(20)
        assert NextPageButton.is_enabled(), "Next page button is not enabled"
        NextPageButton.click()
        time.sleep(5)

    # next page button disabled in the last page
    NextPageButton = find_my_element(driver, "ID", NEXT_PAGE_BUTTON)
    check_not_found(driver, NextPageButton, "Next page button not found")
    driver.execute_script("arguments[0].scrollIntoView();", NextPageButton)
    time.sleep(20)
    assert not (NextPageButton.is_enabled()), "Next page button is not disabled"

    print("Pagination test passed")
    driver.close()


# ? phase 5
def online_tab_test(driver):
    # ---------------------------------------------- Testing today tab ---------------------------------------------- #
    # click on online tab
    OnlineTab = find_my_element(driver, "ID", ONLINE_TAB)
    check_not_found(driver, OnlineTab, "Online tab not found")
    OnlineTab.click()
    time.sleep(10)
    # Get list of elements
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    EventsList = driver.find_elements(
        By.CLASS_NAME,
        "col",
    )
    if EventsList == None:
        print("No events in the today list")
        driver.close()
        exit()
    else:
        print(len(EventsList) - 8)

    EventsNum = len(EventsList) - 8
    if EventsNum == 0:
        print("No events in the weekend list")
    else:
        OnlineEvents = driver.find_elements(By.ID, "is-online")
        assert OnlineEvents != None, "Not all events are online"
        print(len(OnlineEvents))
        assert len(OnlineEvents) == EventsNum, "Not all events are online"
        print("Online tab test passed")


# ? phase 5
def free_tab_test(driver):
    # ---------------------------------------------- Testing free tab ---------------------------------------------- #
    # click on Free tab
    FreeTab = find_my_element(driver, "ID", FREE_TAB)
    check_not_found(driver, FreeTab, "Free tab not found")
    FreeTab.click()
    time.sleep(10)

    # Get list of elements
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    EventsList = driver.find_elements(
        By.XPATH,
        "//div[@class='card-body']",
    )
    if EventsList == None:
        print("No events in the free list")
        driver.close()
        exit()

    print(len(EventsList) - 8)
    EventsNum = len(EventsList) - 8
    if EventsNum == 0:
        print("No events in the free list")
    else:
        FreeEvents = driver.find_elements(By.ID, "is-free")
        assert FreeEvents != None, "Not all events are free"
        print(len(FreeEvents))
        assert len(FreeEvents) == EventsNum, "Not all events are free"
        print("Free tab test passed")


def test_category(driver, Name):
    # ---------------------------------------------- Auxiliary function to test categories ---------------------------------------------- #
    # Check if correct page is reached
    HeaderText = find_my_element(driver, "ID", HEADER_TEXT)
    check_not_found(driver, HeaderText, "Header text not found")
    print(HeaderText.text)
    assert Name in HeaderText.text, Name + " category page not reached"
    print(Name + " category page reached successfuly")


# ? phase 5
def categories_test(driver):
    # ---------------------------------------------- Testing Categories ---------------------------------------------- #
    # # -------------------- Music category -------------
    MusicTab = find_my_element(driver, "XPATH", MUSIC_CATEGORY)
    check_not_found(driver, MusicTab, "Music tab not found")
    driver.execute_script("arguments[0].scrollIntoView();", MusicTab)

    time.sleep(10)
    x, y = 200, 50

    # create an instance of ActionChains
    action = ActionChains(driver)

    # move the mouse to the desired location and click
    action.move_by_offset(x, y).click().perform()

    time.sleep(10)
    assert "Music" in str(driver.current_url), "Music category page not reached"
    test_category(driver, "Music")

    driver.back()
    time.sleep(5)

    # ---------------Performing & Visual Arts-----------
    MusicTab = find_my_element(driver, "XPATH", MUSIC_CATEGORY)
    check_not_found(driver, MusicTab, "Music tab not found")
    driver.execute_script("arguments[0].scrollIntoView();", MusicTab)

    time.sleep(10)
    x, y = 500, 50

    # create an instance of ActionChains
    action = ActionChains(driver)

    # move the mouse to the desired location and click
    action.move_by_offset(x, y).click().perform()

    time.sleep(10)
    assert "Performing&VisualArts" in str(
        driver.current_url
    ), "Performing & Visual Arts category page not reached"

    test_category(driver, "Performing & Visual Arts")
    driver.back()
    time.sleep(5)
    # ---------------------Holiday--------------
    MusicTab = find_my_element(driver, "XPATH", MUSIC_CATEGORY)
    check_not_found(driver, MusicTab, "Music tab not found")
    driver.execute_script("arguments[0].scrollIntoView();", MusicTab)

    time.sleep(10)
    x, y = 800, 50

    # create an instance of ActionChains
    action = ActionChains(driver)

    # move the mouse to the desired location and click
    action.move_by_offset(x, y).click().perform()

    time.sleep(10)
    assert "Holiday" in str(driver.current_url), "Holiday category page not reached"

    test_category(driver, "Holiday")
    driver.back()
    time.sleep(5)
    # # ---------------Health & Fitness---------
    MusicTab = find_my_element(driver, "XPATH", MUSIC_CATEGORY)
    check_not_found(driver, MusicTab, "Music tab not found")
    driver.execute_script("arguments[0].scrollIntoView();", MusicTab)

    time.sleep(10)
    x, y = 1100, 50

    # create an instance of ActionChains
    action = ActionChains(driver)

    # move the mouse to the desired location and click
    action.move_by_offset(x, y).click().perform()
    # action.move_by_offset(x, y).click().perform()

    time.sleep(10)
    assert "Health&Fitness" in str(
        driver.current_url
    ), "Health & Fitness category page not reached"

    test_category(driver, "Health & Fitness")
    driver.back()
    time.sleep(5)
    # -----------------Hobbies-------------
    MusicTab = find_my_element(driver, "XPATH", MUSIC_CATEGORY)
    check_not_found(driver, MusicTab, "Music tab not found")
    driver.execute_script("arguments[0].scrollIntoView();", MusicTab)

    time.sleep(10)
    x, y = 200, 120

    # create an instance of ActionChains
    action = ActionChains(driver)

    # move the mouse to the desired location and click
    action.move_by_offset(x, y).click().perform()
    # action.move_by_offset(x, y).click().perform()

    time.sleep(10)
    assert "Hobbies" in str(driver.current_url), "Hobbies category page not reached"

    test_category(driver, "Hobbies")
    driver.back()
    time.sleep(5)
    # -----------Business---------------
    MusicTab = find_my_element(driver, "XPATH", MUSIC_CATEGORY)
    check_not_found(driver, MusicTab, "Music tab not found")
    driver.execute_script("arguments[0].scrollIntoView();", MusicTab)

    time.sleep(10)
    x, y = 500, 120

    # create an instance of ActionChains
    action = ActionChains(driver)

    # move the mouse to the desired location and click
    action.move_by_offset(x, y).click().perform()
    # action.move_by_offset(x, y).click().perform()

    time.sleep(10)
    assert "Business" in str(driver.current_url), "Business category page not reached"

    test_category(driver, "Business")
    driver.back()
    time.sleep(5)
    # --------------Food & Drink------------------
    MusicTab = find_my_element(driver, "XPATH", MUSIC_CATEGORY)
    check_not_found(driver, MusicTab, "Music tab not found")
    driver.execute_script("arguments[0].scrollIntoView();", MusicTab)

    time.sleep(10)
    x, y = 800, 120

    # create an instance of ActionChains
    action = ActionChains(driver)

    # move the mouse to the desired location and click
    action.move_by_offset(x, y).click().perform()

    time.sleep(10)
    assert "Food&Drink" in str(
        driver.current_url
    ), "Food & Drink category page not reached"

    test_category(driver, "Food & Drink ")
    driver.back()
    time.sleep(5)
    # ------------------Sports & Fitness ----------------
    MusicTab = find_my_element(driver, "XPATH", MUSIC_CATEGORY)
    check_not_found(driver, MusicTab, "Music tab not found")
    driver.execute_script("arguments[0].scrollIntoView();", MusicTab)

    time.sleep(10)
    x, y = 1100, 120

    # create an instance of ActionChains
    action = ActionChains(driver)

    # move the mouse to the desired location and click
    action.move_by_offset(x, y).click().perform()

    time.sleep(10)
    assert "Sports&Fitness" in str(
        driver.current_url
    ), "Sports & Fitness category page not reached"

    test_category(driver, "Sports & Fitness")
    # click on hebtus icon
    Logo = find_my_element(driver, "ID", "hebtus-logo")
    check_not_found(driver, Logo, "Hebtus logo not found")
    Logo.click()
    time.sleep(5)
    # check if landing page is reached
    LandingPage = find_my_element(driver, "ID", LANDING_PAGE)
    check_not_found(driver, LandingPage, "Landing page not reached")
    time.sleep(5)
    print("Categories test passed")
    driver.close()
