# To give us access to the enter key, escape key...etc. ex: when I write something in the search bar and want to press enter:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import sys

sys.path.append(".")  # To access modules in sibling directories

from Common_Files.Utilities import *
from Common_Files.RealReferences import *

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains


def sign_up(driver):
    # Get a list of emails and passwords to be tested
    EmailFile = open("./Test_Cases/SignUpEmails.txt", "r")
    PasswordFile = open("./Test_Cases/SignUpPasswords.txt", "r")
    Emails = EmailFile.readlines()
    Passwords = PasswordFile.readlines()
    for i in range(len(Emails)):
        Emails[i] = Emails[i].rstrip("\n")
    for i in range(len(Passwords)):
        Passwords[i] = Passwords[i].rstrip("\n")
    # sign_up_valid_test(driver, Emails[0], Passwords[0])
    # sign_up_invalid_email(driver, Emails[2:14])
    # sign_up_invalid_tests(driver, Emails[1], Passwords)
    # Sign_up_with_facebook(driver, Emails[16], Passwords[6])
    # sign_up_with_google(driver)
    # go_to_login_page(driver)


# Valid test cases
def sign_up_valid_test(driver, Email, Password):
    # ---------------------------------------------- Testing valid email ---------------------------------------------- #
    # Open sign up page
    driver.get("https://www.eventbrite.com/signin/signup")
    driver.maximize_window()
    driver.implicitly_wait(5)
    # Enter email
    EmailTextbox = find_my_element(driver, "ID", EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.send_keys(Email)
    # create action chain object
    action = ActionChains(driver)
    ContinueButton = find_my_element(driver, "XPATH", CONTINUE_BUTTON)
    check_not_found(driver, ContinueButton, "Continue button not found")
    ContinueButton.click()
    driver.implicitly_wait(10)
    # Confirm email
    EmailConfirmationTextbox = find_my_element(driver, "ID", EMAIL_CONFIRMATION_TEXTBOX)
    check_not_found(
        driver, EmailConfirmationTextbox, "Confirmation email page is not found"
    )
    EmailConfirmationTextbox.send_keys(Email)
    # Enter first and last name
    FirstNameTextbox = find_my_element(driver, "ID", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTextbox, "First name textbox not found")
    FirstNameTextbox.send_keys("UserFirstName")
    driver.implicitly_wait(5)
    LastNameTextbox = find_my_element(driver, "ID", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.send_keys("UserLastName")
    driver.implicitly_wait(5)
    # enter password
    PasswordTextbox = find_my_element(driver, "ID", PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.send_keys(Password)
    time.sleep(30)
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Create acount button not found")

    # perform the operation
    action.move_to_element(CreateAcountButton).click().perform()

    time.sleep(10)
    # Agrree on terms and conditions
    AgreeButton = find_my_element(driver, "XPATH", AGREE_BUTTON)
    check_not_found(
        driver, AgreeButton, "Popup window not found - agree button not found"
    )
    AgreeButton.click()
    time.sleep(30)
    # Start attending button (doesn't always appear)
    StartAttendingButton = find_my_element(driver, "XPATH", START_ATTENDING_BUTTON)
    if StartAttendingButton != None:
        StartAttendingButton.click()

    driver.implicitly_wait(30)
    # Exit from preferences page
    ExitButton1 = find_my_element(driver, "XPATH", EXIT_BUTTON_1)
    check_not_found(driver, ExitButton1, "Preferneces page not reached")
    ExitButton1.click()
    driver.implicitly_wait(30)
    ExitButton2 = find_my_element(driver, "XPATH", EXIT_BUTTON_2)
    check_not_found(driver, ExitButton2, "Pop up window not found")
    ExitButton2.click()
    driver.implicitly_wait(30)
    AdExitButton = find_my_element(driver, "XPATH", AD_EXIT_BUTTON)
    if AdExitButton != None:
        AdExitButton.click()
        time.sleep(10)
        LeaveButton = find_my_element(driver, "XPATH", AD_WANT_TO_LEAVE_BUTTON)
        if LeaveButton != None:
            LeaveButton.click()
            time.sleep(10)
    # check if landing page is reached
    LandingPage = find_my_element(driver, "XPATH", LANDING_PAGE)
    check_not_found(driver, LandingPage, "Landing page not reached")
    driver.implicitly_wait(30)
    print("Signed up successfuly")
    driver.close()


def sign_up_invalid_email(driver, Emails):
    # ---------------------------------------------- Testing Invalid emails ---------------------------------------------- #
    # Open the sign up page
    driver.get("https://www.eventbrite.com/signin/signup")
    driver.maximize_window()
    driver.implicitly_wait(10)
    # ------------------- missing email-------------------
    ContinueButton = find_my_element(driver, "XPATH", CONTINUE_BUTTON)
    check_not_found(driver, ContinueButton, "Continue button not found")
    ContinueButton.click()
    time.sleep(10)
    # Check if an alert is present
    MissingEmailAlert = find_my_element(driver, "XPATH", INVALID_EMAIL_ALERT)
    check_not_found(driver, MissingEmailAlert, "Email is required alert is not found")
    time.sleep(1)
    # -------------------invalid emails-------------------
    # create action chain object
    action = ActionChains(driver)
    WhiteScreen = find_my_element(driver, "XPATH", WHITE_SPACE_SIGNUP_PAGE)
    EmailTextbox = find_my_element(driver, "ID", EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    InvalidEmails = Emails[1:]
    # loop on invalid emails and test them
    for Email in InvalidEmails:
        clear_textbox(EmailTextbox)
        EmailTextbox.send_keys(Email)
        time.sleep(2)
        # perform the operation
        action.move_to_element(WhiteScreen).click().perform()
        ContinueButton.click()
        # Check if an alert is present
        InvalidEmail = find_my_element(driver, "XPATH", INVALID_EMAIL_ALERT)
        check_not_found(driver, InvalidEmail, "Invalid not detected")
        time.sleep(2)
    # -------------------email already registered-------------------
    clear_textbox(EmailTextbox)
    EmailTextbox.send_keys(Emails[0])
    time.sleep(2)
    WhiteScreen = find_my_element(driver, "XPATH", WHITE_SPACE_SIGNUP_PAGE)
    # perform the operation
    action.move_to_element(WhiteScreen).click().perform()
    ContinueButton.click()
    time.sleep(2)
    # Check if an alert is present
    AlreadyRegisteredEmailAlert = find_my_element(
        driver, "XPATH", EMAIL_ALREADY_USED_ALERT
    )
    check_not_found(
        driver, AlreadyRegisteredEmailAlert, "Already registered email not detected"
    )
    time.sleep(2)
    print("Invalid emails testcases passed")
    driver.close()


def sign_up_invalid_tests(driver, Email, Passwords):
    # ---------------------------------------------- Testing invalid info ---------------------------------------------- #
    # Open sign up page
    driver.get("https://www.eventbrite.com/signin/signup")
    driver.maximize_window()
    driver.implicitly_wait(5)
    # enter valid email and go to next page
    EmailTextbox = find_my_element(driver, "ID", EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.send_keys(Email)
    ContinueButton = find_my_element(driver, "XPATH", CONTINUE_BUTTON)
    check_not_found(driver, ContinueButton, "Continue button not found")
    ContinueButton.click()
    driver.implicitly_wait(10)
    # ------------------- confirmation email missing-------------------
    EmailConfirmationTextbox = find_my_element(driver, "ID", EMAIL_CONFIRMATION_TEXTBOX)
    check_not_found(
        driver, EmailConfirmationTextbox, "Confirmation email page is not found"
    )
    FirstNameTextbox = find_my_element(driver, "ID", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTextbox, "First name textbox not found")
    FirstNameTextbox.send_keys("UserFirstName")
    driver.implicitly_wait(5)
    LastNameTextbox = find_my_element(driver, "ID", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.send_keys("UserLastName")
    driver.implicitly_wait(5)
    PasswordTextbox = find_my_element(driver, "ID", PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.send_keys(Passwords[0])
    time.sleep(30)
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Create acount button not found")
    # create action chain object
    action = ActionChains(driver)
    # perform the operation
    action.move_to_element(CreateAcountButton).click().perform()
    time.sleep(10)
    # Check if alert is present
    EmailDontMatchAlert = find_my_element(driver, "XPATH", EMAIL_DONT_MATCH_ALERT)
    check_not_found(driver, EmailDontMatchAlert, "Missing email not detected")

    # ------------------- wrong confirmation email -------------------
    clear_textbox(EmailConfirmationTextbox)
    EmailConfirmationTextbox.send_keys("WrongEmail")
    time.sleep(10)
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Create acount button not found")
    # create action chain object
    action = ActionChains(driver)
    # perform the operation
    action.move_to_element(CreateAcountButton).click().perform()
    time.sleep(10)
    # Check if alert is present
    EmailDontMatchAlert = find_my_element(driver, "XPATH", EMAIL_DONT_MATCH_ALERT)
    check_not_found(driver, EmailDontMatchAlert, "Wrong email not detected")

    # ------------------- First Name missing-------------------
    EmailConfirmationTextbox = find_my_element(driver, "ID", EMAIL_CONFIRMATION_TEXTBOX)
    check_not_found(driver, EmailConfirmationTextbox, "Confirm email is not found")
    clear_textbox(EmailConfirmationTextbox)
    EmailConfirmationTextbox.send_keys(Email)
    clear_textbox(FirstNameTextbox)
    time.sleep(10)
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Create acount button not found")
    time.sleep(10)
    # Check if alert is present
    FirstNameMissingAlert = find_my_element(driver, "XPATH", FIRST_NAME_REQUIRED_ALERT)
    check_not_found(driver, FirstNameMissingAlert, "First name missing alert not found")

    # ------------------- Last Name missing-------------------
    clear_textbox(LastNameTextbox)
    FirstNameTextbox.send_keys("UserFirstName")
    time.sleep(10)
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Create acount button not found")
    time.sleep(10)
    LastNameMissingAlert = find_my_element(driver, "XPATH", LAST_NAME_REQUIRED_ALERT)
    check_not_found(driver, LastNameMissingAlert, "First name missing alert not found")

    # ------------------- Password missing-------------------
    clear_textbox(PasswordTextbox)
    LastNameTextbox.send_keys("UserLastName")
    time.sleep(10)
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Create acount button not found")
    time.sleep(10)
    # Check if alert is present
    PasswordMissingAlert = find_my_element(driver, "XPATH", PASSWORD_REQUIRED_ALERT)
    check_not_found(driver, PasswordMissingAlert, "First name missing alert not found")

    # -------------------password < 8 characters-------------------
    PasswordTextbox.send_keys(Passwords[1])
    time.sleep(10)
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Create acount button not found")
    time.sleep(10)
    # Check if alert is present
    PasswordMissingAlert = find_my_element(driver, "XPATH", PASSWORD_REQUIRED_ALERT)
    check_not_found(driver, PasswordMissingAlert, "First name missing alert not found")

    print("Invalid testcases passed")
    time.sleep(10)
    driver.close()


def Sign_up_with_facebook(driver, Email, Password):
    # ---------------------------------------------- Testing sign up with google ---------------------------------------------- #
    driver.get("https://www.eventbrite.com/signin/signup")
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Click on login with facebook button
    LoginWithFacebookButton = find_my_element(
        driver, "XPATH", SIGNUP_WITH_FACEBOOK_BUTTON
    )
    check_not_found(
        driver, LoginWithFacebookButton, "Login with facebook button not found"
    )
    LoginWithFacebookButton.click()
    time.sleep(10)
    # switch to the facebook window
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(10)
    # enter email and password
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
    FacebookContinueButton = find_my_element(driver, "XPATH", FACEBOOK_CONTINUE_BUTTON)
    if FacebookContinueButton != None:
        FacebookContinueButton.click()
        time.sleep(10)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(10)
    # Agree on terms and conditions
    AgreeButton = find_my_element(driver, "XPATH", ACCEPT_BUTTON)
    check_not_found(
        driver, AgreeButton, "Popup window not found - agree button not found"
    )
    AgreeButton.click()
    time.sleep(30)
    # Start attending button (doesn't always appear)
    StartAttendingButton = find_my_element(driver, "XPATH", START_ATTENDING_BUTTON)
    if StartAttendingButton != None:
        StartAttendingButton.click()

    driver.implicitly_wait(30)
    # Exit from preferences page
    ExitButton1 = find_my_element(driver, "XPATH", EXIT_BUTTON_1)
    check_not_found(driver, ExitButton1, "Preferneces page not reached")
    ExitButton1.click()
    driver.implicitly_wait(30)
    ExitButton2 = find_my_element(driver, "XPATH", EXIT_BUTTON_2)
    check_not_found(driver, ExitButton2, "Pop up window not found")
    ExitButton2.click()
    driver.implicitly_wait(30)
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
    driver.implicitly_wait(30)
    print("Successfully Signed up with facebook account")
    time.sleep(20)
    driver.close()


def sign_up_with_google(driver):
    driver.get("https://www.eventbrite.com/signin/signup")
    driver.maximize_window()
    driver.implicitly_wait(10)
    LoginWithGoogleButton = find_my_element(driver, "XPATH", LOGIN_WITH_GOOGLE_BUTTON)
    check_not_found(driver, LoginWithGoogleButton, "Login with google button not found")
    LoginWithGoogleButton.click()
    time.sleep(10)
    print("Successfully login with google account")


def go_to_login_page(driver):
    # ---------------------------------------------- Testing log in button ---------------------------------------------- #
    driver.get("https://www.eventbrite.com/signin/signup")
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Click on log in button
    LoginButton = find_my_element(driver, "XPATH", SIGNUP_LOGIN_BUTTON)
    check_not_found(driver, LoginButton, "Login button not found")
    LoginButton.click()
    time.sleep(30)
    # check if log in page is reached
    LoginPage = find_my_element(driver, "XPATH", LOGIN_BUTTON)
    check_not_found(driver, LoginPage, "Login page not reached")
    print("Login page reached successfuly")
    driver.close()
