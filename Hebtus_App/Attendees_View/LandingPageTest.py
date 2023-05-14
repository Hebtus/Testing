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

from datetime import datetime, date, timedelta


def landing_page(driver):
    sign_in_valid(driver, "hebtususer@gmail.com", "123456789")
    # see_more_test(driver)
    # tabs_categories_test(driver)

    # location_nearby_events_test(driver)

    # today_tab_test(driver)

    # this_weekend_tab_test(driver)

    # online_tab_test(driver)

    free_tab_test(driver)


    # categories_test(driver)


# ? Phase 5
def tabs_categories_test(driver):
    # music
    MusicTab = find_my_element(driver, "XPATH", MUSIC_TAB)
    check_not_found(driver, MusicTab, "Music tab not found")
    assert MusicTab.is_enabled(), "Music tab is not enabled"
    MusicTab.click()
    time.sleep(2)
    # food
    FoodTab = find_my_element(driver, "XPATH", FOOD_DRINK_TAB)
    check_not_found(driver, FoodTab, "food tab not found")
    assert FoodTab.is_enabled(), "food tab is not enabled"
    FoodTab.click()
    time.sleep(2)
    # Charity
    CharityTab = find_my_element(driver, "XPATH", CHARITY_CAUSES_TAB)
    check_not_found(driver, CharityTab, "Charity tab not found")
    assert CharityTab.is_enabled(), "Charity tab is not enabled"
    CharityTab.click()
    time.sleep(2)
    # # All
    AllTab = find_my_element(driver, "XPATH", ALL_TAB)
    check_not_found(driver, AllTab, "All tab not found")
    assert AllTab.is_enabled(), "All tab is not enabled"
    AllTab.click()
    time.sleep(2)
    # Swipe right twice
    screen_width = driver.get_window_size()["width"]
    screen_height = driver.get_window_size()["height"]
    AllTab = find_my_element(driver, "XPATH", ALL_TAB)
    check_not_found(driver, AllTab, "All tab not found")
    location2 = AllTab.location
    size2 = AllTab.size
    CharityTab = find_my_element(driver, "XPATH", CHARITY_CAUSES_TAB)
    check_not_found(driver, CharityTab, "Charity tab not found")
    # Swipe right using TouchAction
    # Calculate the starting and ending positions for the swipe
    location = CharityTab.location
    size = CharityTab.size

    # Swipe from the center of the element to the top of the screen
    start_x = location["x"] + size["width"] / 2
    start_y = location["y"] + size["height"] / 2
    end_x = location2["x"] + size2["width"] / 2
    end_y = location["y"] + size["height"] / 2
    swipe_action = TouchAction(driver)
    swipe_action.press(x=start_x, y=start_y).wait(500).move_to(
        x=end_x, y=end_y
    ).release().perform()
    time.sleep(1)
    swipe_action.press(x=start_x, y=start_y).wait(500).move_to(
        x=end_x, y=end_y
    ).release().perform()
    time.sleep(1)

    # Online tab
    OnlineTab = find_my_element(driver, "XPATH", ONLINE_TAB)
    check_not_found(driver, OnlineTab, "Online tab not found")
    assert OnlineTab.is_enabled(), "Online tab is not enabled"
    OnlineTab.click()
    print("Tabs test passed")
    # ---------------- Categories ---------------------
    # Music category
    MusicCategory = find_my_element(driver, "XPATH", MUSIC_CATEGORY)
    check_not_found(driver, MusicCategory, "Music Category not found")
    assert MusicCategory.is_enabled(), "Music Category is not enabled"
    MusicCategory.click()
    time.sleep(3)
    # Food category
    FoodCategory = find_my_element(driver, "XPATH", FOOD_DRINK_CATEGORY)
    check_not_found(driver, FoodCategory, "Food Category not found")
    assert FoodCategory.is_enabled(), "Food Category is not enabled"
    FoodCategory.click()
    time.sleep(3)
    # Scroll down using TouchAction
    swipe_action = TouchAction(driver)
    swipe_action.press(x=screen_width * 0.5, y=screen_height * 0.8).move_to(
        x=screen_width * 0.5, y=screen_height * 0.2
    ).release().perform()
    time.sleep(3)

    # Charity category
    CharityCategory = find_my_element(driver, "XPATH", CHARITY_CATEGORY)
    check_not_found(driver, CharityCategory, "Charity Category not found")
    assert CharityCategory.is_enabled(), "Charity Category is not enabled"
    CharityCategory.click()
    time.sleep(3)
    print("Categories test passed")
    driver.quit()


