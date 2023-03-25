from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# ----- Includes for Attendee's view web pages ----- #

# ----- Includes for Creator's view web pages ----- #
from Creators_View.LogInToCreatorView import creator_view
from Creators_View.BasicInfo import basic_info
from Creators_View.EventList import event_list

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
basic_info(driver, 1)
