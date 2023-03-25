from selenium.webdriver.common.by import By
import time
import sys
sys.path.append(".") # Adds higher directory to python modules path
from Common_Files.Utilities import find_my_element
from Common_Files.RealReferences import *

def creator_view(driver):

    # Start at log-in page:
    driver.get("https://www.eventbrite.com/signin/")
    email_address = driver.find_element(By.ID, "email")
    email_address.send_keys("malak.mokhtar@gmail.com")  # Send text to a box
    password = driver.find_element(By.ID, "password")
    password.send_keys("MaloukaLouka")
    LogInBtn = driver.find_element(By.XPATH, "//button[@type='submit']")
    LogInBtn.click()

    time.sleep(2)

    try:
        SessionExpired = driver.find_element(By.XPATH,SESSION_EXPIRED_TITLE)
        time.sleep(1)
        creatorView = find_my_element(driver, "LINK_TEXT", "Create an event") # clicking on create an event navigates us back to log-in page
        creatorView.click()
        time.sleep(5)
        email_address = find_my_element(driver, "ID", "email")
        email_address.send_keys("malak.mokhtar@gmail.com")  # Send text to a box
        password = find_my_element(driver,"ID", "password")
        password.send_keys("MaloukaLouka")
        LogInBtn = find_my_element(driver,"XPATH", "//button[@type='submit']")
        time.sleep(1)
        LogInBtn.click()
        time.sleep(2)
    except:
        print("No navigation to session expired tab")
        # Navigate to creator's view
        try: # Random AD that appears
            Ad = driver.find_element(By.XPATH,RANDOM_AD_SKIP)
            while(Ad.is_displayed()):
                Ad.click()
                time.sleep(2)
                Ad = driver.find_element(By.XPATH,RANDOM_AD_SKIP)
                Ad.click()
                time.sleep(2)
        except:
            print("No Ad displayed when logged in")
            creatorView = find_my_element(driver, "LINK_TEXT", "Create an event")
            creatorView.click()

    RandomTaxFillInfo=find_my_element(driver,"XPATH","//*[@id='cross-chunky_svg__eds-icon--cross-chunky_base']")
    RandomTaxFillInfo.click()