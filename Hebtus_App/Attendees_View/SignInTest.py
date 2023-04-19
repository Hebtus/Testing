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


def sign_in(driver):
    # Get a list of emails and passwords to be tested
    EmailFile = open("./Test_Cases/SignUpEmails.txt", "r")
    PasswordFile = open("./Test_Cases/SignUpPasswords.txt", "r")
    Emails = EmailFile.readlines()
    Passwords = PasswordFile.readlines()
    for i in range(len(Emails)):
        Emails[i] = Emails[i].rstrip("\n")
    for i in range(len(Passwords)):
        Passwords[i] = Passwords[i].rstrip("\n")

    # sign_in_valid(driver, "ayausamakhalifa@gmail.com", "123456789")
    sign_in_invalid(driver, "ayausamakhalifa@gmail.com")
    # login_with_facebook(driver, Emails[15], Passwords[5])
    # forget_password_test(driver, Emails[17], Passwords[4])

#* Phase 4
def sign_in_valid(driver, Email, Password):
    # ---------------------------------------------- Testing valid log in ---------------------------------------------- #
    # enter email and password
    EmailTextbox = find_my_element(driver, "XPATH", EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.click()
    time.sleep(1)
    EmailTextbox = find_my_element(driver, "XPATH", EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found 2")
    EmailTextbox.send_keys(Email)
    time.sleep(1)

    PasswordTextbox = find_my_element(driver, "XPATH", PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.click()
    time.sleep(1)
    PasswordTextbox = find_my_element(driver, "XPATH", PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found 2")
    PasswordTextbox.send_keys(Password)
    time.sleep(1)
    LoginButton = find_my_element(driver, "XPATH", LOGIN_BUTTON)
    check_not_found(driver, LoginButton, "Login button not found")
    LoginButton.click()
    time.sleep(4)
    # check if landing page is reached
    LandingPage = find_my_element(driver, "XPATH", LANDING_PAGE)
    check_not_found(driver, LandingPage, "Landing page not reached")
    print("signed in successfuly")
    # Sign out
    # Click on Profile icon
    ProfileIcon = find_my_element(driver, "XPATH", PROFILE_ICON)
    check_not_found(driver, ProfileIcon, "Profile icon not found")
    ProfileIcon.click()
    time.sleep(1)
    # click sign out
    SignoutButton = find_my_element(driver, "XPATH", SIGN_OUT_BUTTON)
    check_not_found(driver, SignoutButton, "Sign out button not found")
    SignoutButton.click()
    time.sleep(2)
    # check login page reached
    LoginPage = find_my_element(driver, "XPATH", EMAIL_TEXTBOX)
    check_not_found(driver, LoginPage, "LoginPage not reached")
    print("signed out successfully")
    driver.quit()

#* Phase 4
def sign_in_invalid(driver, Email):
    # ---------------------------------------------- Testing invalid log in ---------------------------------------------- #
    # ------------------- unregistered email-------------------
    # enter email and password
    EmailTextbox = find_my_element(driver, "XPATH", EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.click()
    time.sleep(1)
    EmailTextbox = find_my_element(driver, "XPATH", EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found 2")
    EmailTextbox.send_keys("Neweventbrite@gmail.com")
    time.sleep(1)
    PasswordTextbox = find_my_element(driver, "XPATH", PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.click()
    time.sleep(1)
    PasswordTextbox = find_my_element(driver, "XPATH", PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found 2")
    PasswordTextbox.send_keys("147258369")
    time.sleep(1)
    LoginButton = find_my_element(driver, "XPATH", LOGIN_BUTTON)
    check_not_found(driver, LoginButton, "Login button not found")
    LoginButton.click()
    time.sleep(4)
    # Check if error message appeared
    OkButton = find_my_element(driver, "XPATH", ERROR_WINDOW_OK_BUTTON)
    check_not_found(driver, OkButton, "Error message not found")
    OkButton.click()
    time.sleep(1)
    # -------------------invalid password-------------------
    # enter email
    EmailTextbox = find_my_element(driver, "XPATH", EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.click()
    time.sleep(1)
    EmailTextbox = find_my_element(driver, "XPATH", EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found 2")
    EmailTextbox.click()
    time.sleep(1)
    EmailTextbox.set_text(Email)
    time.sleep(1)
    LoginButton = find_my_element(driver, "XPATH", LOGIN_BUTTON)
    check_not_found(driver, LoginButton, "Login button not found")
    LoginButton.click()
    time.sleep(4)
    # Check if error message appeared
    OkButton = find_my_element(driver, "XPATH", ERROR_WINDOW_OK_BUTTON)
    check_not_found(driver, OkButton, "Error message not found")
    OkButton.click()
    time.sleep(1)
    print("Sign in Invlaid tests passed")
    driver.quit()


def login_with_facebook(driver, Email, Password):
    # ---------------------------------------------- Testing log in with facebook ---------------------------------------------- #
    driver.get("https://www.eventbrite.com/signin")
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Click on log in with facebook
    LoginWithFacebookButton = find_my_element(
        driver, "XPATH", LOGIN_WITH_FACEBOOK_BUTTON
    )
    check_not_found(
        driver, LoginWithFacebookButton, "Login with facebook button not found"
    )
    LoginWithFacebookButton.click()
    time.sleep(10)
    # Switch to facebook window
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(10)
    # Enter email and password
    FacebookPasswordTextbox = find_my_element(driver, "ID", FACEBOOK_PASSWORD_TEXTBOX)
    check_not_found(driver, FacebookPasswordTextbox, "Facebook page not found")
    FacebookEmailTextbox = find_my_element(driver, "ID", FACEBOOK_EMAIL_TEXTBOX)
    check_not_found(driver, FacebookEmailTextbox, "Facebook email textbox not found")
    FacebookEmailTextbox.send_keys(Email)
    FacebookPasswordTextbox.send_keys(Password)
    time.sleep(10)
    FacebookLoginButton = find_my_element(driver, "XPATH", FACEBOOK_LOGIN_BUTTON)
    check_not_found(driver, FacebookLoginButton, "Facebook login button not found")
    FacebookLoginButton.click()
    time.sleep(20)
    driver.switch_to.window(driver.window_handles[0])
    AdExitButton = find_my_element(driver, "XPATH", AD_EXIT_BUTTON)
    if AdExitButton != None:
        AdExitButton.click()
        time.sleep(10)
        LeaveButton = find_my_element(driver, "XPATH", AD_WANT_TO_LEAVE_BUTTON)
        if LeaveButton != None:
            LeaveButton.click()
            time.sleep(10)
    # Check if landing page is reached
    LandingPage = find_my_element(driver, "XPATH", LANDING_PAGE)
    check_not_found(driver, LandingPage, "Landing page not reached")
    driver.implicitly_wait(5)
    driver.quit()
    print("Successfully login with facebook account")


def forget_password_test(driver, Email, Password):
    # ---------------------------------------------- Testing forget password ---------------------------------------------- #
    # Open log in page
    driver.get("https://www.eventbrite.com/signin")
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Enter email and wrong password
    EmailTextbox = find_my_element(driver, "ID", EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.send_keys(Email)
    time.sleep(10)
    PasswordTextbox = find_my_element(driver, "ID", PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    # invalid password
    PasswordTextbox.send_keys("Password")
    time.sleep(30)
    LoginButton = find_my_element(driver, "XPATH", LOGIN_BUTTON)
    check_not_found(driver, LoginButton, "Login button not found")
    LoginButton.click()
    time.sleep(30)
    # Click forget password button
    ForgetPasswordButton = find_my_element(driver, "XPATH", FORGET_PASSWORD_BUTTON)
    check_not_found(driver, ForgetPasswordButton, "Forget my password button not found")
    ForgetPasswordButton.click()
    time.sleep(10)
    # opend gamil to log in
    driver.get("https://mail.google.com/")
    time.sleep(20)
    # Enter email and password
    GmailTextbox = find_my_element(driver, "ID", GMAIL_TEXTBOX)
    check_not_found(driver, GmailTextbox, "Gmail page not reached")
    GmailTextbox.send_keys(Email)
    time.sleep(10)
    NextButton = find_my_element(driver, "XPATH", NEXT_BUTTON)
    check_not_found(driver, NextButton, "Next button not found")
    NextButton.click()
    time.sleep(10)
    GmailPasswordTextbox = find_my_element(driver, "XPATH", GMAIL_PASSWORD_TEXTBOX)
    check_not_found(driver, GmailPasswordTextbox, "Gmail password page not reached")
    GmailPasswordTextbox.send_keys(Email)
    time.sleep(10)
    NextButton = find_my_element(driver, "XPATH", PASSWORD_NEXT_BUTTON)
    check_not_found(driver, NextButton, "Next button not found")
    NextButton.click()
    time.sleep(10)
    # create action chain object
    action = ActionChains(driver)
    # get first email
    FirstEmail = find_my_element(driver, "XPATH", FIRST_EMAIL)
    check_not_found(driver, FirstEmail, "First email not found")
    # perform the operation
    action.move_to_element(FirstEmail).click().perform()
    # Click on set new password button
    SetNewPassword = find_my_element(driver, "LINK_TEXT", SET_NEW_PASSWORD_LINK)
    check_not_found(driver, SetNewPassword, "Set new password button not found")
    # perform the operation
    action.move_to_element(SetNewPassword).click().perform()
    time.sleep(30)
    # Add new password
    PasswordTextbox = find_my_element(driver, "ID", PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.send_keys(Password)
    UpdatePasswordButton = find_my_element(driver, "XPATH", UPDATE_PASSWORD_BUTTON)
    check_not_found(driver, UpdatePasswordButton, "Update password button not found")
    # Click update password
    UpdatePasswordButton.click()
    time.sleep(30)
    AdExitButton = find_my_element(driver, "XPATH", AD_EXIT_BUTTON)
    if AdExitButton != None:
        AdExitButton.click()
        time.sleep(10)
        LeaveButton = find_my_element(driver, "XPATH", AD_WANT_TO_LEAVE_BUTTON)
        if LeaveButton != None:
            LeaveButton.click()
            time.sleep(10)
    # Check if landing page reached
    LandingPage = find_my_element(driver, "XPATH", LANDING_PAGE)
    check_not_found(driver, LandingPage, "Landing page not reached")
    time.sleep(10)
    print("Forget and update password test passed successfuly")
    driver.quit()
