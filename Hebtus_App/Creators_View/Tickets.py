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

# # import Action chains
from selenium.webdriver.common.action_chains import ActionChains

def find_my_elements(Driver, type, val):
    try:
        if type == "XPATH":
            items = WebDriverWait(Driver, 30).until(
                EC.presence_of_all_elements_located((AppiumBy.XPATH, val))
            )
        elif type == "LINK_TEXT":
            items = WebDriverWait(Driver, 20).until(
                EC.presence_of_all_elements_located((AppiumBy.LINK_TEXT, val))
            )
        elif type == "CLASS":
            items = WebDriverWait(Driver, 20).until(
                EC.presence_of_all_elements_located((AppiumBy.CLASS_NAME, val))
            )
        elif type == "AID":
            items = WebDriverWait(Driver, 20).until(
                EC.presence_of_all_elements_located((AppiumBy.ACCESSIBILITY_ID, val))
            )
        else:
            return None
    except:
        # print("Elements not found.")
        return None
    return items

def tickets(driver):
    # Validate Navigation (check if "Tickets" title is present)
    TicketsTitle = find_my_element(driver,"XPATH",TICKETS_TITLE)
    check_not_found(driver,TicketsTitle,"Did not navigate to Tickets page")

    time.sleep(2)
    touch = TouchAction(driver)

    def Promo_Codes_Test(driver):
        # Promo codes test:
        PromoCode = find_my_element(driver,"XPATH",PROMO_CODE)
        PromoCode.click()
        time.sleep(2)

        # Click on Add promo code
        PromoCode = find_my_element(driver,"XPATH",ADD_A_CODE)
        PromoCode.click()
        time.sleep(2)

        # fill fields
        Field = find_my_element(driver,"XPATH",CODE_NAME)
        Field.click()
        time.sleep(1)
        Field.send_keys("MALAK")
        time.sleep(1)
        driver.hide_keyboard()

        Field = find_my_element(driver,"XPATH",NUMBER_OF_USES)
        Field.click()
        time.sleep(1)
        Field.send_keys("2")
        time.sleep(1)
        driver.hide_keyboard()

        Btn = find_my_element(driver,"XPATH",PROMO_PERCENTAGE_BTN)
        Btn.click()
        time.sleep(2)

        Field = find_my_element(driver,"XPATH",PROMO_PERCENTAGE)
        Field.click()
        time.sleep(1)
        Field.send_keys("65")
        time.sleep(1)
        driver.hide_keyboard()

        #Add the promo code
        Btn = find_my_element(driver,"XPATH",ADD_PROMO)
        Btn.click()
        time.sleep(2)

        Btn = find_my_element(driver,"XPATH",PROMO_BACK)
        Btn.click()
        time.sleep(2)

        Btn = find_my_element(driver,"XPATH",PROMO_REFRESH)
        Btn.click()
        time.sleep(2)

        # Validate if promo code has been added and added correctly
        # Validate name
        Text = find_my_element(driver,"XPATH",PROMO_ADDED_NAME).get_attribute('content-desc')
        check_not_found(driver,Text,"Error! Promo code was not added succesfully")
        if(Text != "MALAK"):
            print("Error! Promo code name does not match the one added")
        time.sleep(1)
        # Validate type
        Text = find_my_element(driver,"XPATH",PROMO_CODE_TYPE).get_attribute('content-desc')
        check_not_found(driver,Text,"Error! Promo code was not added succesfully")
        if(Text != "percantage"):
            print("Error! Promo code type does not match the one added")
        time.sleep(1)
        # swipe horizontally
        touch.press(x=353, y=666).move_to(x=25,y=666).release().perform()
        time.sleep(2)
        # Validate uses
        Text = find_my_element(driver,"XPATH",PROMO_CODE_USES).get_attribute('content-desc')
        check_not_found(driver,Text,"Error! Promo code was not added succesfully")
        if(Text != "2"):
            print("Error! Promo code uses does not match the one added")
        time.sleep(1)
        # Swipe again
        touch.press(x=418, y=662).move_to(x=24,y=658).release().perform()
        time.sleep(2)
        # Click on options
        Btn = find_my_element(driver,"XPATH",PROMO_CODE_OPTIONS)
        Btn.click()
        time.sleep(2)
        # choose delete
        Btn = find_my_element(driver,"XPATH",PROMO_CODE_DELETE)
        Btn.click()
        time.sleep(2)
        # click on refresh
        Btn = find_my_element(driver,"XPATH",PROMO_REFRESH)
        Btn.click()
        time.sleep(2)
        # check if event was deleted
        if(find_my_element(driver,"XPATH",PROMO_CODE_OPTIONS) != None):
            print("Error! Unable to delete promo code")

    def Admission_Test(driver):

        # Click on add more tickets
        AddTicket = find_my_element(driver,"XPATH",ADD_MORE_TICKETS)
        AddTicket.click()
        time.sleep(2)

        # Fill fields for adding ticket
        # Name
        Textbox = find_my_element(driver, "XPATH", ADD_TICKETS_NAME)
        check_not_found(driver, Textbox, "Name textbox not found")
        Textbox.click()
        time.sleep(1)
        Textbox.send_keys("Back row tickets")
        driver.hide_keyboard()
        time.sleep(1)
        # Price
        Textbox = find_my_element(driver, "XPATH", ADD_TICKETS_PRICE)
        check_not_found(driver, Textbox, "Price textbox not found")
        Textbox.click()
        time.sleep(1)
        Textbox.send_keys("100")
        driver.hide_keyboard()
        time.sleep(1)
        # Quantity
        Textbox = find_my_element(driver, "XPATH", ADD_TICKETS_QUANTITY)
        check_not_found(driver, Textbox, "Quantity textbox not found")
        Textbox.click()
        time.sleep(1)
        Textbox.send_keys("70")
        time.sleep(1)
        driver.hide_keyboard()
        time.sleep(1)

        touch.press(x=25, y=359).move_to(x=23,y=136).release().perform()
        time.sleep(15)

        # Date and time
        #StartDate = find_my_element(driver, "XPATH", ADD_TICKETS_EVENT_STARTS)
        #check_not_found(driver, StartDate, "Start date not found")
        #StartDate.click()
        #time.sleep(1)
        #StartDate.send_keys("2023-05-17")
        #time.sleep(2)
        #driver.hide_keyboard()
        #time.sleep(4)
