# To give us access to the enter key, escape key...etc. ex: when I write something in the search bar and want to press enter:
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# {"status":"fail"}
sys.path.append(".")  # To access modules in sibling directories

from Common_Files.Utilities import *
from Common_Files.RealReferences_App import *

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains


def sign_up(driver):
    # Get a list of emails and passwords to be tested
    EmailFile = open("./Hebtus_App/Test_Cases/SignUpEmails.txt", "r")
    PasswordFile = open("./Hebtus_App/Test_Cases/SignUpPasswords.txt", "r")
    Emails = EmailFile.readlines()
    Passwords = PasswordFile.readlines()
    for i in range(len(Emails)):
        Emails[i] = Emails[i].rstrip("\n")
    for i in range(len(Passwords)):
        Passwords[i] = Passwords[i].rstrip("\n")
    # sign_in_new_account(driver, Emails[0], Passwords[0])
    # exit()

    # Click on sign up button
    time.sleep(5)
    x = 540.5
    y = 1573
    # tap on the location using the coordinates
    action = TouchAction(driver)
    action.tap(x=x, y=y).perform()
    time.sleep(5)
    # login_button_test(driver)
    # sign_up_valid_test(driver, Emails[0], Passwords[0])
    # sign_up_No_Verification_test(driver, Emails[1], Passwords[0])
    # sign_up_invalid_email(driver, Emails[2:14])
    sign_up_invalid_tests(driver, Emails[1], Passwords)
    # Sign_up_with_facebook(driver, Emails[16], Passwords[6])
    # sign_up_with_google(driver)
    # go_to_login_page(driver)


