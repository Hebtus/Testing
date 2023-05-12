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

def publish(driver, mode = 0):
    if mode == 0: # Normal operation
        pass
    else:
        def Navigation_Test(driver):
            PublishTitle = find_my_element(driver,"XPATH",PUBLISH_TITLE)
            if(PublishTitle == None):
                print("Failed to navigate correctly to publish page")
            time.sleep(2)

        Navigation_Test(driver)
        