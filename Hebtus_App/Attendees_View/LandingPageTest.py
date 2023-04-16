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

from datetime import datetime, date, timedelta


def landing_page(driver):
    # call_location_test(driver)
    # time.sleep(30)
    # call_see_more_test(driver)
    # time.sleep(30)
    # call_today_tab_test(driver)
    # time.sleep(30)
    call_weekend_tab(driver)
    # time.sleep(30)
    # call_online_tab(driver)
    # time.sleep(30)
    # call_free_tab_test(driver)
    # time.sleep(30)
    # call_categories_test(driver)


def call_location_test(driver):
    # login(driver, "testereventbrite@gmail.com", "eventbritetester")
    location_nearby_events_test(driver)


def call_see_more_test(driver):
    login(driver, "testereventbrite@gmail.com", "eventbritetester")
    see_more_test(driver)


def call_today_tab_test(driver):
    # login(driver, "testereventbrite@gmail.com", "eventbritetester")
    today_tab_test(driver)


def call_weekend_tab(driver):
    # login(driver, "testereventbrite@gmail.com", "eventbritetester")
    this_weekend_tab_test(driver)


def call_online_tab(driver):
    login(driver, "testereventbrite@gmail.com", "eventbritetester")
    online_tab_test(driver)


def call_free_tab_test(driver):
    login(driver, "testereventbrite@gmail.com", "eventbritetester")
    free_tab_test(driver)


def call_categories_test(driver):
    login(driver, "testereventbrite@gmail.com", "eventbritetester")
    categories_test(driver)


def login(driver, Email, Password):
    # Open eventbrite
    driver.get("https://www.eventbrite.com/signin")
    driver.maximize_window()
    driver.implicitly_wait(5)
    # Login with email and password
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
    AllTab = find_my_element(driver, "XPATH", ALL_TAB)
    check_not_found(driver, AllTab, "All tab not found")
    AllTab.click()
    time.sleep(10)


def location_nearby_events_test(driver):
    # ---------------------------------------------- Testing Detection of geolocation ---------------------------------------------- #
    driver.get("https://www.hebtus.me/#")
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(5)
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


def see_more_test(driver):
    # ---------------------------------------------- Testing see more button ---------------------------------------------- #
    # Scroll down to load
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(30)
    SeeMoreButton = find_my_element(driver, "LINK_TEXT", SEE_MORE_BUTTON)
    check_not_found(driver, SeeMoreButton, "See more button not found")
    # create action chain object
    action = ActionChains(driver)
    # perform the operation
    action.move_to_element(SeeMoreButton).click().perform()
    time.sleep(30)
    SeeMorePge = find_my_element(driver, "XPATH", SEE_MORE_PAGE)
    check_not_found(driver, SeeMorePge, "See more page not reached")
    time.sleep(10)
    print("See more test passed")
    driver.close()


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
    print(Date)
    return Date


def today_tab_test(driver):
    # ---------------------------------------------- Testing today tab ---------------------------------------------- #
    driver.get("https://www.hebtus.me/#")
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(5)
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
    for i in range(1, EventsNum):
        time.sleep(5)
        START_DATE_XPATH = (
            START_DATE_1 + str(i) + START_DATE_2
        )
        EventStartDate = find_my_element(driver, "XPATH", START_DATE_XPATH)
        if EventStartDate != None:
            driver.execute_script("arguments[0].scrollIntoView();", EventStartDate)
            time.sleep(5)
            StartDate = EventStartDate.text
            StartDate = GetDate(StartDate)
            END_DATE_XPATH = (END_DATE_1+ str(i)+ END_DATE_2)
            EventEndtDate = find_my_element(driver, "XPATH", END_DATE_XPATH)
            if EventEndtDate != None:
                EndDate = EventEndtDate.text
                EndDate = GetDate(EndDate)
                assert StartDate <= date.today() <= EndDate, "Today Tab test failed"
                # if StartDate <= date.today() <= EndDate:
                #     print("Today")
                # else:
                #     print("Not today")

    print("Today tab test passed")
    driver.close()

