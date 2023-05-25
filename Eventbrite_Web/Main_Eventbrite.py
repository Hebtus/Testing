from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# ----- Includes for Attendee's view web pages ----- #
from Attendees_View.SignUpTest import sign_up
from Attendees_View.SignInTest import sign_in
from Attendees_View.EventPageTest import event_page
from Attendees_View.LandingPageTest import landing_page

# ----- Includes for Creator's view web pages ----- #
from Creators_View.LogInToCreatorView import creator_view
from Creators_View.BasicInfo import basic_info
from Creators_View.EventList import event_list

import time

choice = int(input("Enter \n (1) For Attendee's View \n (2) For Creator's View \n"))

Coptions = Options()
Coptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=Coptions)

PATH = "C:\Program Files (x86)\chromedriver.exe"  # edit depending on your chromedriver path
s = Service(PATH)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


# ---------------------------------------------------------------- Start ---------------------------------------------------------------- #
if(choice == 1):
# ------------- Attendee's view web pages testing ------------- #
    sign_up(driver)
    # sign_in(driver)
    # event_page(driver)
    # landing_page(driver)

elif(choice == 2):
    # ------------- Creator's view web pages testing -------------- #
    choice = int(input("Enter \n (1) For Event List Test \n (2) For Basic Info Tickets and Publish Test \n"))
    driver.maximize_window()
    creator_view(driver)  # temporary
    time.sleep(10)
    if(choice == 1):
        event_list(driver)
    elif(choice == 2):
        basic_info(driver, 1)
