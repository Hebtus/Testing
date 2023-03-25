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

from datetime import datetime, date, timedelta


def landing_page(driver):
    # login(driver, "testereventbrite@gmail.com", "eventbritetester")
    free_tab_test(driver)


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
    # see_more_test(driver)
    # location_nearby_kevents_test(driver)
    # today_tab_test(driver)
    # this_weekend_tab_test(driver)
    location_nearby_events_test(driver)
    # free_tab_test(driver)


def location_nearby_events_test(driver):
    # MyLocation = find_my_element(driver, "ID", LOCATION_PICKER)
    # check_not_found(driver, MyLocation, "Location not found")
    # print(MyLocation.get_attribute("value"))
    # if MyLocation.get_attribute("value") == "Al Qahirah":
    #     print("Location detected correctly")
    # else:
    #     print("Location not detected correctly")
    # click on All tab
    FreeTab = find_my_element(driver, "XPATH", FREE_TAB)
    check_not_found(driver, FreeTab, "Free tab not found")
    FreeTab.click()
    time.sleep(30)
    # Scroll down
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(60)
    EventsList = driver.find_elements(
        By.CLASS_NAME,
        EVENT_ELEMENT,
    )
    if EventsList == None:
        print("No events in the list")
        driver.close()
        exit()
    EventsList = EventsList[0:10]
    EventsNumber = len(EventsList)
    EventsLocationList = []
    for i in range(EventsNumber):
        EVENT_LOCATION = ALL_EVENTS_LOCATION_1 + str(i) + ALL_EVENTS_LOCATION_2
        EventLocation = find_my_element(driver, "XPATH", EVENT_LOCATION)
        if EventLocation != None:
            EventsLocationList.append(EventLocation.get_attribute("innerHTML"))
        else:
            print("No location found")
    print(EventsLocationList)
    for Location in EventsLocationList:
        if Location.find("Cairo") == -1:
            print("Not all events are nearby")
            driver.close()
            exit()
    print("Nearby events test passed")
    time.sleep(10)
    driver.close()


def see_more_test(driver):
    # Scroll down
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
    check_not_found(driver, SeeMoreButton, "See more page not reached")
    time.sleep(10)
    print("See more test passed")
    driver.close()


def today_tab_test(driver):
    # click on Today tab
    TodayTab = find_my_element(driver, "XPATH", TODAY_TAB)
    check_not_found(driver, TodayTab, "Today tab not found")
    TodayTab.click()
    time.sleep(30)
    # Scroll down
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(30)
    EventsList = driver.find_elements(
        By.CLASS_NAME,
        EVENT_ELEMENT,
    )
    if EventsList == None:
        print("No events in the today list")
        driver.close()
        exit()
    EventsNumber = len(EventsList)
    EventsDateList = []
    for i in range(EventsNumber):
        EVENT_DATE = ALL_EVENT_DATE_1 + str(i) + ALL_EVENT_DATE_2
        EventDate = find_my_element(driver, "XPATH", EVENT_DATE)
        if EventDate != None:
            EventsDateList.append(EventDate.get_attribute("innerHTML"))
    print(EventsDateList)
    for Date in EventsDateList:
        if Date.find("Today") == -1:
            print("Not all events are today")
            driver.close()
            exit()
    print("Today tab test passed")
    time.sleep(10)
    driver.close()


def is_this_weekend(Date):
    # remove extra dat
    Date = Date.split("+")[0]

    if Date.find("Today") != -1:
        Date = date.today()
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
            FullEventDateSeperated[0], "%b"
        ).month  # to cast month from string to int (Note: April -> 4 (not 04))
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
            Date = date(2023, int(MonthStr), int(DayStr))

    if Date.weekday() == 5 or Date.weekday() == 4:
        Difference = (Date - date.today()).days
        # check if saturday and event day is next friday
        if Difference == 6 and date.today().weekday() == 5:
            return False
        if Difference > 6 or Difference < 0:
            return False
        else:
            return True