# TODO: XPATH in references file
# TODO: This weekend

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
    if Today.weekday() == 4:    # Friday
        Weekend2 = Today + timedelta(days=1)
    elif Today.weekday() == 5:  # Saturday
        Weekend2 = "None"
    elif Today.weekday() == 6:  #Sunday
        Weekend1 = Today + timedelta(days=5)
        Weekend2 = Weekend1 + timedelta(days=1)
    else:
        Weekend1 = Today + timedelta(days=(4-Today.weekday()))
        Weekend2 = Weekend1 + timedelta(days=1)

    if Weekend2 == "None":
        return StartDate <= Weekend1 <= EndDate
    else:
        return StartDate <= Weekend1 <= EndDate and StartDate <= Weekend2 <= EndDate
    # print(Weekend1)
    # print(Weekend2)

    # if Date.weekday() == 5 or Date.weekday() == 4:
    #     Difference = (Date - date.today()).days
    #     # check if saturday and event day is next friday
    #     if Difference == 6 and date.today().weekday() == 5:
    #         return False
    #     # check if the difference is < 6 (means it is in the same week as today)
    #     if Difference > 6 or Difference < 0:
    #         return False
    #     else:
    #         return True


    # # remove extra data
    # print(Date)
    # Date = Date.split("+")[0]
    # # if "today", add today's date
    # if Date.find("Today") != -1:
    #     Date = date.today()
    # # if tomorrow, add tomorrow's date
    # elif Date.find("Tomorrow") != -1:
    #     Datestr = (str(datetime.today() + timedelta(days=1))).split()[0]
    #     Datestr = Datestr.split("-")
    #     Day = int(Datestr[2])
    #     Month = int(Datestr[1])
    #     Year = int(Datestr[0])
    #     Date = date(Year, Month, Day)
    # else:
    #     FullEventDateSeperated = Date.split()[1:]  # default is split at whitespaces
    #     FullEventDateSeperated[1] = (FullEventDateSeperated[1].split(","))[
    #         0
    #     ]  # to get rid of comma next to day
    #     MonthNum = datetime.strptime(
    #         FullEventDateSeperated[0], "%b"
    #     ).month  # to cast month from string to int (Note: Apr -> 4 (not 04))
    #     # to change formats: 9/4/2023 7:00PM -> 09/04/2023 07:00PM
    #     # Day
    #     if int(FullEventDateSeperated[1]) < 10:
    #         DayStr = "0" + FullEventDateSeperated[1]
    #     else:
    #         DayStr = FullEventDateSeperated[1]
    #     # Month
    #     if MonthNum < 10:
    #         MonthStr = "0" + str(MonthNum)
    #     else:
    #         MonthStr = str(MonthNum)
    #     Date = date(2023, int(MonthStr), int(DayStr))
    # print(Date)
    # # weekdays = 5,4 are weekends
    # if Date.weekday() == 5 or Date.weekday() == 4:
    #     Difference = (Date - date.today()).days
    #     # check if saturday and event day is next friday
    #     if Difference == 6 and date.today().weekday() == 5:
    #         return False
    #     # check if the difference is < 6 (means it is in the same week as today)
    #     if Difference > 6 or Difference < 0:
    #         return False
    #     else:
    #         return True


def this_weekend_tab_test(driver):
    # ---------------------------------------------- Testing this weekend tab ---------------------------------------------- #
    driver.get("https://www.hebtus.me/#")
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(30)
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
    for i in range(1, EventsNum):
        time.sleep(5)
        START_DATE_XPATH = (
            START_DATE_1 + str(i) + START_DATE_2
        )
        EventStartDate = find_my_element(driver, "XPATH", START_DATE_XPATH)
        if EventStartDate != None:
            driver.execute_script("arguments[0].scrollIntoView();", EventStartDate)
            time.sleep(5)
            StartDate = EventStartDate.text
            StartDate = GetDate(StartDate)
            print(StartDate)
            END_DATE_XPATH = (END_DATE_1+ str(i)+ END_DATE_2)
            EventEndtDate = find_my_element(driver, "XPATH", END_DATE_XPATH)
            if EventEndtDate != None:
                EndDate = EventEndtDate.text
                EndDate = GetDate(EndDate)
                print(EndDate)
                # Check if this weekend
                assert is_this_weekend(StartDate, EndDate), "This weekend Tab test failed"
                print("This weekend")
                # assert StartDate <= date.today() <= EndDate, "Today Tab test failed"
    
    
    
    # click on Today tab
    TodayTab = find_my_element(driver, "XPATH", THIS_WEEKEND_TAB)
    check_not_found(driver, TodayTab, "This weekend tab not found")
    TodayTab.click()
    time.sleep(30)
    # Scroll down to load
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(30)
    # Get events list
    EventsList = driver.find_elements(
        By.CLASS_NAME,
        EVENT_ELEMENT,
    )
    if EventsList == None:
        print("No events in the weekend list")
        driver.close()
        exit()
    EventsNumber = len(EventsList)
    EventsDateList = []
    # Get date of all events
    for i in range(EventsNumber):
        EVENT_DATE = WEEKEND_EVENT_DATE_1 + str(i) + WEEKEND_EVENT_DATE_2
        EventDate = find_my_element(driver, "XPATH", EVENT_DATE)
        if EventDate != None:
            EventsDateList.append(EventDate.get_attribute("innerHTML"))
    # print(EventsDateList)
    # Check if the date is in this weekend
    for Date in EventsDateList:
        if is_this_weekend(Date) == False:
            print("Not all events are this weekend")
            driver.close()
            exit()
    print("This weekend tab test passed")
    time.sleep(10)
    driver.close()