# * Phase 4
def see_more_test(driver):
    # ---------------------------------------------- Testing see more button ---------------------------------------------- #
    # Scroll down to see more button
    # get the size of the window
    window_size = driver.get_window_size()

    # starting coordinates for the swipe gesture
    start_x = window_size["width"] // 2
    start_y = window_size["height"] - 100

    # ending coordinates for the swipe gesture
    end_x = start_x
    end_y = 100

    # initialize the old page source
    old_page_source = None

    # perform the swipe gesture until the end of page is reached
    while True:
        action = TouchAction(driver)
        action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()
        if old_page_source is not None and driver.page_source == old_page_source:
            break
        old_page_source = driver.page_source

    # Click see more button
    time.sleep(2)
    SeeMoreButton = find_my_element(driver, "XPATH", SEE_MORE_BUTTON)
    check_not_found(driver, SeeMoreButton, "See more button not found")
    SeeMoreButton.click()

    time.sleep(2)

    SeeMorePge = find_my_element(driver, "XPATH", SEE_MORE_PAGE)
    check_not_found(driver, SeeMorePge, "See more page not reached")

    # Click on home page
    HomeButton = find_my_element(driver, "XPATH", HEBTUS_BUTTON)
    check_not_found(driver, HomeButton, "Hebtus home button not found")
    HomeButton.click()
    time.sleep(2)
    # check if landing page is reached
    LandingPage = find_my_element(driver, "XPATH", LANDING_PAGE)
    check_not_found(driver, LandingPage, "Landing page not reached")

    time.sleep(10)
    print("See more test passed")
    driver.quit()


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


# ? Phase 5
def location_nearby_events_test(driver):
    # ---------------------------------------------- Testing Detection of geolocation ---------------------------------------------- #
    # Get the detected location
    # Get the screen dimensions
    screen_width = driver.get_window_size()["width"]
    screen_height = driver.get_window_size()["height"]
    # Scroll down using TouchAction
    swipe_action = TouchAction(driver)
    swipe_action.press(x=screen_width * 0.5, y=screen_height * 0.8).move_to(
        x=screen_width * 0.5, y=screen_height * 0.2
    ).release().perform()
    time.sleep(3)
    MyLocation = find_my_element(driver, "XPATH", LOCATION_TEXT)
    check_not_found(driver, MyLocation, "Location not found")
    # Check if it's correct
    # assert "Cairo" in MyLocation.get_attributte(
    #     "content-desc"
    # ), "Location not detected successfully"

    # scroll up
    swipe_action = TouchAction(driver)
    swipe_action.press(x=screen_width * 0.5, y=screen_height * 0.2).move_to(
        x=screen_width * 0.5, y=screen_height * 0.8
    ).release().perform()
    time.sleep(2)

    LocationTextbox = find_my_element(driver, "XPATH", LOCATION_PICKER_TB)
    check_not_found(driver, LocationTextbox, "Location textbox not found")
    LocationTextbox.click()
    time.sleep(3)
    LocationTextbox.send_keys("Alexandria")

    time.sleep(1)
    SearchButton = find_my_element(driver, "XPATH", SEARCH_BUTTON)
    check_not_found(driver, SearchButton, "Search button not found")
    SearchButton.click()
    time.sleep(2)
    # Scroll down using TouchAction
    swipe_action = TouchAction(driver)
    swipe_action.press(x=screen_width * 0.5, y=screen_height * 0.8).move_to(
        x=screen_width * 0.5, y=screen_height * 0.2
    ).release().perform()
    time.sleep(3)
    MyLocation = find_my_element(driver, "XPATH", LOCATION_TEXT)
    check_not_found(driver, MyLocation, "Location not found")
    # Check if it's correct
    # assert "Alexandria" in MyLocation.get_attributte(
    #     "content-desc"
    # ), "Location not detected successfully"

    # scroll up
    swipe_action = TouchAction(driver)
    swipe_action.press(x=screen_width * 0.8, y=screen_height * 0.2).move_to(
        x=screen_width * 0.8, y=screen_height * 0.8
    ).release().perform()
    time.sleep(3)
    # get back to current location
    DropDownMenu = find_my_element(driver, "XPATH", DROP_DOWN_MENU)
    DropDownMenu.click()
    time.sleep(1)
    MyCurrentLocation = find_my_element(driver, "XPATH", CURRENT_LOCATION_BUTTON)
    MyCurrentLocation.click()
    time.sleep(3)

    # Scroll down using TouchAction
    swipe_action = TouchAction(driver)
    swipe_action.press(x=screen_width * 0.5, y=screen_height * 0.8).move_to(
        x=screen_width * 0.5, y=screen_height * 0.2
    ).release().perform()
    time.sleep(3)
    MyLocation = find_my_element(driver, "XPATH", LOCATION_TEXT)
    check_not_found(driver, MyLocation, "Location not found")
    # Check if it's correct
    # assert "Cairo" in MyLocation.get_attributte(
    #     "content-desc"
    # ), "Location not detected successfully"
    print("Location test passed")
    time.sleep(3)
    driver.quit()