#
        #EndDate = find_my_element(driver, "XPATH", ADD_TICKETS_EVENT_ENDS)
        #check_not_found(driver, EndDate, "End date not found")
        #EndDate.click()
        #time.sleep(2)
        #EndDate.send_keys("2023-05-18")
        #time.sleep(3)
        #driver.hide_keyboard()
        #time.sleep(4)

        # Add ticket
        AddTicketBtn = find_my_element(driver, "XPATH", ADD_TICKET_BTN)
        check_not_found(driver, AddTicketBtn, "Add ticket button not found")
        AddTicketBtn.click()
        time.sleep(3)
        # Go back
        GoBack = find_my_element(driver, "XPATH", ADD_TICKETS_GO_BACK)
        check_not_found(driver, GoBack, "Go back button not found")
        GoBack.click()
        time.sleep(3)

        # outer swipe down to refresh
        touch.press(x=225, y=690).move_to(x=441,y=286).release().perform()
        time.sleep(2)

        # refresh
        Refresh = find_my_element(driver, "XPATH", REFRESH)
        check_not_found(driver, Refresh, "Go back button not found")
        Refresh.click()
        time.sleep(3)

        # Initial swipe to get frame of ticket cards
        touch.press(x=472, y=385).move_to(x=463,y=222).release().perform()
        time.sleep(2)

        # retrieve data for all ticket cards
        Names = []
        Quantities = []
        Prices = []
        # outer loop that swipes infinitely until it finds that refresh button has appeared
        try: 
            NameList = find_my_elements(driver,"XPATH",TICKET_NAMES)
            while(True):
                # retrieve all names
                NameList = find_my_elements(driver,"XPATH",TICKET_NAMES)
                for i in range(0, len(NameList)+1):
                    print(NameList[i].get_attribute('content-desc'))
                    Names.append(NameList[i].get_attribute('content-desc'))
                # retrieve all prices
                NameList = find_my_elements(driver,"XPATH",TICKET_PRICES)
                for i in range(0, len(NameList)+1):
                    print(NameList[i].get_attribute('content-desc'))
                    Prices.append(NameList[i].get_attribute('content-desc'))
                # retrieve all quantities
                NameList = find_my_elements(driver,"XPATH",TICKET_QUANTITIES)
                for i in range(0, len(NameList)+1):
                    print(NameList[i].get_attribute('content-desc'))
                    Quantities.append(NameList[i].get_attribute('content-desc'))
                # swipe
                touch.press(x=470, y=711).move_to(x=469,y=145).release().perform()
                time.sleep(2)
                # check break condition
                if(find_my_element(driver, "XPATH", REFRESH) == None):
                    break
            
            # check list of names to find the added ticket
            try:
                i = Names.index("Back row tickets")
                if(Quantities[i] != "70"):
                    print("Error! Quantity does not match the one added")
                if(Prices[i] != "100"):
                    print("Error! Price does not match the one added")
            except:
                print("Error! Was not able to add tickets or added name does not match")
        except:
            print("Error! No ticket cards available")

    Admission_Test(driver)
    Promo_Codes_Test(driver)





    

