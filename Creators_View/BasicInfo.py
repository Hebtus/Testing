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

    # ---------------------------------------------------- Finding Fields --------------------------------------------------- #
    EventTitleField = find_my_element(driver, "ID", EVENT_TITLE_FIELD)
    TagsField = find_my_element(driver, "ID", TAGS_FIELD)
    OrganizerField = find_my_element(driver,"ID",ORGANIZER_DROPDOWN_FIELD)
    TypeField=find_my_element(driver,"ID",EVENT_TYPE_DROPDOWN_FIELD)
    CategoryField=find_my_element(driver,"ID",EVENT_CATEGORY_DROPDOWN_FIELD)
    StartDateField = find_my_element(driver,"ID",EVENT_START_DATE_FIELD)
    EndDateField=find_my_element(driver,"ID",EVENT_END_DATE_FIELD)
    StartTimeField = find_my_element(driver,"ID",EVENT_START_TIME_FIELD)
    EndTimeField=find_my_element(driver,"ID",EVENT_END_TIME_FIELD)

    if mode == 0: # Normal operation
        EventTitleField.send_keys(EventTitles[0])
        time.sleep(1)
        drp = Select(OrganizerField)
        drp.select_by_visible_text("malak")
        time.sleep(1)
        drp = Select(TypeField)
        drp.select_by_visible_text("Concert or Performance")
        drp = Select(CategoryField)
        time.sleep(1)
        drp.select_by_visible_text("Music")
        time.sleep(1)
        SubCategoryField=find_my_element(driver,"ID",EVENT_SUBCATEGORY_DROPDOWN_FIELD)
        drp = Select(SubCategoryField)
        time.sleep(1)
        drp.select_by_visible_text("Rock")  
        for i in range(1, 4):
                TagsField.send_keys(Tags[i])
                time.sleep(1)
                TagsField.send_keys(Keys.RETURN)  # Enter is refered to as return
                time.sleep(1)
        LocationTitle=find_my_element(driver,"XPATH",VENUE_LOCATION_TITLE)
        OnlineEventButton=find_my_element(driver,"XPATH",ONLINE_EVENT_BUTTON_FIELD)
        driver.execute_script("arguments[0].scrollIntoView();",LocationTitle)
        time.sleep(1)
        OnlineEventButton.click()
        time.sleep(1) 
        my_clear(StartDateField)
        time.sleep(1) 
        StartDateField.send_keys("06/24/2023")
        StartDateField.click()
        time.sleep(1) 
        my_clear(EndDateField)
        time.sleep(1) 
        EndDateField.send_keys("06/26/2023")
        EndDateField.click()
        time.sleep(1) 
        my_clear(StartTimeField)
        time.sleep(1) 
        StartTimeField.send_keys("5:30 PM")
        StartTimeField.send_keys(Keys.RETURN)
        time.sleep(1) 
        my_clear(EndTimeField)
        time.sleep(1) 
        EndTimeField.send_keys("10:00 PM")
        EndTimeField.send_keys(Keys.RETURN)
        time.sleep(1) 
        DateAndTimeTitle = find_my_element(driver,"XPATH",DATE_AND_TIME_TITLE)
        driver.execute_script("arguments[0].scrollIntoView();",DateAndTimeTitle)
        time.sleep(1)
        SaveAndContinueButton=find_my_element(driver,"XPATH",SAVE_AND_CONTINUE_BUTTON)
        SaveAndContinueButton.click()
            #UploadImageButton=find_my_element(driver,"XPATH",UPLOAD_IMAGE_BUTTON)
            #UploadImageButton.click()
            #Upload images
        SummaryTitle = find_my_element(driver,"XPATH", EVENT_SUMMARY_TITLE)
        driver.execute_script("arguments[0].scrollIntoView();",SummaryTitle)
        SummaryField = find_my_element(driver,"ID",EVENT_SUMMARY_FIELD)
        SummaryField.send_keys(EventTitles[2])
        time.sleep(1)
        AddMoreTitle = find_my_element(driver, "XPATH", ADD_MORE_TITLE)
        driver.execute_script("arguments[0].scrollIntoView();",AddMoreTitle)
        SaveAndContinueButton.click()


        


    
    elif mode==1: # Testing operation
        # ---------------------------------------------- Testing Event Title Field ---------------------------------------------- #

        # Test 1: Entering more than 75 characters
        EventTitleField.send_keys(EventTitles[1])
        # Retrieve the text inside the textbox to check that only 75 characters were wrtten
        if len(EventTitleField.get_attribute("value")) != 75:
            print(
                "Error: Case of 75 character as maximum limit for Event Title field not handled"
            )
        
        # Test 2: Empty string and all other fields filled (except tags since not mandatory) (performed later, before save and continue) 
        
        # Select organizer, no testing since only one option
        drp = Select(OrganizerField)
        drp.select_by_visible_text("malak")
        time.sleep(1)

        # ---------------------------------------------- Testing Type, Category and Sub-Category Fields ---------------------------------------------- #
        # Test 1 selecting a type, category and subcategory then changing them
        drp = Select(TypeField)
        drp.select_by_visible_text("Conference")
        drp = Select(CategoryField)
        time.sleep(1)
        drp.select_by_visible_text("Fashion & Beauty")
        time.sleep(1)
        SubCategoryField=find_my_element(driver,"ID",EVENT_SUBCATEGORY_DROPDOWN_FIELD)
        drp = Select(SubCategoryField)
        time.sleep(1)
        drp.select_by_visible_text("Accessories") 
        time.sleep(1)
        drp = Select(TypeField)
        drp.select_by_visible_text("Concert or Performance")
        drp = Select(CategoryField)
        time.sleep(1)
        drp.select_by_visible_text("Music")
        time.sleep(1)
        SubCategoryField=find_my_element(driver,"ID",EVENT_SUBCATEGORY_DROPDOWN_FIELD)
        drp = Select(SubCategoryField)
        time.sleep(1)
        drp.select_by_visible_text("Rock")
        time.sleep(1) 
        #print(CategoryField.text)
        #print(TypeField.text)
        #print(SubCategoryField.text)
        #if((TypeField.text != "Concert or Performance") or (CategoryField.text != "Music") or (SubCategoryField.text != "Rock")):
         #   print("Error: Unable to change Type or Category or Sub-category after choosing it")
        
        # Test 2 Type, category and subcategory selected, changing category (sub-category must be de-selected)
        drp = Select(CategoryField)
        time.sleep(1)
        drp.select_by_visible_text("Science & Technology")
        if SubCategoryField.is_selected():
            print("Error: Case when Category and Subcategory are chosen and then changing Category does not de-select Subcategory")

        # -------------------------------------------------- Testing Tags Field ------------------------------------------------- #
        driver.execute_script(SCROLL_AMOUNT_FOR_TAG,"")
        # ---------- Test 1: Entering more than 25 characters ---------- #
        time.sleep(3)
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
            TagsField.send_keys(Keys.RETURN)  # Enter is refered to as return
            time.sleep(1)

        # Retrieve tags to check if they are 10 indeed
        TagsRetrieval= find_my_element(driver,"XPATH",TAGS_INSERTED_FIELD)
        TagsRetrievals= (TagsRetrieval.text).split("\n")

        if len(TagsRetrievals) != 10:
            print("Error: Entered 10 tags and retrived ", str(len(TagsRetrievals)), " tags instead.")
        
        # check if message is displayed
        TagMsg = find_my_element(driver,"XPATH",TAG_ERROR_MSG)
        assert TagMsg.text == "10/10 tag limit reached." # if condition not true then this line will produce AssertionError

        # Print 10 tags in console (un-comment next 2 lines)
        #for TagRetrieval in TagsRetrievals:
        #    print(TagRetrieval)

        # ---------- Test 3 : Tags field area accepting more than 10 tags (tag entered should not be inserted and tag field is cleared) ---------- #
        time.sleep(3)
        TagsField.send_keys(Tags[11])
        time.sleep(1)
        TagsField.send_keys(Keys.RETURN)
        TagsRetrieval2= find_my_element(driver,"XPATH",TAGS_INSERTED_FIELD)
        # check if tag field area had any changes
        if(TagsRetrieval.text != TagsRetrieval2.text):
            print("Error: Tags field area accepted more than 10 tags")
        # check tags field is cleared out
        if(len(TagsField.get_attribute("value"))!=0):
            print("Error: Tags field not cleared out after insertion of 11th tag")

        # ---------- Test 4: Delete a tag ---------- #
        time.sleep(3)
        DeleteTags = find_my_elements(driver,"XPATH",TAGS_DELETE_BASE)
        DeleteTags[4].click()
        DeleteTags = find_my_elements(driver,"XPATH",TAGS_DELETE_BASE)
        if(len(DeleteTags)!=9):
            print("Error: failed to delete a tag")

        # ---------- Test 5: replicate a tag (should display: "Tag already exists." and not clear tag field)---------- #
        time.sleep(3)
        TagsRetrieval= find_my_element(driver,"XPATH",TAGS_INSERTED_FIELD) # tag field area before performing test 5
        TagsField.send_keys(Tags[12]) # music
        time.sleep(1)
        TagsField.send_keys(Keys.RETURN)
        TagMsg=find_my_element(driver,"XPATH",TAG_ERROR_MSG)
        # check if message is displayed
        assert TagMsg.text == "Tag already exists." # if condition not true then this line will produce AssertionError
        # check that tag field is not cleared
        if(len(TagsField.get_attribute("value"))==0):
            print("Error: tag field should not have been cleared after entering replicated tag")
        # check that replicated tag was not added in tags field area
        TagsRetrieval2= find_my_element(driver,"XPATH",TAGS_INSERTED_FIELD)
        if(TagsRetrieval.text != TagsRetrieval2.text):
            print("Error: Tags field area replicated tag")

        # ---------- Test 6: Tags containing special characters or spaces (should display: "Tags can only contain letters, numbers, and underscores.") ---------- #
        time.sleep(3)
        my_clear(TagsField)
        time.sleep(1)
        for i in range(13, 18):
            TagsField.send_keys(Tags[i])
            time.sleep(1)
            TagsField.send_keys(Keys.RETURN)  # Enter is refered to as return
            time.sleep(1)
            TagMsg=find_my_element(driver,"XPATH",TAG_ERROR_MSG)
            # check if message is displayed
            assert TagMsg.text == "Tags can only contain letters, numbers, and underscores." # if condition not true then this line will produce AssertionError
            TagsRetrieval2= find_my_element(driver,"XPATH",TAGS_INSERTED_FIELD)
            # check if tag field area had any changes
            if(TagsRetrieval.text != TagsRetrieval2.text):
                print("Error: Tags field area accepted tags with special characters or spaces")
            # check tags field is cleared out
            if(len(TagsField.get_attribute("value"))!=0):
                print("Error: Tags field not cleared out after insertion tag with special characters")

        # ---------- Test 7: Delete all tags ---------- #
        time.sleep(3)
        for i in range(0, len(DeleteTags)):
            time.sleep(1)
            DeleteTags[i].click()
        #try:
            #DeleteTags = driver.find_elements(By.XPATH,TAGS_DELETE_BASE)
            #print("Error: failed to delete all tags")
        #except:
            #print("Success: Was able to delete all tags")

        # ------------------------------------------------- Testing Location Field ------------------------------------------------ #
        # Scroll to location field
        LocationTitle=find_my_element(driver,"XPATH",VENUE_LOCATION_TITLE)
        driver.execute_script("arguments[0].scrollIntoView();",LocationTitle)
        # Venue
        VenueField=find_my_element(driver,"ID",VENUE_LOCATION_FIELD)
        driver.execute_script("arguments[0].scrollIntoView();",VenueField)
        if VenueField.is_enabled() == False:
            print("Error: Venue location field is not enabled")
        time.sleep(1)
        VenueField.send_keys("Agouza, Egypt")
        time.sleep(1)
        VenueField.send_keys(Keys.BACK_SPACE)
        VenueFieldChoice = find_my_element(driver,"XPATH",VENUE_OPTION_ONE_BUTTON)
        VenueFieldChoice.click()
        # Test 1 checking if Address 1 field and postal code field are enabled
        VenueAddress1=find_my_element(driver,"XPATH",VENUE_ADDRESS1_FIELD)
        PostalCode=find_my_element(driver,"ID",VENUE_POSTAL_CODE_FIELD)
        if VenueAddress1.is_enabled() == False:
            print("Error: Address 1 field is not enabled")
        if PostalCode.is_enabled() == False:
            print("Error: Postal code field is not enabled")
        
        # Test 2 Address 1 mandatory (should display "Address 1 is required.")
        # Case 1
        # Clicking on Address 1 field and not writing anything
        VenueAddress1.click()
        time.sleep(1)
        # Then clicking somewhere else 
        VenueAddress2=find_my_element(driver,"XPATH",VENUE_ADDRESS2_FIELD)
        VenueAddress2.click()
        time.sleep(1)
        # check that error message appears
        AddressErrorMsg = find_my_element(driver,"XPATH",VENUE_ADDRESS1_ERROR_MSG)
        assert AddressErrorMsg.text == "Address 1 is required." # if condition not true then this line will produce AssertionError 
        # Case 2
        # Clicking on Address 1 field writing something
        VenueAddress1.click()
        time.sleep(1)
        VenueAddress1.send_keys("test text")
        time.sleep(1)
        # Clicking somewhere else
        VenueAddress2.click()
        time.sleep(1)
        # Clicking again on address 1, deleting what is written
        VenueAddress1.click()
        time.sleep(1)
        my_clear(VenueAddress1)
        # And then clicking somewhere else
        VenueAddress2.click()
        # check that error message appears
        AddressErrorMsg = find_my_element(driver,"XPATH",VENUE_ADDRESS1_ERROR_MSG)
        assert AddressErrorMsg.text == "Address 1 is required." # if condition not true then this line will produce AssertionError
        # Write in Address 1 Normally
        VenueAddress1.send_keys("38 Mahmoud Khalil Al Housarei")
        # Test 3 Not filling Postal Code
        # Case 1
        # Clicking on Postal Code field and not writing anything
        PostalCode.click()
        time.sleep(1)
        # Then clicking somewhere else 
        VenueAddress2.click()
        time.sleep(1)
        # check that error message appears
        PostalCodeErrorMsg = find_my_element(driver,"XPATH",VENUE_POSTAL_CODE_ERROR_MSG)
        assert PostalCodeErrorMsg.text == "ZIP code is required." # if condition not true then this line will produce AssertionError
        # Case 2
        # Clicking on Postal Code field writing something
        PostalCode.click()
        time.sleep(1)
        PostalCode.send_keys("1")
        time.sleep(1)
        # Clicking somewhere else
        VenueAddress2.click()
        time.sleep(1)
        # Clicking again on Postal Code field, deleting what is written
        PostalCode.click()
        time.sleep(1)
        my_clear(PostalCode)
        # And then clicking somewhere else
        VenueAddress2.click()
        # check that error message appears
        PostalCodeErrorMsg = find_my_element(driver,"XPATH",VENUE_POSTAL_CODE_ERROR_MSG)
        assert PostalCodeErrorMsg.text == "ZIP code is required." # if condition not true then this line will produce AssertionError
        # Write in Postal Code Normally
        PostalCode.send_keys("12654")
        time.sleep(1)
        # Test 4 check if all other fields are enabled
        CityField=find_my_element(driver,"ID",VENUE_CITY_FIELD)
        if CityField.is_enabled() == False:
            print("Error: City field is not enabled")
        StateField=find_my_element(driver,"ID",VENUE_STATE_FIELD)
        if StateField.is_enabled() == False:
            print("Error: State field is not enabled")
        CountryField=find_my_element(driver,"ID",VENUE_COUNTRY_FIELD)
        if CountryField.is_enabled() == False:
            print("Error: Country field is not enabled")
        SearchLocation=find_my_element(driver,"XPATH",VENUE_LOCATION_BUTTON_FIELD)
        if SearchLocation.is_enabled() == False:
            print("Error: Search location button is not enabled")

        # Test 5: clicking on search location button takes me back to previous tab
        SearchLocation.click()
        time.sleep(1)
        if SearchLocation.is_displayed() == False:
            print("Error: clicking on search location button did not take me back")
        time.sleep(4)
  
        # To be announced
        ToBeAnnounced = find_my_element(driver,"XPATH",VENUE_TO_BE_ANNOUNCED_BUTTON)
        ToBeAnnounced.click()
        time.sleep(1)

        # Online event
        OnlineEventButton=find_my_element(driver,"XPATH",ONLINE_EVENT_BUTTON_FIELD)
        OnlineEventButton.click()
        time.sleep(1)

        # Clicking on Venue option, leaving it empty and clicking on save and continue at the end (NOT ALWAYS HANDLED BY EVENTBRITE)
        VenueButton=find_my_element(driver,"XPATH",VENUE_LOCATION_BUTTON_FIELD)
        VenueButton.click()
        time.sleep(2)
        VenueField=find_my_element(driver,"ID",VENUE_LOCATION_FIELD)
        my_clear(VenueField)
        time.sleep(1)
        VenueField.send_keys(Keys.RETURN)
        #time.sleep(2)
        #SaveAndContinueButton=find_my_element(driver,"XPATH",SAVE_AND_CONTINUE_BUTTON)
        #driver.execute_script("arguments[0].scrollIntoView();",SaveAndContinueButton)
        #SaveAndContinueButton.click()
        #VenueErrorMsg = find_my_element(driver,"XPATH",VENUE_ERROR_MSG)
        #assert VenueErrorMsg.get_attribute('innerHTML') == "Location is required."

        # ----------------------------------------- Testing Dates of Event -------------------------------- #
        # Scroll to location field since it would show event date area clearly
        LocationTitle=find_my_element(driver,"XPATH",VENUE_LOCATION_TITLE)
        driver.execute_script("arguments[0].scrollIntoView();",LocationTitle)
        # Test 1: Event start date is after Event end date
        my_clear(StartDateField)
        time.sleep(1) 
        StartDateField.send_keys("07/26/2023")
        StartDateField.click()
        time.sleep(1) 
        my_clear(EndDateField)
        time.sleep(1) 
        EndDateField.send_keys("07/24/2023")
        EndDateField.click()
        time.sleep(1) 
        # send keys somewhere else
        my_clear(StartTimeField)
        time.sleep(1) 
        StartTimeField.send_keys("5:30 PM")
        StartTimeField.send_keys(Keys.RETURN)
        time.sleep(1) 
        # assert that error message is displayed
        DateErrorMsg = find_my_element(driver,"XPATH",EVENT_START_DATE_MSG)
        assert DateErrorMsg.get_attribute('innerHTML') == "End date must be after start date."

        DateErrorMsg = find_my_element(driver,"XPATH",EVENT_END_DATE_MSG)
        assert DateErrorMsg.get_attribute('innerHTML') == "End date must be after start date."

        # Test 2: same day start hour after end hour
        my_clear(StartDateField)
        time.sleep(1) 
        StartDateField.send_keys("07/24/2023")
        StartDateField.click()
        time.sleep(1) 
        my_clear(EndTimeField)
        time.sleep(1) 
        EndTimeField.send_keys("4:00 PM")
        EndTimeField.send_keys(Keys.RETURN)
        time.sleep(1)
        # assert that error message is displayed
        DateErrorMsg = find_my_element(driver,"XPATH",EVENT_START_DATE_MSG)
        assert DateErrorMsg.get_attribute('innerHTML') == "End date must be after start date."

        DateErrorMsg = find_my_element(driver,"XPATH",EVENT_END_DATE_MSG)
        assert DateErrorMsg.get_attribute('innerHTML') == "End date must be after start date." 

        time.sleep(1)
        EndTimeField.send_keys("7:00 PM")
        EndTimeField.send_keys(Keys.RETURN)

        time.sleep(1)

        DateAndTimeTitle = find_my_element(driver,"XPATH",DATE_AND_TIME_TITLE)
        driver.execute_script("arguments[0].scrollIntoView();",DateAndTimeTitle)
        time.sleep(1)

        # ----------------------------------------- Testing Display time button -------------------------------- #
        # Test 1 de-select display time button
        DisplayTime = find_my_element(driver,"XPATH",START_TIME_CHECKBOX)
        DisplayTime.click()
        if DisplayTime.is_selected():
            print("Error: Unable to de-select display time button")
        time.sleep(1)

        # --------------------- Test 2 for Event title field --------------------- #
        my_clear(EventTitleField)
        EventTitleErrorMsg = find_my_element(driver,"XPATH",EVENT_TITLE_ERROR_MSG)
        assert EventTitleErrorMsg.text == "Title is required." # if condition not true then this line will produce AssertionError

          

