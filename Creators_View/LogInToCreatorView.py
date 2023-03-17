from selenium.webdriver.common.by import By
import sys
sys.path.append(".") # Adds higher directory to python modules path
from Common_Files.Utilities import find_my_element

def creator_view(driver):
    # Start at log-in page:
    driver.get("https://www.eventbrite.com/signin/")
    email_address = driver.find_element(By.ID, "email")
    email_address.send_keys("malak.mokhtar@gmail.com")  # Send text to a box
    password = driver.find_element(By.ID, "password")
    password.send_keys("MaloukaLouka")
    LogInBtn = driver.find_element(By.XPATH, "//button[@type='submit']")
    LogInBtn.click()

    # Navigate to creator's view
    creatorView = find_my_element(driver, "LINK_TEXT", "Create an event")
    creatorView.click()