#! New
def sign_up_No_Verification_test(driver, Email, Password):
    # Enter email
    EmailTextbox = find_my_element(driver, "XPATH", SIGN_UP_EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.click()
    time.sleep(1)
    EmailTextbox = find_my_element(driver, "XPATH", SIGN_UP_EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.send_keys(Email)
    # Enter first name
    FirstNameTextbox = find_my_element(driver, "XPATH", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTextbox, "First name textbox not found")
    FirstNameTextbox.click()
    time.sleep(1)
    FirstNameTextbox = find_my_element(driver, "XPATH", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTextbox, "First name textbox not found")
    FirstNameTextbox.send_keys("UserFirstName")
    driver.implicitly_wait(5)
    # Enter last name
    LastNameTextbox = find_my_element(driver, "XPATH", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.click()
    time.sleep(1)
    LastNameTextbox = find_my_element(driver, "XPATH", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.send_keys("UserLastName")
    driver.implicitly_wait(5)
    # enter password
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.click()
    time.sleep(1)
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.send_keys(Password)
    # Confirm password
    ConfirmPasswordTextbox = find_my_element(driver, "XPATH", CONFIRM_PASSWORD_TEXTBOX)
    check_not_found(
        driver, ConfirmPasswordTextbox, "Confrim Password textbox not found"
    )
    ConfirmPasswordTextbox.click()
    time.sleep(1)
    ConfirmPasswordTextbox = find_my_element(driver, "XPATH", CONFIRM_PASSWORD_TEXTBOX)
    check_not_found(
        driver, ConfirmPasswordTextbox, "Confrim Password textbox not found"
    )
    ConfirmPasswordTextbox.send_keys(Password)

    driver.hide_keyboard()
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Sign up button not found")
    CreateAcountButton.click()
    time.sleep(5)
    # CLick ok
    OkButton = find_my_element(driver, "XPATH", WELCOME_OK_BUTTON)
    check_not_found(driver, OkButton, "Welcome window did not appear")
    OkButton.click()
    time.sleep(2)
    # check if Login page is reached
    LoginPage = find_my_element(driver, "XPATH", EMAIL_TEXTBOX)
    check_not_found(driver, LoginPage, "Login page not reached")
    time.sleep(3)
    print("Signed up successfuly")
    # Go to sign up page again
    # Click on sign up button
    time.sleep(3)
    x = 540.5
    y = 1573
    # tap on the location using the coordinates
    action = TouchAction(driver)
    action.tap(x=x, y=y).perform()
    time.sleep(5)
    # Enter email
    EmailTextbox = find_my_element(driver, "XPATH", SIGN_UP_EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.click()
    time.sleep(1)
    EmailTextbox = find_my_element(driver, "XPATH", SIGN_UP_EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.send_keys(Email)
    # Enter first name
    FirstNameTextbox = find_my_element(driver, "XPATH", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTextbox, "First name textbox not found")
    FirstNameTextbox.click()
    time.sleep(1)
    FirstNameTextbox = find_my_element(driver, "XPATH", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTextbox, "First name textbox not found")
    FirstNameTextbox.send_keys("UserFirstName")
    driver.implicitly_wait(5)
    # Enter last name
    LastNameTextbox = find_my_element(driver, "XPATH", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.click()
    time.sleep(1)
    LastNameTextbox = find_my_element(driver, "XPATH", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.send_keys("UserLastName")
    driver.implicitly_wait(5)
    # enter password
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.click()
    time.sleep(1)
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.send_keys(Password)
    # Confirm password
    ConfirmPasswordTextbox = find_my_element(driver, "XPATH", CONFIRM_PASSWORD_TEXTBOX)
    check_not_found(
        driver, ConfirmPasswordTextbox, "Confrim Password textbox not found"
    )
    ConfirmPasswordTextbox.click()
    time.sleep(1)
    ConfirmPasswordTextbox = find_my_element(driver, "XPATH", CONFIRM_PASSWORD_TEXTBOX)
    check_not_found(
        driver, ConfirmPasswordTextbox, "Confrim Password textbox not found"
    )
    ConfirmPasswordTextbox.send_keys(Password)

    driver.hide_keyboard()
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Sign up button not found")
    CreateAcountButton.click()
    time.sleep(5)
    # CLick ok
    OkButton = find_my_element(driver, "XPATH", WELCOME_OK_BUTTON)
    check_not_found(driver, OkButton, "Welcome window did not appear")
    OkButton.click()
    time.sleep(2)
    # check if Login page is not reached
    SignupPage = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, SignupPage, "Did not stay in sign up page")
    time.sleep(2)
    print("Signed up without verification test passed")
    driver.quit()


#! New
def login_button_test(driver):
    # ----------------- login button in sign up page -------
    # Click on login button
    x = 540.0
    y = 1698.0
    # tap on the location using the coordinates
    action = TouchAction(driver)
    action.tap(x=x, y=y).perform()
    time.sleep(5)
    # check if Login page is reached
    LoginPage = find_my_element(driver, "XPATH", EMAIL_TEXTBOX)
    check_not_found(driver, LoginPage, "Login page not reached")

    print("Login page reached successfuly")
    driver.quit()


#! New
def sign_up_valid_test(driver, Email, Password):
    # ---------------------------------------------- Testing valid email ---------------------------------------------- #
    # Enter email
    EmailTextbox = find_my_element(driver, "XPATH", SIGN_UP_EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.click()
    time.sleep(1)
    EmailTextbox = find_my_element(driver, "XPATH", SIGN_UP_EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.send_keys(Email)
    # Enter first name
    FirstNameTextbox = find_my_element(driver, "XPATH", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTextbox, "First name textbox not found")
    FirstNameTextbox.click()
    time.sleep(1)
    FirstNameTextbox = find_my_element(driver, "XPATH", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTextbox, "First name textbox not found")
    FirstNameTextbox.send_keys("UserFirstName")
    driver.implicitly_wait(5)
    # Enter last name
    LastNameTextbox = find_my_element(driver, "XPATH", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.click()
    time.sleep(1)
    LastNameTextbox = find_my_element(driver, "XPATH", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.send_keys("UserLastName")
    driver.implicitly_wait(5)
    # enter password
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.click()
    time.sleep(1)
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.send_keys(Password)
    # Confirm password
    ConfirmPasswordTextbox = find_my_element(driver, "XPATH", CONFIRM_PASSWORD_TEXTBOX)
    check_not_found(
        driver, ConfirmPasswordTextbox, "Confrim Password textbox not found"
    )
    ConfirmPasswordTextbox.click()
    time.sleep(1)
    ConfirmPasswordTextbox = find_my_element(driver, "XPATH", CONFIRM_PASSWORD_TEXTBOX)
    check_not_found(
        driver, ConfirmPasswordTextbox, "Confrim Password textbox not found"
    )
    ConfirmPasswordTextbox.send_keys(Password)

    driver.hide_keyboard()
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Sign up button not found")
    CreateAcountButton.click()
    time.sleep(5)
    # CLick ok
    OkButton = find_my_element(driver, "XPATH", WELCOME_OK_BUTTON)
    check_not_found(driver, OkButton, "Welcome window did not appear")
    OkButton.click()
    time.sleep(2)
    # check if Login page is reached
    LoginPage = find_my_element(driver, "XPATH", EMAIL_TEXTBOX)
    check_not_found(driver, LoginPage, "Login page not reached")
    time.sleep(5)
    print("Signed up successfuly")
    driver.quit()


#! New
def sign_in_new_account(driver, Email, Password):
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
    print("signed in with new account successfuly")
    time.sleep(2)
    driver.quit()


#! New
def sign_up_invalid_email(driver, Emails):
    # ---------------------------------------------- Testing Invalid emails ---------------------------------------------- #
    # ------------------- missing email-------------------
    # Enter first name
    FirstNameTextbox = find_my_element(driver, "XPATH", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTextbox, "First name textbox not found")
    FirstNameTextbox.click()
    time.sleep(1)
    FirstNameTextbox = find_my_element(driver, "XPATH", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTextbox, "First name textbox not found")
    FirstNameTextbox.send_keys("UserFirstName")
    driver.implicitly_wait(5)
    # Enter last name
    LastNameTextbox = find_my_element(driver, "XPATH", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.click()
    time.sleep(1)
    LastNameTextbox = find_my_element(driver, "XPATH", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.send_keys("UserLastName")
    driver.implicitly_wait(5)
    # enter password
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.click()
    time.sleep(1)
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.send_keys("Password")
    # Confirm password
    ConfirmPasswordTextbox = find_my_element(driver, "XPATH", CONFIRM_PASSWORD_TEXTBOX)
    check_not_found(
        driver, ConfirmPasswordTextbox, "Confrim Password textbox not found"
    )
    ConfirmPasswordTextbox.click()
    time.sleep(1)
    ConfirmPasswordTextbox = find_my_element(driver, "XPATH", CONFIRM_PASSWORD_TEXTBOX)
    check_not_found(
        driver, ConfirmPasswordTextbox, "Confrim Password textbox not found"
    )
    ConfirmPasswordTextbox.send_keys("Password")

    driver.hide_keyboard()
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Sign up button not found")
    CreateAcountButton.click()
    time.sleep(5)
    # Check if an alert is present
    MissingEmailAlert = find_my_element(driver, "XPATH", EMPTY_EMAIL_ALERT)
    check_not_found(driver, MissingEmailAlert, "Email is required alert is not found")
    time.sleep(1)
    # -------------------invalid emails-------------------
    InvalidEmails = Emails[1:]
    # loop on invalid emails and test them
    for Email in InvalidEmails:
        # Enter email
        EmailTextbox = find_my_element(driver, "XPATH", SIGN_UP_EMAIL_TEXTBOX)
        check_not_found(driver, EmailTextbox, "Email textbox not found")
        EmailTextbox.click()
        time.sleep(1)
        EmailTextbox = find_my_element(driver, "XPATH", SIGN_UP_EMAIL_TEXTBOX)
        check_not_found(driver, EmailTextbox, "Email textbox not found")
        EmailTextbox.set_text(Email)
        driver.hide_keyboard()
        CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
        check_not_found(driver, CreateAcountButton, "Sign up button not found")
        CreateAcountButton.click()
        time.sleep(2)

        # Check if an alert is present
        InvalidEmail = find_my_element(driver, "XPATH", INVALID_EMAIL_ALERT)
        check_not_found(driver, InvalidEmail, "Invalid not detected")
        time.sleep(2)
    # -------------------email already registered with wong password -------------------
    # TODO --------------------- Partially done -----------------------
    EmailTextbox = find_my_element(driver, "XPATH", SIGN_UP_EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.click()
    time.sleep(1)
    EmailTextbox = find_my_element(driver, "XPATH", SIGN_UP_EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.set_text("ayausamakhalifa@gmail.com")
    driver.hide_keyboard()
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Sign up button not found")
    CreateAcountButton.click()
    time.sleep(2)
    # Check if an alert is present
    WrongPasswordAlert = find_my_element(driver, "XPATH", ERROR_WINDOW_OK_BUTTON)
    check_not_found(
        driver, WrongPasswordAlert, "Wrong email or password alert did not appear"
    )
    WrongPasswordAlert.click()
    time.sleep(2)
    print("Invalid emails testcases passed")
    # -------------------email already registered with corretc password -------------------
    # enter password
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.click()
    time.sleep(1)
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.set_text("123456789")
    # Confirm password
    ConfirmPasswordTextbox = find_my_element(driver, "XPATH", CONFIRM_PASSWORD_TEXTBOX)
    check_not_found(
        driver, ConfirmPasswordTextbox, "Confrim Password textbox not found"
    )
    ConfirmPasswordTextbox.click()
    time.sleep(1)
    ConfirmPasswordTextbox = find_my_element(driver, "XPATH", CONFIRM_PASSWORD_TEXTBOX)
    check_not_found(
        driver, ConfirmPasswordTextbox, "Confrim Password textbox not found"
    )
    ConfirmPasswordTextbox.set_text("123456789")

    driver.hide_keyboard()
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Sign up button not found")
    CreateAcountButton.click()
    time.sleep(4)
    # check if Login page is reached
    LoginPage = find_my_element(driver, "XPATH", EMAIL_TEXTBOX)
    check_not_found(driver, LoginPage, "Login page not reached")
    time.sleep(5)
    print("Already registered email in sign up test passed")
    driver.quit()


#! New
def sign_up_invalid_tests(driver, Email, Passwords):
    # ---------------------------------------------- Testing invalid info ---------------------------------------------- #
    # Enter email
    EmailTextbox = find_my_element(driver, "XPATH", SIGN_UP_EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.click()
    time.sleep(1)
    EmailTextbox = find_my_element(driver, "XPATH", SIGN_UP_EMAIL_TEXTBOX)
    check_not_found(driver, EmailTextbox, "Email textbox not found")
    EmailTextbox.send_keys("NewEmail1@gmail.com")
    # Enter last name
    LastNameTextbox = find_my_element(driver, "XPATH", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.click()
    time.sleep(1)
    LastNameTextbox = find_my_element(driver, "XPATH", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.send_keys("UserLastName")
    time.sleep(1)
    # enter password
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.click()
    time.sleep(1)
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.send_keys(Passwords[0])
    # Confirm password
    ConfirmPasswordTextbox = find_my_element(driver, "XPATH", CONFIRM_PASSWORD_TEXTBOX)
    check_not_found(
        driver, ConfirmPasswordTextbox, "Confrim Password textbox not found"
    )
    ConfirmPasswordTextbox.click()
    time.sleep(1)
    ConfirmPasswordTextbox = find_my_element(driver, "XPATH", CONFIRM_PASSWORD_TEXTBOX)
    check_not_found(
        driver, ConfirmPasswordTextbox, "Confrim Password textbox not found"
    )
    ConfirmPasswordTextbox.send_keys(Passwords[0])

    driver.hide_keyboard()
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Sign up button not found")
    CreateAcountButton.click()
    time.sleep(5)
    # ------------------- First Name missing-------------------
    # Check if alert is present
    FirstNameMissingAlert = find_my_element(driver, "XPATH", FIRST_NAME_REQUIRED_ALERT)
    check_not_found(driver, FirstNameMissingAlert, "First name missing alert not found")
    time.sleep(5)
    #!--------------Above Tested --------------------
    # ------------------- Last Name missing-------------------
    # Enter first name
    FirstNameTextbox = find_my_element(driver, "XPATH", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTextbox, "First name textbox not found")
    FirstNameTextbox.click()
    time.sleep(1)
    FirstNameTextbox = find_my_element(driver, "XPATH", FIRT_NAME_TEXTBOX)
    check_not_found(driver, FirstNameTextbox, "First name textbox not found")
    FirstNameTextbox.send_keys("UserFirstName")
    # Remove last name
    LastNameTextbox = find_my_element(driver, "XPATH", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.click()
    time.sleep(1)
    LastNameTextbox = find_my_element(driver, "XPATH", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.set_text("")
    time.sleep(1)

    driver.hide_keyboard()
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Sign up button not found")
    CreateAcountButton.click()
    time.sleep(5)

    # Check if alert is present
    LastNameMissingAlert = find_my_element(driver, "XPATH", LAST_NAME_REQUIRED_ALERT)
    check_not_found(driver, LastNameMissingAlert, "First name missing alert not found")
    time.sleep(5)
    # ------------------- Password missing-------------------
    # Enter last name
    LastNameTextbox = find_my_element(driver, "XPATH", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.click()
    time.sleep(1)
    LastNameTextbox = find_my_element(driver, "XPATH", LAST_NAME_TEXTBOX)
    check_not_found(driver, LastNameTextbox, "Last name textbox not found")
    LastNameTextbox.send_keys("UserLastName")
    time.sleep(1)
    # Clear password field
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.click()
    time.sleep(1)
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.set_text("")
    time.sleep(1)

    driver.hide_keyboard()
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Sign up button not found")
    CreateAcountButton.click()
    time.sleep(5)
    # Check if alert is present
    PasswordMissingAlert = find_my_element(driver, "XPATH", PASSWORD_REQUIRED_ALERT)
    check_not_found(driver, PasswordMissingAlert, "First name missing alert not found")

    # -------------------password < 8 characters-------------------
    time.sleep(5)
    # Clear password field
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.click()
    time.sleep(1)
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.set_text("123")
    time.sleep(1)

    driver.hide_keyboard()
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Sign up button not found")
    CreateAcountButton.click()
    time.sleep(5)
    # Check if alert is present
    PasswordMissingAlert = find_my_element(driver, "XPATH", INVALID_PASSWORD_ALERT)
    check_not_found(
        driver,
        PasswordMissingAlert,
        "Password should be at least 8 char alert did not appear",
    )
    # --------------------------Wrong confirm password --------------
    # Add password
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.click()
    time.sleep(1)
    PasswordTextbox = find_my_element(driver, "XPATH", SIGN_UP_PASSWORD_TEXTBOX)
    check_not_found(driver, PasswordTextbox, "Password textbox not found")
    PasswordTextbox.set_text("123456789")
    time.sleep(1)

    # clear confirm password textbox
    ConfirmPasswordTextbox = find_my_element(driver, "XPATH", CONFIRM_PASSWORD_TEXTBOX)
    check_not_found(
        driver, ConfirmPasswordTextbox, "Confrim Password textbox not found"
    )
    ConfirmPasswordTextbox.click()
    time.sleep(1)
    ConfirmPasswordTextbox = find_my_element(driver, "XPATH", CONFIRM_PASSWORD_TEXTBOX)
    check_not_found(
        driver, ConfirmPasswordTextbox, "Confrim Password textbox not found"
    )
    ConfirmPasswordTextbox.set_text("")

    driver.hide_keyboard()
    CreateAcountButton = find_my_element(driver, "XPATH", CREATE_ACOUNT_BUTON)
    check_not_found(driver, CreateAcountButton, "Sign up button not found")
    CreateAcountButton.click()
    time.sleep(5)
    # Check if alert is present
    PasswordMissingAlert = find_my_element(driver, "XPATH", PASSWORD_MISMATCH_ALERT)
    check_not_found(
        driver,
        PasswordMissingAlert,
        "Password does not match alert did not appear",
    )

    print("Invalid testcases passed")
    time.sleep(10)
    driver.quit()


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
    driver.quit()


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
    driver.quit()