# ? phase 5
def GetEventsDate(driver):
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
            check_not_found(driver, Event, "Event Not Found")
            time.sleep(2)
            ContentSet.add(Event.get_attribute("content-desc"))
            # print(Event.get_attribute("content-desc"))
            # print(str(i) + ": ------------------------------")
        if old_page_source is not None and driver.page_source == old_page_source:
            break
        old_page_source = driver.page_source
    # print(ContentSet)
    DateSet = set()
    for event in ContentSet:
        EventsInfo = event.split("\n")
        Date = EventsInfo[1].split(" ")[0]
        DateSet.add(Date)
    return DateSet


# ? Phse 5
def today_tab_test(driver):
    # ---------------------------------------------- Testing today tab ---------------------------------------------- #
    # Swipe right using TouchAction
    # Swipe from the center of the element to the top of the screen
    start_x = 948.0
    start_y = 1149.5
    end_x = 280
    end_y = 1149.5
    swipe_action = TouchAction(driver)
    swipe_action.press(x=start_x, y=start_y).wait(700).move_to(
        x=end_x, y=end_y
    ).release().perform()
    time.sleep(3)
    # click on Today tab
    TodayTab = find_my_element(driver, "XPATH", TODAY_TAB)
    check_not_found(driver, TodayTab, "Today tab not found")
    TodayTab.click()
    time.sleep(3)

    DateSet = GetEventsDate(driver)
    print(DateSet)
    for Date in DateSet:
        Date = Date.split("-")
        Date = date(int(Date[0]), int(Date[1]), int(Date[2]))
        assert date.today() >= Date, "Not all events are today"
    print("Today tab test passed")
    driver.quit()


# ? Phase 5
def is_this_weekend(StartDate):
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
        return StartDate <= Weekend1
    else:
        return StartDate <= Weekend1 and StartDate <= Weekend2


