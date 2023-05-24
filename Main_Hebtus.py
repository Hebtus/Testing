from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# ----- Includes for Attendee's view web pages ----- #

# ----- Includes for Creator's view web pages ----- #
from Creators_View.LogInToCreatorView import creator_view
from Creators_View.BasicInfo import basic_info
from Creators_View.EventList import event_list
from Creators_View.Tickets import tickets
from Creators_View.Publish import publish
from Creators_View.Dashboard import dashboard
from Creators_View.Publish import publish

Coptions = Options()
Coptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=Coptions)

PATH = "C:\Program Files (x86)\chromedriver.exe"  # edit depending on your chromedriver path
s = Service(PATH)

# ---------------------------------------------------------------- Start ---------------------------------------------------------------- #
# ------------- Attendee's view web pages testing ------------- #

# ----- Navigation from Attendee's view to Creator's view ----- #

# ------------- Creator's view web pages testing -------------- #
driver.maximize_window()
creator_view(driver)  # temporary
#event_list(driver)
#dashboard(driver)
basic_info(driver, 1)
tickets(driver,1)
publish(driver,1)