def this_weekend_tab_test(driver):
    # click on Today tab
    TodayTab = find_my_element(driver, "XPATH", THIS_WEEKEND_TAB)
    check_not_found(driver, TodayTab, "This weekend tab not found")
    TodayTab.click()
    time.sleep(30)
    # Scroll down
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(30)
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
    for i in range(EventsNumber):
        EVENT_DATE = WEEKEND_EVENT_DATE_1 + str(i) + WEEKEND_EVENT_DATE_2
        EventDate = find_my_element(driver, "XPATH", EVENT_DATE)
        if EventDate != None:
            EventsDateList.append(EventDate.get_attribute("innerHTML"))
    print(EventsDateList)
    for Date in EventsDateList:
        if is_this_weekend(Date) == False:
            print("Not all events are this weekend")
            driver.close()
            exit()
    print("This weekend tab test passed")
    time.sleep(10)
    driver.close()


def online_tab_test(driver):
    print("")


def free_tab_test(driver):
    # click on Free tab
    # FreeTab = find_my_element(driver, "XPATH", FREE_TAB)
    # check_not_found(driver, FreeTab, "Free tab not found")
    # FreeTab.click()
    # time.sleep(30)
    # # Scroll down
    # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    # time.sleep(30)
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
    # EventsList = driver.find_elements(
    #     By.CLASS_NAME,
    #     EVENT_ELEMENT,
    # )
    # EventsURLList = []
    # # EventsList = EventsList[0:9]
    # for element in EventsList:
    #     try:
    #         link = element.find_element(By.TAG_NAME, "a")
    #         EventsURLList.append(link.get_attribute("href"))
    #         print(link.get_attribute("href"))
    #     except:
    #         print("No Data Available!")

    EventsURLList = [
        "https://www.eventbrite.com/e/the-design-show-egypt-tickets-372686233557?aff=ebdssbcitybrowse",
        "https://www.eventbrite.at/e/cloudflight-coding-contest-ccc-cairo-tickets-535486292917?aff=ebdssbcitybrowse",
        "https://www.eventbrite.com/e/how-to-improve-your-memory-cairo-tickets-488040421037?aff=ebdssbcitybrowse",
        "https://www.eventbrite.com/e/middle-east-vape-show-2023-tickets-512820940237?aff=ebdssbcitybrowse",
        "https://www.eventbrite.com.au/e/eit-visit-in-egypt-march-2023-tickets-596314070437?aff=ebdssbcitybrowse",
        "https://www.eventbrite.com/e/effective-note-taking-cairo-tickets-488909981917?aff=ebdssbcitybrowse",
        "https://www.eventbrite.com/e/how-can-i-feel-confident-and-dynamic-egypt-experience-the-holy-energy-tickets-167887842055?aff=ebdssbcitybrowse",
        "https://www.eventbrite.com/e/meditation-zarqa-learn-to-be-in-balance-immotionaly-spiritualy-tickets-168533860313?aff=ebdssbcitybrowse",
        "https://www.eventbrite.com/e/first-time-authors-publishing-masterclass-write-a-bestseller-cairo-tickets-591303453547?aff=ebdssbcitybrowse",
    ]
    for Link in EventsURLList:
        driver.get(Link)
        driver.maximize_window()
        driver.implicitly_wait(10)
        # Scroll down
        driver.execute_script("window.scrollBy(0,500)")
        driver.implicitly_wait(10)
        Free = find_my_element(driver, "XPATH", FREE_INFO_2)
        if Free == None:
            Free = find_my_element(driver, "XPATH", FREE_INFO_1)
            if Free == None:
                exit()
        if Free.get_attribute("innerHTML") == "Free":
            print("Free")
        else:
            print("not free")
        print(Free.get_attribute("innerHTML"))
    print("Free tab test passed")
    driver.close()


def other_tabs_test(driver):
    # click tab
    # test
    # go back
    print("")


def categories_test(driver):
    # click tab
    # test
    # go back
    print("")
