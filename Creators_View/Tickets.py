# To give us access to the enter key, escape key...etc. ex: when I write something in the search bar and want to press enter:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.wait import WebDriverWait

import sys
sys.path.append(".") # To access modules in sibling directories

from Common_Files.Utilities import *
from Common_Files.RealReferences import *


# sellingEndTime: Date must be in the future
# sellingStartTime: Date must be in the future
# Select a ticket type is not supported
# Minimum enumerable capacity should be greater than 0
# sellingStartTime: Start selling date must be before end selling date, sellingEndTime: End selling date must be after start selling date
# Event Name can not be more than 30 characters long.
# ticket created successfully

def tickets(driver, mode = 0):
    if mode == 0: # Normal operation
        pass
    else:
        def Navigation_Test(driver):
            TicketsTitle = find_my_element(driver,"XPATH",TICKETS_TITLE)
            if(TicketsTitle == None):
                print("Failed to navigate correctly to tickets page")
            time.sleep(2)

        def Add_Ticket_Button_Test(driver):  
            AddTicket = find_my_element(driver,"ID",ADD_TICKET_OUTER)
            AddTicket.click()
            time.sleep(4)
            AddTicketTitle = find_my_element(driver,"ID",TICKET_TITLE_TAB)
            if(AddTicketTitle == None):
                 print("Error: did not open tab to enter ticket details")
            time.sleep(2)

        def All_Required_Fields_Test(driver):
                Donation = find_my_element(driver,"ID",DONATION)
                Donation.click()
                time.sleep(1)
                # Test: Not filling any of the required fields (click add without filling any fields)
                AddTicketButton = find_my_element(driver,"ID", ADD_TICKET_INNER)
                AddTicketButton.click()
                ErrorMsg = find_my_element(driver,"ID",TICKETS_ERROR_MSG)
                if(ErrorMsg == None):
                    print("Error: no error message displayed in case of not filling all required fields in add ticket")
                time.sleep(2)
                assert ErrorMsg.get_attribute("innerHTML") == "Ticket validation failed: name: Please provide a ticket name, type: Select a ticket type is not supported, capacity: Minimum enumerable capacity should be greater than 0, sellingStartTime: Date must be in the future, sellingEndTime: Date must be in the future"

        def Name_Length_Test(driver):
                Name = find_my_element(driver,"ID",NAME_TICKET_FIELD)
                Name.click()
                Name.send_keys("This is a 66 character message testing the 50 limit on characters.")
                if len(Name.get_attribute("value")) != 50:
                    print(
                        "Error: Case of 50 character as maximum limit for Name field in tickets not handled"
                    )
                time.sleep(2) 

        def Adding_Ticket_Test(driver):
            # Fill all fields
            Name = find_my_element(driver,"ID",NAME_TICKET_FIELD)
            Quantity = find_my_element(driver,"ID",QUANTITY_TICKET_FIELD)
            Price = find_my_element(driver,"ID",PRICE_TICKET_FIELD)
            StartDate = find_my_element(driver,"ID",START_DATE_TICKET)
            EndDate = find_my_element(driver,"ID",END_DATE_TICKET)
            SelectTicket = find_my_element(driver,"ID",SELECT_TICKET_TYPE)
            StartTime = find_my_element(driver,"ID",START_TIME_TICKET)
            EndTime = find_my_element(driver,"ID",END_TIME_TICKET)
            Donation = find_my_element(driver,"ID",DONATION)

            Donation.click()
            my_clear(Name)
            Name.send_keys("First row tickets")
            time.sleep(1)
            my_clear(Quantity)
            Quantity.send_keys("10")
            time.sleep(1)
            my_clear(Price)
            Price.send_keys("150")
            time.sleep(1)
            SelectTicket.click()
            drp = Select(SelectTicket)
            time.sleep(1)
            drp.select_by_visible_text("VIP")
            Donation.click()
            my_clear(StartDate)
            StartDate.send_keys("06/13/2023")
            time.sleep(1)
            my_clear(EndDate)
            EndDate.send_keys("06/15/2023")
            time.sleep(1)
            my_clear(StartTime)
            StartTime.send_keys("03:00 PM")
            time.sleep(1)
            my_clear(EndTime)
            EndTime.send_keys("05:00 PM")
            time.sleep(1)

            # Add the tickets
            Form_Add_Ticket_and_Close(driver)
            # Check if the ticket was added succesfully
            Ticket_Added_or_Edited_Succesfully_Test(driver,Title="First row tickets",StartDate="2023-06-13",TicketCount="0 / 10",Operation="Added")


        def  Form_Add_Ticket_and_Close(driver):
            AddTicket = find_my_element(driver,"ID",ADD_TICKET_INNER)
            AddTicket.click()
            time.sleep(1)
            CloseForm = find_my_element(driver,"ID",CLOSE_TICKET_FORM)
            CloseForm.click()
            time.sleep(1)
        
        def Ticket_Added_or_Edited_Succesfully_Test(driver,Title,StartDate,TicketCount,Operation):
            # Test that a ticket card was created and displayed
            TicketCard = find_my_element(driver,"ID",FIRST_TICKET_CARD)
            if(TicketCard == None):
                print("Error! No ticket card created and displayed after adding tickets")
            
            # Test: validate data inside ticket card
            EventTitle = find_my_element(driver,"ID",FIRST_EVENT_TITLE)
            EventStartDate = find_my_element(driver,"ID",FIRST_EVENT_START_DATE)
            EventTicketCount = find_my_element(driver,"ID",FIRST_EVENT_TICKET_COUNT)

            try:
                assert EventTitle.get_attribute("innerHTML") == Title
            except:
                print("Error: Name does not match",Operation,"Name")

            try:
                assert EventStartDate.get_attribute("innerHTML") == StartDate
            except:
                print("Error: Start Date does not match",Operation,"Start Date")

            try:
                assert EventTicketCount.get_attribute("innerHTML") == TicketCount
            except:
                print("Error: Ticket Count does not match",Operation,"Ticket Count")

            time.sleep(2)

        def Edit_Event_Test(driver):
            # Test: edit event tickets
            EventEdit = find_my_element(driver,"ID",FIRST_EVENT_TICKET_EDIT)
            EventEdit.click()
            time.sleep(2)
            # check if edit tab was opened
            EditTicketTitle = find_my_element(driver,"ID",TICKET_TITLE_TAB)
            if(EditTicketTitle == None):
                print("Error: did not open tab to edit ticket details")
            time.sleep(2)
            
            # edit name, quantity and start date
            Name = find_my_element(driver,"ID",NAME_TICKET_FIELD)
            Quantity = find_my_element(driver,"ID",QUANTITY_TICKET_FIELD)
            StartDate = find_my_element(driver,"ID",START_DATE_TICKET)
            
            my_clear(Name)
            Name.send_keys("Gold tickets")
            time.sleep(1)
            my_clear(Quantity)
            Quantity.send_keys("4")
            time.sleep(1)
            my_clear(StartDate)
            StartDate.send_keys("06/10/2023")
            time.sleep(1)

            # check if they were edited
            Form_Add_Ticket_and_Close(driver)

            # check if ticket was edited
            Ticket_Added_or_Edited_Succesfully_Test(driver,Title="Gold tickets",StartDate="06/10/2023",TicketCount="4", Operation="Edited")
            time.sleep(2)

        def Go_To_Publish(driver):
            PublishButton = find_my_element(driver,"XPATH",GO_TO_PUBLISH)
            PublishButton.click()
            time.sleep(2)

        Navigation_Test(driver)
        Add_Ticket_Button_Test(driver)
        All_Required_Fields_Test(driver)
        Name_Length_Test(driver)
        Adding_Ticket_Test(driver)
        Edit_Event_Test(driver)
        Go_To_Publish(driver)




        
















