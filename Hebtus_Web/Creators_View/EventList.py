# To give us access to the enter key, escape key...etc. ex: when I write something in the search bar and want to press enter:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import re
import pyperclip
from datetime import datetime
import csv
import openpyxl

import sys
sys.path.append(".") # To access modules in sibling directories

from Common_Files.Utilities import *
from Common_Files.RealReferences_Hebtus import *

def event_list(driver, mode=0):
    # Go to event list
    Btn = find_my_element(driver,"XPATH",GO_TO_EVENTLIST)
    Btn.click()
    time.sleep(4)

    # ---------------------------------------------------- Testing Filters --------------------------------------------------- #
    FilterButton = find_my_element(driver,"ID",FILTER_EVENTS_BUTTON) 
    # Test : Choose filter "All events", count each type and then use filter for every type to check if count matches.
    # Also extract all information to compare with CSV export
    # Lists to extract information
    EventNames=[]
    EventDates=[]
    EventStatuses=[]
    EventTicketsSold=[]
    EventTicketsAvailable=[]
    FilterButton.click()
    time.sleep(1)
    AllEventsButton = find_my_element(driver,"ID", FILTER_ALL_EVENTS)
    AllEventsButton.click()
    FilterButton.click()
    time.sleep(8)



    AllEvents=find_my_elements(driver,"XPATH",EVENTS_LIST)
    AllEventsCount = len(AllEvents) -1 # since header row is included
    # print("Event count",AllEventsCount)
    DraftCount = 0
    OnsaleCount = 0
    EndedCount = 0
    for i in range(2,(AllEventsCount+2)):
        # List for event names
        NameStrXPATH = EVENT_PART1 + str(i) + EVENT_TITLE_PART2
        NameTemp = find_my_element(driver,"XPATH",NameStrXPATH)
        NameText=NameTemp.get_attribute('innerHTML')
        # print("Name: ",NameText)
        EventNames.append(NameText)
        # List for event dates
        DatesXPATH = EVENT_PART1 + str(i) + EVENT_DATE_PART2
        DateTemp = find_my_element(driver,"XPATH",DatesXPATH)
        DateText=DateTemp.get_attribute('innerHTML')
        EventDates.append(DateText)
        # print("Date: ",DateText)
        # List for event statuses
        StatusStrXPATH = EVENT_PART1 + str(i) + EVENT_DRAFT_ONSALE_ENDED_STATUS_PART2
        StatusTemp = find_my_element(driver,"XPATH",StatusStrXPATH)
        StatusHTML = StatusTemp.get_attribute('innerHTML')
        # print("Status: ",StatusHTML)
        # List for Tickets sold
        TicketsSoldXPATH=EVENT_PART1 + str(i) + EVENT_SOLD_PART2
        SoldTemp = find_my_element(driver,"XPATH",TicketsSoldXPATH)
        TicketsText=SoldTemp.get_attribute('innerHTML') # ex: "5/20"
        # print("Sold: ",TicketsText)
        TicketsTemp=TicketsText.split("/")
        # print("Sold num: ",TicketsTemp[0])
        # print("TicketsTemp[1]: ",TicketsTemp[1])
        EventTicketsSold.append(int(TicketsTemp[0]))
        # List for Tickets available
        AvailableNum=int(TicketsTemp[1]) - int(TicketsTemp[0])
        EventTicketsAvailable.append(AvailableNum)

        if "Draft" in StatusHTML:
            DraftCount+=1
            EventStatuses.append("Draft")
        elif "On Sale" in StatusHTML:
            OnsaleCount+=1
            EventStatuses.append("Live")
        elif "Event ended" in StatusHTML:
            EndedCount+=1
            EventStatuses.append("Past")