def online_tab_test(driver):
    # ---------------------------------------------- Testing today tab ---------------------------------------------- #
    # click on online tab
    OnlineTab = find_my_element(driver, "XPATH", ONLINE_TAB)
    check_not_found(driver, OnlineTab, "Online tab not found")
    OnlineTab.click()
    time.sleep(30)
    # Scroll down to load
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(60)
    # Get event list
    EventsList = driver.find_elements(
        By.CLASS_NAME,
        EVENT_ELEMENT,
    )
    if len(EventsList) == 0:
        print("No events in the list")
        driver.close()
        exit()
    # EventsList = EventsList[0:10]
    EventsURLList = []
    # Get URLs of event pages
    for element in EventsList:
        try:
            link = element.find_element(By.TAG_NAME, "a")
            EventsURLList.append(link.get_attribute("href"))
            print(link.get_attribute("href"))
        except:
            print("No Data Available!")
    # print(EventsURLList)
    for Link in EventsURLList:
        # Open event page
        driver.get(Link)
        driver.implicitly_wait(10)
        # Scroll down to load
        driver.execute_script("window.scrollBy(0,500)")
        driver.implicitly_wait(10)
        # Get location
        Location = find_my_element(
            driver,
            "XPATH",
            ONLINE_INFO_1,
        )

        if Location == None:
            Location = find_my_element(
                driver,
                "XPATH",
                ONLINE_INFO_2,
            )
        check_not_found(driver, Location, "location not found")
        # check if online
        if Location != None:
            if (Location.get_attribute("innerHTML")).find("Online") == -1:
                print("Not all events are online")
                driver.close()
                exit()
            else:
                print("online")
        else:
            print("Not found")
    print("Online tab test passed")
    time.sleep(10)
    driver.close()


def free_tab_test(driver):
    # ---------------------------------------------- Testing free tab ---------------------------------------------- #
    # click on Free tab
    FreeTab = find_my_element(driver, "XPATH", FREE_TAB)
    check_not_found(driver, FreeTab, "Free tab not found")
    FreeTab.click()
    time.sleep(30)
    # Scroll down to load
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(30)
    # Get event list
    EventsList = driver.find_elements(
        By.CLASS_NAME,
        EVENT_ELEMENT,
    )
    if len(EventsList) == 0:
        print("No events in free tab list")
        driver.close()
        exit()
    EventsURLList = []
    # EventsList = EventsList[0:9]
    # get URLs of event pages
    for element in EventsList:
        try:
            link = element.find_element(By.TAG_NAME, "a")
            EventsURLList.append(link.get_attribute("href"))
            print(link.get_attribute("href"))
        except:
            print("No Data Available!")
    for Link in EventsURLList:
        # Open event page
        driver.get(Link)
        driver.implicitly_wait(10)
        # Scroll down to load
        driver.execute_script("window.scrollBy(0,500)")
        driver.implicitly_wait(10)
        Free = find_my_element(
            driver,
            "XPATH",
            '//*[@id="root"]/div/section/form/div/div/div/ul/li/div/div/div[2]/div/span',
        )
        if Free == None:
            Free = find_my_element(driver, "XPATH", FREE_INFO_1)
            if Free == None:
                print("Ticket price not found")
                exit()
        # Check if price is free
        if Free.get_attribute("innerHTML") != "Free":
            print("Not all events are free")
            driver.close()
            exit()
    print("Free tab test passed")
    driver.close()


def test_category(driver, LinkText, Name):
    # ---------------------------------------------- Auxiliary function to test categories ---------------------------------------------- #
    # Scroll down to load
    driver.execute_script("window.scrollBy(0,500)")
    time.sleep(30)
    # Fin category button and click it
    Category = find_my_element(driver, "LINK_TEXT", LinkText)
    check_not_found(driver, Category, (Name + " category button not found"))
    Category.click()
    time.sleep(30)
    # Find Page title
    Page = find_my_element(
        driver,
        "XPATH",
        "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/div[1]/div/div/div/h1",
    )
    check_not_found(driver, Page, (Name + " category page not reached"))
    # Check if correct page is reached
    if (Page.get_attribute("innerHTML")).find(Name) == -1:
        print(Name + " category page not reached")
        driver.back()
        return
    print(Name + " category page reached successfuly")
    # Go back to previous page (home page)
    driver.back()
    time.sleep(30)


def categories_test(driver):
    # ---------------------------------------------- Testing Categories ---------------------------------------------- #
    # click on All tab
    AllTab = find_my_element(driver, "XPATH", ALL_TAB)
    check_not_found(driver, AllTab, "All tab not found")
    AllTab.click()
    time.sleep(30)
    test_category(driver, MUSIC_CATEGORY, "Music events")
    test_category(driver, HOBBBIES_CATEGORY, "Hobbies events")
    test_category(driver, VISUAL_ARTS_CATEGORY, "Visual Arts events")
    test_category(driver, BUSINESS_CATEGORY, "Business events")
    test_category(driver, HOLDIDAY_CATEGORY, "Holiday events")
    test_category(driver, FOOD_DRINK_CATEGORY, "Drink events")
    test_category(driver, HEALTH_CATEGORY, "Health events")
    test_category(driver, SPORTS_CATEGORY, "Fitness events")
    driver.close()
