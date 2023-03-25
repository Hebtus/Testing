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
    login(driver, "testereventbrite@gmail.com", "eventbritetester")
    # free_tab_test(driver)


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
    # location_nearby_events_test(driver)
    # free_tab_test(driver)
    categories_test(driver)


def location_nearby_events_test(driver):
    MyLocation = find_my_element(driver, "ID", LOCATION_PICKER)
    check_not_found(driver, MyLocation, "Location not found")
    print(MyLocation.get_attribute("value"))
    if MyLocation.get_attribute("value") == "Al Qahirah":
        print("Location detected correctly")
    else:
        print("Location not detected correctly")
    # click on All tab
    AllTab = find_my_element(driver, "XPATH", ALL_TAB)
    check_not_found(driver, AllTab, "All tab not found")
    AllTab.click()
    time.sleep(30)
    # Scroll down
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(60)
    EventsList = driver.find_elements(
        By.CLASS_NAME,
        EVENT_ELEMENT,
    )
    if len(EventsList) == 0:
        print("No events in the list")
        driver.close()
        exit()

    EventsList = EventsList[0:10]
    EventsURLList = []
    for element in EventsList:
        try:
            link = element.find_element(By.TAG_NAME, "a")
            EventsURLList.append(link.get_attribute("href"))
            print(link.get_attribute("href"))
        except:
            print("No Data Available!")
    print(EventsURLList)
    for Link in EventsURLList:
        driver.get(Link)
        driver.implicitly_wait(10)
        # Scroll down
        driver.execute_script("window.scrollBy(0,500)")
        driver.implicitly_wait(10)
        Location = find_my_element(
            driver,
            "XPATH",
            "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[2]/section/div[2]/section[2]/div/div/div[2]/p",
        )
        check_not_found(driver, Location, "location not found")
        if Location != None:
            if (Location.get_attribute("innerHTML")).find("Cairo") == -1 and (
                Location.get_attribute("innerHTML")
            ).find("Online") == -1:
                print("Not all events are nearby")
            else:
                print("Cairo or online")
        else:
            print("Not found")

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
    # click on All tab
    OnlineTab = find_my_element(driver, "XPATH", ONLINE_TAB)
    check_not_found(driver, OnlineTab, "Online tab not found")
    OnlineTab.click()
    time.sleep(30)
    # Scroll down
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(60)
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
    for element in EventsList:
        try:
            link = element.find_element(By.TAG_NAME, "a")
            EventsURLList.append(link.get_attribute("href"))
            print(link.get_attribute("href"))
        except:
            print("No Data Available!")
    print(EventsURLList)
    for Link in EventsURLList:
        driver.get(Link)
        driver.implicitly_wait(10)
        # Scroll down
        driver.execute_script("window.scrollBy(0,500)")
        driver.implicitly_wait(10)
        Location = find_my_element(
            driver,
            "XPATH",
            "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[2]/section/div[2]/section[2]/div/div/div[2]/p",
        )
        check_not_found(driver, Location, "location not found")
        if Location != None:
            if (Location.get_attribute("innerHTML")).find("Online") == -1:
                print("Not all events are online")
                # driver.close()
                # exit()
            else:
                print("online")
        else:
            print("Not found")
    print("Online tab test passed")
    time.sleep(10)
    driver.close()


def free_tab_test(driver):
    # click on Free tab
    FreeTab = find_my_element(driver, "XPATH", FREE_TAB)
    check_not_found(driver, FreeTab, "Free tab not found")
    FreeTab.click()
    time.sleep(30)
    # Scroll down
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(30)
    try:
        EventsList = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (
                    By.CLASS_NAME,
                    "feed-events-bucket__content__cards-container",
                )
            )
        )
    except:
        print("Element not found.")
        exit()
    EventsList = driver.find_elements(
        By.CLASS_NAME,
        EVENT_ELEMENT,
    )
    EventsURLList = []
    # EventsList = EventsList[0:9]
    for element in EventsList:
        try:
            link = element.find_element(By.TAG_NAME, "a")
            EventsURLList.append(link.get_attribute("href"))
            print(link.get_attribute("href"))
        except:
            print("No Data Available!")

    for Link in EventsURLList:
        driver.get(Link)
        driver.implicitly_wait(10)
        # Scroll down
        driver.execute_script("window.scrollBy(0,500)")
        driver.implicitly_wait(10)

        Free = find_my_element(driver, "XPATH", FREE_INFO_2)
        if Free == None:
            Free = find_my_element(driver, "XPATH", FREE_INFO_1)
            if Free == None:
                print("Ticket price not found")
                exit()
        if Free.get_attribute("innerHTML") != "Free":
            print("Not all events are free")
            driver.close()
            exit()
    print("Free tab test passed")
    driver.close()


def test_category(driver, LinkText, Name):
    driver.execute_script("window.scrollBy(0,500)")
    time.sleep(30)
    Category = find_my_element(driver, "LINK_TEXT", LinkText)
    check_not_found(driver, Category, (Name + " category button not found"))
    Category.click()
    time.sleep(30)

    Page = find_my_element(
        driver,
        "XPATH",
        "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/div[1]/div/div/div/h1",
    )
    check_not_found(driver, Page, (Name + " category page not reached"))
    if (Page.get_attribute("innerHTML")).find(Name) == -1:
        print(Name + " category page not reached")
        driver.back()
        return

    print(Name + " category page reached successfuly")
    driver.back()
    time.sleep(30)


def categories_test(driver):

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
    driver.execute_script("window.scrollBy(0,500)")
    time.sleep(30)
    MusicCategory = find_my_element(driver, "LINK_TEXT", MUSIC_CATEGORY)
    check_not_found(driver, MusicCategory, "Music category button not found")
    MusicCategory.click()
    time.sleep(30)

    driver.close()