# ----- UPCOMING EVENTS: ----- #
    # Check if number of events in the filter of "upcoming events" is of the same count
    FilterButton.click()
    time.sleep(1)
    UpcomingEventsButton = find_my_element(driver,"ID", FILTER_UPCOMING_EVENTS)
    UpcomingEventsButton.click()
    FilterButton.click()
    time.sleep(8)
    AllUpcomingEvents = find_my_elements(driver,"XPATH",EVENTS_LIST)
    AllUpcomingCount = len(AllUpcomingEvents) - 1
    if AllUpcomingCount != OnsaleCount:
        print("Error: Not all events with status of On Sale are shown using the filter of upcoming events")
    
    # Check if dates of upcoming events are all upcoming dates
    for i in range(2,AllUpcomingCount+2):
        EVENT_DATE= EVENT_PART1 + str(i) + EVENT_DATE_PART2
        EventDate = find_my_element(driver,"XPATH",EVENT_DATE)
        FullEventDate = EventDate.get_attribute('innerHTML') # ex: Thu May 11 2023 14:16:10 GMT+0200
        FullEventDateSeperated= FullEventDate.split() # default is split at whitespaces
        MonthNum = datetime.strptime(FullEventDateSeperated[1], '%b').month # to cast month from string to int (Note: April -> 4 (not 04))

        # Day
        DayStr=FullEventDateSeperated[2]
        # Month
        if MonthNum<10:
            MonthStr='0'+str(MonthNum)
        else:
            MonthStr=str(MonthNum)

        # Notice: month/day/year not day/month/year
        DateNewFormat = MonthStr + '/' + DayStr + '/' + FullEventDateSeperated[3] + ' ' + FullEventDateSeperated[4] #ex: 05/11/2023 14:16:10
        # print(DateNewFormat)

        datetime_object = datetime.today()
        TodayNewFormat = datetime.strftime(datetime_object, '%m/%d/%Y %H:%M:%S') # to put in format of 04/17/2023 16:05:14
        # print(TodayNewFormat)
        TodayDate = datetime.strptime(TodayNewFormat, '%m/%d/%Y %H:%M:%S') # to cast from str to timeobject

        EventDate = datetime.strptime(DateNewFormat, '%m/%d/%Y %H:%M:%S') # to cast from str to timeobject

        if(TodayDate>EventDate):
            print("Error: An event with a past date is displayed in upcoming events")

    # ----- PAST EVENTS: ----- #
    # Check if number of events in the filter of "past events" is of the same count
    FilterButton.click()
    time.sleep(1)
    PastEventsButton = find_my_element(driver,"ID", FILTER_PAST_EVENTS)
    PastEventsButton.click()
    FilterButton.click()
    time.sleep(8)
    AllPastEvents = find_my_elements(driver,"XPATH",EVENTS_LIST)
    AllPastCount = len(AllPastEvents) -1
    if AllPastCount != EndedCount:
        print("Error: Not all events with Event ended status are shown using the filter of past events")

    # Check if dates of past events are all past dates
    for i in range(2,AllPastCount+2):
        EVENT_DATE= EVENT_PART1 + str(i) + EVENT_DATE_PART2
        EventDate = find_my_element(driver,"XPATH",EVENT_DATE)
        FullEventDate = EventDate.get_attribute('innerHTML') # ex: Thu Mar 11 2023 14:16:10 GMT+0200
        FullEventDateSeperated= FullEventDate.split() # default is split at whitespaces
        MonthNum = datetime.strptime(FullEventDateSeperated[1], '%b').month # to cast month from string to int (Note: April -> 4 (not 04))

        # Day
        DayStr=FullEventDateSeperated[2]
        # Month
        if MonthNum<10:
            MonthStr='0'+str(MonthNum)
        else:
            MonthStr=str(MonthNum)

        # Notice: month/day/year not day/month/year
        DateNewFormat = MonthStr + '/' + DayStr + '/' + FullEventDateSeperated[3] + ' ' + FullEventDateSeperated[4] #ex: 05/11/2023 14:16:10
        # print(DateNewFormat)

        datetime_object = datetime.today()
        TodayNewFormat = datetime.strftime(datetime_object, '%m/%d/%Y %H:%M:%S') # to put in format of 04/17/2023 16:05:14
        # print(TodayNewFormat)
        TodayDate = datetime.strptime(TodayNewFormat, '%m/%d/%Y %H:%M:%S') # to cast from str to timeobject

        EventDate = datetime.strptime(DateNewFormat, '%m/%d/%Y %H:%M:%S') # to cast from str to timeobject

        if(TodayDate<EventDate):
            print("Error: An event with an upcoming date is displayed in past events")

    # ---------------------------------------------------- Testing search bar --------------------------------------------------- #
    # First go to all events filter
    FilterButton.click()
    time.sleep(1)
    AllEvents=find_my_elements(driver,"XPATH",EVENTS_LIST)
    AllEventsButton.click()
    FilterButton.click()
    time.sleep(7)
    SearchBar = find_my_element(driver,"ID",EVENTS_SEARCH_BAR)
    SearchBar.clear()

    # ------------ Search with one letter that is found in many event titles ------------ #
    SearchBar.send_keys("a")
    time.sleep(4)
    SearchedEvents=find_my_elements(driver,"XPATH",EVENTS_LIST)
    SearchedEventsCount = len(SearchedEvents) -1 # since header row is included
    # loop on the events search result to check if the letter "a" is included in all of them
    for i in range(2,(SearchedEventsCount+2)):
        # List for event names
        NameStrXPATH = EVENT_PART1 + str(i) + EVENT_TITLE_PART2
        NameTemp = find_my_element(driver,"XPATH",NameStrXPATH)
        NameText=NameTemp.get_attribute('innerHTML')
        if "a" not in NameText:
            print("Error: search result retrieved an event that does not have the letter a")
    # check if the number of events retrived with the letter "a" matches the number of events we have in "all events" with the letter a
    CountEventsWithLetterA = 0
    for i in range(0,len(EventNames)):
        if "a" in EventNames[i]:
            CountEventsWithLetterA+=1
    if(CountEventsWithLetterA != SearchedEventsCount):
        print("Error: Not all events with the letter a were retrieved")
    
    scroll_to_bottom_of_page(driver)
    time.sleep(10)    
    driver.execute_script("window.scrollBy(0,0)","")
    time.sleep(3)

    # ------------ Search with a substring of an event title ------------ #
    SearchBar.clear()
    SearchBar.send_keys("Party")
    time.sleep(4)
    SearchedEvents=find_my_elements(driver,"XPATH",EVENTS_LIST)
    SearchedEventsCount = len(SearchedEvents) -1 # since header row is included
    # loop on the events search result to check if the letter "a" is included in all of them
    for i in range(2,(SearchedEventsCount+2)):
        # List for event names
        NameStrXPATH = EVENT_PART1 + str(i) + EVENT_TITLE_PART2
        NameTemp = find_my_element(driver,"XPATH",NameStrXPATH)
        NameText=NameTemp.get_attribute('innerHTML')
        if "Party" not in NameText:
            print("Error: search result retrieved an event that does not have the substring Party")
    # check if the number of events retrived with the substring "Party" matches the number of events we have in "all events" with the substring "Party"
    CountEventsWithSubstringParty = 0
    for i in range(0,len(EventNames)):
        if "Party" in EventNames[i]:
            CountEventsWithSubstringParty+=1
    if(CountEventsWithSubstringParty != SearchedEventsCount):
        print("Error: Not all events with the substring Party were retrieved")

    scroll_to_bottom_of_page(driver)
    time.sleep(10)    
    # scroll back up
    driver.execute_script("window.scrollBy(0,0)","")
    time.sleep(3)

    # ------------ Search for an event that does not exist ------------ #
    SearchBar.clear()
    SearchBar.send_keys("Spa Event")
    SearchedEvents=find_my_elements(driver,"XPATH",EVENTS_LIST)
    SearchedEventsCount = len(SearchedEvents) - 1 # because header row is counted 
    # check if the number of events retrived is zero
    if(SearchedEventsCount != 0):
        print("Error: Retrieved events when none exist with the searched name")
    time.sleep(4)   