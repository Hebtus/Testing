# To give us access to the enter key, escape key...etc. ex: when I write something in the search bar and want to press enter:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

import sys
sys.path.append(".") # To access modules in sibling directories

from Common_Files.Utilities import *
from Common_Files.RealReferences import *



def basic_info(driver, mode = 0):
    # ----------------------------------- Make a list of testcases for each field ------------------------------------------- #

    F = open("./Test_Cases/EventTitleTestCases.txt", "r")
    EventTitles = [EventTitle.rstrip("\n") for EventTitle in F.readlines()]
    F.close()

    F = open("./Test_Cases/TagsTestCases.txt", "r")
    Tags = [Tag.rstrip("\n") for Tag in F.readlines()]
    F.close()

    # Navigate to basic info page
    CreateEvent = find_my_element(driver,"ID",CREATE_EVENT_BUTTON)
    CreateEvent.click()
    time.sleep(5)

    if mode == 0: # Normal operation
        print("Normal")
    
    elif mode==1: # Testing operation

        # ---------------------------------------------- Testing Event Title Field ---------------------------------------------- #
        EventTitleField = find_my_element(driver, "ID", EVENT_TITLE_FIELD)
        # Test 1: Entering more than 75 characters
        EventTitleField.click()
        EventTitleField.send_keys(EventTitles[1])
        # Retrieve the text inside the textbox to check that only 75 characters were wrtten
        if len(EventTitleField.get_attribute("value")) != 75:
            print(
                "Error: Case of 75 character as maximum limit for Event Title field not handled"
            )
        time.sleep(3)
        # Test 2: Empty string and all other fields filled (except tags since not mandatory) (performed later, before save and continue) 

        # ---------------------------------------------- Testing Type, Category and Sub-Category Fields ---------------------------------------------- #
        # Test 0 Options are available to select from
        TypeField=find_my_element(driver,"ID",EVENT_TYPE_DROPDOWN_FIELD)
        CategoryField=find_my_element(driver,"ID",EVENT_CATEGORY_DROPDOWN_FIELD)
        SubCategoryField=find_my_element(driver,"ID",EVENT_SUBCATEGORY_DROPDOWN_FIELD)
        TypeField.click()
        time.sleep(1)
        TypeOptions = find_my_elements(driver,"XPATH",TYPE_OPTIONS)
        if(len(TypeOptions) == 1):
            print("Error: no options to choose from for type")
        
        CategoryField.click()
        time.sleep(1)
        CategoryOptions = find_my_elements(driver,"XPATH",CATEGORY_OPTIONS)
        if(len(CategoryOptions) == 1):
            print("Error: no options to choose from for category")
        
        SubCategoryField.click()
        time.sleep(1)
        SubCategoryOptions = find_my_elements(driver,"XPATH",SUBCATEGORY_OPTIONS)
        if(len(SubCategoryOptions) == 1):
            print("Error: no options to choose from for subcategory")

        # Test 1 selecting category
        CategoryField.click()
        time.sleep(1)
        drp = Select(CategoryField)
        time.sleep(1)
        drp.select_by_visible_text("Music")
        time.sleep(1)
        
        # -------------------------------------------------- Testing Tags Field ------------------------------------------------- #
        TagsField = find_my_element(driver, "ID", TAGS_FIELD)
        AddTag = find_my_element(driver,"ID",ADD_TAG)

        # ---------- Test 1: Entering more than 25 characters ---------- #
        time.sleep(2)
        TagsField.click()
        time.sleep(1)
        TagsField.send_keys(Tags[0])
        # Retrieve the text inside the textbox to check that only 25 characters were wrtten
        if len(TagsField.get_attribute("value")) != 25:
            print(
                "Error: Case of 25 character as maximum limit for Tags field not handled"
            )

        time.sleep(4)
        my_clear(TagsField)

        # ---------- Test 2 : Entering 10 tags (should display: "10/10 tag limit reached.") ---------- #
        time.sleep(3)
        # Enter 10 tags
        for i in range(1, 11):
            TagsField.send_keys(Tags[i])
            time.sleep(1)
            AddTag.click()
            time.sleep(1)

        # Retrieve tags to check if they are 10 indeed
        TagsRetrievals= find_my_elements(driver,"XPATH",ALL_TAGS)

        if len(TagsRetrievals) != 10:
            print("Error: Entered 10 tags and retrived ", str(len(TagsRetrievals)), " tags instead.")
        
        # ---------- Test 3 : Tags field area accepting more than 10 tags (tag entered should not be inserted and tag field is cleared) ---------- #
        time.sleep(3)
        TagsField.send_keys(Tags[11])
        time.sleep(1)
        AddTag.click()
        TagMsg = find_my_element(driver,"XPATH",TAG_ERROR_MSG)
        assert TagMsg.text == "You can only choose 10 tags." # if condition not true then this line will produce AssertionError
        TagsRetrievals= find_my_elements(driver,"XPATH",ALL_TAGS)
        # check if tag field area had any changes
        if(len(TagsRetrievals) != 10):
            print("Error: Tags field area accepted more than 10 tags")
        time.sleep(2)
        while(len(TagsField.get_attribute("value"))>0):
            TagsField.send_keys(Keys.BACK_SPACE)
        AddTag.click()
        time.sleep(3)

        # ---------- Test 4: Delete a tag ---------- #
        DeleteTag = find_my_element(driver,"ID",Tags[1])
        DeleteTag.click()
        TagsRetrievals= find_my_elements(driver,"XPATH",ALL_TAGS)
        if(len(TagsRetrievals)!=9):
            print("Error: failed to delete a tag")

        # ---------- Test 5: replicate a tag (should display: "Tag already exists." and not clear tag field)---------- #
        TagsField.send_keys(Tags[8])
        time.sleep(1)
        AddTag.click()
        TagMsg = find_my_element(driver,"XPATH",TAG_ERROR_MSG)
        assert TagMsg.text == "This tag is already choosen." # if condition not true then this line will produce AssertionError
        TagsRetrievals= find_my_elements(driver,"XPATH",ALL_TAGS)
        if(len(TagsRetrievals)!=9):
            print("Error: Added duplicate tag to tag area")
        
        # ---------- Test 6: Tags containing special characters or spaces (should display: "Only letters, numbers and underscores are allowed.") ---------- #
        time.sleep(3)
        for i in range(13, 18):
            while(len(TagsField.get_attribute("value"))>0):
                TagsField.send_keys(Keys.BACK_SPACE)
            TagsField.send_keys(Tags[i])
            time.sleep(1)
            AddTag.click()  # Enter is refered to as return
            time.sleep(1)
            TagMsg=find_my_element(driver,"XPATH",TAG_ERROR_MSG)
            # check if message is displayed
            assert TagMsg.text == "Only letters, numbers and underscores are allowed." # if condition not true then this line will produce AssertionError
            TagsRetrievals= find_my_elements(driver,"XPATH",ALL_TAGS)
            # check if tag field area had any changes
            if(len(TagsRetrievals)!=9):
                print("Error: Tags field area accepted tags with special characters or spaces")
                
        # ---------- Test 7: Delete all tags ---------- #
        time.sleep(3)
        for i in range(2, 11):
            DeleteTag = find_my_element(driver,"ID",Tags[i])
            DeleteTag.click()
            time.sleep(1)
        try:
            TagsRetrievals= find_my_elements(driver,"XPATH",ALL_TAGS)
            print("Error: failed to delete all tags")
        except:
            print("Success: Was able to delete all tags")

        # ------------------------------------------------- Testing Location Field ------------------------------------------------ #
        time.sleep(1)
        VenueButton=find_my_element(driver,"XPATH",VENUE_BUTTON)
        VenueButton.click()
        OnlineButton =find_my_element(driver,"XPATH",ONLINE_BUTTON)
        time.sleep(1)
        OnlineButton.click()
        TBAButton =find_my_element(driver,"XPATH",TO_BE_ANNOUNCED_BUTTON)
        time.sleep(1)
        TBAButton.click()
        if(VenueButton.is_enabled() == False):
            print("Error: Venue button for location is not clickable")
        if(OnlineButton.is_enabled() == False):
            print("Error: Online button for location is not clickable")
        if(TBAButton.is_enabled() == False):
            print("Error: To be annlounced button for location is not clickable")
        time.sleep(2)

        # ----------------------------------------- Testing Dates of Event -------------------------------- #
        # Scroll to location field since it would show event date area clearly
        DateAndTimeTitle=find_my_element(driver,"XPATH",DATE_AND_TIME_TITLE)
        driver.execute_script("arguments[0].scrollIntoView();",DateAndTimeTitle)
        time.sleep(2)

        # ---- Test 1: Event start date is after Event end date ----- #
        StartDateField = find_my_element(driver,"ID",EVENT_START_DATE_FIELD)
        EndDateField=find_my_element(driver,"ID",EVENT_END_DATE_FIELD)
        StartTimeField = find_my_element(driver,"ID",EVENT_START_TIME_FIELD)
        EndTimeField=find_my_element(driver,"ID",EVENT_END_TIME_FIELD)

        my_clear(StartDateField)
        time.sleep(1) 
        StartDateField.click()
        StartDateField.send_keys("07/26/2023")
        time.sleep(1) 
        EndDateField.click()
        my_clear(EndDateField)
        time.sleep(1) 
        EndDateField.send_keys("07/24/2023")
        time.sleep(2) 

        # assert that error message is displayed
        DateErrorMsg = find_my_element(driver,"XPATH",EVENT_START_DATE_MSG)
        assert DateErrorMsg.text == "End date must be after start date."

        DateErrorMsg = find_my_element(driver,"XPATH",EVENT_END_DATE_MSG)
        assert DateErrorMsg.text == "End date must be after start date."
        
        # Put dates correctly so message dissapears
        my_clear(StartDateField)
        time.sleep(1) 
        StartDateField.click()
        StartDateField.send_keys("05/19/2023")
        time.sleep(1) 
        my_clear(EndDateField)
        time.sleep(1) 
        EndDateField.click()
        EndDateField.send_keys("05/19/2023")
        time.sleep(3)

        # ----------------------------------------- Testing Check boxes for display time -------------------------------- #
        DisplayStart = find_my_element(driver,"XPATH",DISPLAY_START_TIME)
        if(DisplayStart.is_enabled() == False):
            print("Error: cannot interact with display start time checkbox")
        DisplayStart.click()
        if(DisplayStart.is_selected() == False):
            print("Error: Failed to select display start time checkbox")
        time.sleep(1)
        DisplayStart.click()
        if(DisplayStart.is_selected() == True):
            print("Error: Failed to unselect display start time checkbox")
        time.sleep(1)

        DisplayEnd = find_my_element(driver,"XPATH",DISPLAY_END_TIME)
        if(DisplayEnd.is_enabled() == False):
            print("Error: cannot interact with display end time checkbox")
        DisplayEnd.click()
        if(DisplayEnd.is_selected() == False):
            print("Error: Failed to select display end time checkbox")
        time.sleep(1)
        DisplayEnd.click()
        if(DisplayEnd.is_selected() == True):
            print("Error: Failed to unselect display end time checkbox")