# ? Phase 5
def this_weekend_tab_test(driver):
    # ---------------------------------------------- Testing this weekend tab ---------------------------------------------- #
    start_x = 948.0
    start_y = 1149.5
    end_x = 280
    end_y = 1149.5
    swipe_action = TouchAction(driver)
    swipe_action.press(x=start_x, y=start_y).wait(700).move_to(
        x=end_x, y=end_y
    ).release().perform()
    time.sleep(3)

    # click on this weekend tab
    WeekendTab = find_my_element(driver, "XPATH", THIS_WEEKEND_TAB)
    check_not_found(driver, WeekendTab, "This weekend tab not found")
    WeekendTab.click()
    time.sleep(3)

    DateSet = GetEventsDate(driver)
    print(DateSet)
    for Date in DateSet:
        Date = Date.split("-")
        Date = date(int(Date[0]), int(Date[1]), int(Date[2]))
        assert is_this_weekend(Date), "Not all events are this weekend"

    print("This weekend tab test passed")
    time.sleep(2)
    driver.quit()


# ? phase 5
def is_free(driver):
    GetTicketButton = find_my_element(driver, "XPATH", GET_TICKET_BUTTON)
    check_not_found(driver, GetTicketButton, "Get ticket button not found")
    GetTicketButton.click()
    time.sleep(2)
    # check if there is free tickets section
    TicketsType = find_my_element(driver, "XPATH", TICKETS_TYPES)
    check_not_found(driver, TicketsType, "Tickets type section not found")
    assert "Free tickets" in TicketsType.get_attribute(
        "content-desc"
    ), "Not all events are Free"
    # click back button to return
    location = TicketsType.location
    # Get the X and Y coordinates of the top-left corner of the element
    x = location["x"]
    y = location["y"]
    # Create a TouchAction object
    action = TouchAction(driver)
    # Perform a tap at the specified position
    action.tap(x=x, y=y).perform()

    # click leave button
    LeaveButton = find_my_element(driver, "XPATH", LEAVE_BUTTON)
    check_not_found(driver, LeaveButton, "Leave button not found")
    LeaveButton.click()


# ? phase 5
def free_tab_test(driver):
    # ---------------------------------------------- Testing free tab ---------------------------------------------- #
    start_x = 948.0
    start_y = 1149.5
    end_x = 280
    end_y = 1149.5
    swipe_action = TouchAction(driver)
    swipe_action.press(x=start_x, y=start_y).wait(700).move_to(
        x=end_x, y=end_y
    ).release().perform()
    time.sleep(3)

    # click on Free tab
    FreeTab = find_my_element(driver, "XPATH", FREE_TAB)
    check_not_found(driver, FreeTab, "Free tab not found")
    FreeTab.click()
    time.sleep(3)

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
        end = True
        for i in range(count):
            EVENT = EVENT_1 + str(i) + EVENT_2
            Event = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((AppiumBy.XPATH, EVENT))
            )
            # Event = find_my_element(driver, "XPATH", EVENT)
            time.sleep(2)
            print(Event.get_attribute("content-desc"))
            print(str(i) + ": ------------------------------")
            Event.click()
            is_free(driver)
            time.sleep(2)
            # get back to home page
            # Click on home page
            HomeButton = find_my_element(driver, "XPATH", HEBTUS_BUTTON)
            check_not_found(driver, HomeButton, "Hebtus home button not found")
            HomeButton.click()
            time.sleep(2)
            # click on free tab again
            swipe_action = TouchAction(driver)
            swipe_action.press(x=start_x, y=start_y).wait(700).move_to(
                x=end_x, y=end_y
            ).release().perform()
            time.sleep(3)

            # click on Free tab
            FreeTab = find_my_element(driver, "XPATH", FREE_TAB)
            check_not_found(driver, FreeTab, "Free tab not found")
            FreeTab.click()
            time.sleep(3)
            # navigate to the same position by scrolling as much as j*2
            for k in range(2 * (j + 1)):
                # Scroll down using TouchAction
                swipe_action = TouchAction(driver)
                swipe_action.press(x=screen_width * 0.5, y=screen_height * 0.8).move_to(
                    x=screen_width * 0.5, y=screen_height * 0.2
                ).release().perform()
                time.sleep(3)
        if (
            old_page_source is not None and driver.page_source == old_page_source
        ) or end:
            break
        old_page_source = driver.page_source

    print("Free tab test passed")
    driver.quit()
