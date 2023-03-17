# To give us access to the enter key, escape key...etc. ex: when I write something in the search bar and want to press enter:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import sys
sys.path.append(".") # To access modules in sibling directories

from Common_Files.Utilities import *
from Common_Files.RealReferences import *



def basic_info(driver):
    # ----------------------------------- Make a list of testcases for each field ------------------------------------------- #

    F = open("./Test_Cases/EventTitleTestCases.txt", "r")
    EventTitles = [EventTitle.rstrip("\n") for EventTitle in F.readlines()]
    F.close()

    F = open("./Test_Cases/TagsTestCases.txt", "r")
    Tags = [Tag.rstrip("\n") for Tag in F.readlines()]
    F.close()

    # ---------------------------------------------- Testing Event Title Field ---------------------------------------------- #
    EventTitleField = find_my_element(driver, "ID", EVENT_TITLE_FIELD)
    # Test 1: Entering more than 75 characters
    EventTitleField.send_keys(EventTitles[1])
    # Retrieve the text inside the textbox to check that only 75 characters were wrtten
    if len(EventTitleField.get_attribute("value")) != 75:
        print(
            "Error: Case of 75 character as maximum limit for Event Title field not handled"
        )

    # Test 2: Empty string and all other fields filled (can be joined with normal operation test)

    # -------------------------------------------------- Testing Tags Field ------------------------------------------------- #
    TagsField = find_my_element(driver, "ID", TAGS_FIELD)
    # Test 1: Entering more than 25 characters
    TagsField.send_keys(Tags[0])
    # Retrieve the text inside the textbox to check that only 25 characters were wrtten
    if len(TagsField.get_attribute("value")) != 25:
        print(
            "Error: Case of 25 character as maximum limit for Tags firled not handled"
        )

    time.sleep(1)
    TagsField.send_keys(Keys.CONTROL, "a")
    TagsField.send_keys(Keys.BACKSPACE)

    # Test 2 : Entering 10 tags (should display: "10/10 tag limit reached.")
    for i in range(1, 11):
        TagsField.send_keys(Tags[i])
        time.sleep(1)
        TagsField.send_keys(Keys.RETURN)  # Enter is refered to as return
        time.sleep(1)

    # Test 3: Delete a tag

    # Test 4: replicate a tag

    # Test 5: Tags containing special characters or spaces (should display: "Tags can only contain letters, numbers, and underscores.")






    # Venue = find_my_element(driver,"XPATH", "//label[for=segmented-venueType-1]")
    # Venue = driver.find_element(By.XPATH, "//label[@for='segmented-venueType-1']")
    # Venue.click()
    # for EventTitle in EventTitles:
    #   EventTitleField.send_keys(EventTitle)
    #  time.sleep(1)
    # EventTitleField.send_keys(Keys.CONTROL, "a")
    # EventTitleField.send_keys(Keys.BACKSPACE)
    # time.sleep(1)
