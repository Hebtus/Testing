# ---------------- This file is used to easily map references for elements to the ones already used ----------------#
# ---------------- Attendee's View ----------------#
# Login page
# "//android.view.View//android.widget.TextView[@text='Location/Online' and @class='android.widget.TextView']"
PASSWORD_TEXTBOX = "//android.view.View//android.widget.EditText[@class='android.widget.EditText'][position() = 2]"  #! New
EMAIL_TEXTBOX = "//android.view.View//android.widget.EditText[@class='android.widget.EditText'][position() = 1]"  #! New
LOGIN_BUTTON = "//android.widget.Button[@content-desc='Log In']"  #! New
LANDING_PAGE = "//android.view.View//android.widget.ScrollView[@class='android.widget.ScrollView'][position() = 1]"  #! New
PROFILE_ICON = "//android.view.View//android.view.View[@class='android.view.View'][position() = 2]"  #! New
SIGN_OUT_BUTTON = (
    "//android.view.View//android.widget.Button[@content-desc='Sign out']"  #! New
)
# Invalid Login email or password
ERROR_WINDOW_OK_BUTTON = (
    "//android.view.View//android.widget.Button[@content-desc='OK']"  #! New
)
# ---------------------------------------------------------------------------------------------------
# sign up button in login page
SIGN_UP_BUTTON_LP = "//android.widget.LinearLayout//android.widget.FrameLayout//android.widget.FrameLayout//android.view.View//android.view.View//android.view.View//android.view.View//android.view.View//android.widget.Button[@content-desc='Don't have an account? Sign Up.'][position() = 8]"  #! New

# ---------------------------------------------------------------------------------------------------
SIGN_UP_EMAIL_TEXTBOX = "//android.widget.ScrollView//android.widget.EditText[@class='android.widget.EditText'][position() = 1]"  #! New
FIRT_NAME_TEXTBOX = "//android.widget.ScrollView//android.widget.EditText[@class='android.widget.EditText'][position() = 2]"  #! New
LAST_NAME_TEXTBOX = "//android.widget.ScrollView//android.widget.EditText[@class='android.widget.EditText'][position() = 3]"  #! New
SIGN_UP_PASSWORD_TEXTBOX = "//android.widget.ScrollView//android.widget.EditText[@class='android.widget.EditText'][position() = 4]"  #! New
CONFIRM_PASSWORD_TEXTBOX = "//android.widget.ScrollView//android.widget.EditText[@class='android.widget.EditText'][position() = 5]"  #! New
CREATE_ACOUNT_BUTON = "//android.widget.ScrollView//android.widget.Button[@content-desc='Sign Up']"  #! New
# ---------------------------------------------------------------------------------------------------


CONTINUE_BUTTON = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/form/div[2]/div/button"
EMAIL_CONFIRMATION_TEXTBOX = "emailConfirmation"
TERMS_CONDITIONS_POPUP_WINDOW = "edsModalContentChildren"
AGREE_BUTTON = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/main/div/div/div/div/div/div[2]/button[2]"
START_ATTENDING_BUTTON = "/html/body/div[1]/div/div[2]/div/div[3]/div[1]/div[3]/button"
EXIT_BUTTON_1 = "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/button[1]"
EXIT_BUTTON_2 = "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div/main/div/div/div/div[1]/button"
WHITE_SPACE_SIGNUP_PAGE = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[1]/div[1]/h1"
# login button in sinup page
SIGNUP_LOGIN_BUTTON = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[4]/button"

# signup invalid tests
INVALID_EMAIL_ALERT = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/form/div[1]/div[1]/div[2]/div/aside"
EMAIL_ALREADY_USED_ALERT = (
    "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[2]/div"
)
EMAIL_DONT_MATCH_ALERT = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/form/div[1]/div[2]/div/div[2]/div/aside"
LAST_NAME_REQUIRED_ALERT = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/form/div[1]/div[3]/div[1]/div[2]/div/div[2]/div/aside"
FIRST_NAME_REQUIRED_ALERT = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/form/div[1]/div[3]/div[1]/div[1]/div/div[2]/div/aside"
PASSWORD_REQUIRED_ALERT = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/form/div[1]/div[3]/div[2]/div[1]/div/div[2]/div/aside"

# login with google and facebook
SIGNUP_WITH_FACEBOOK_BUTTON = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[3]/div[1]/div[2]/div/ul/li/div/div/button"
LOGIN_WITH_FACEBOOK_BUTTON = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[5]/div/div[2]/div/ul/li[1]/div/div/button"
FACEBOOK_EMAIL_TEXTBOX = "email"
FACEBOOK_PASSWORD_TEXTBOX = "pass"
FACEBOOK_LOGIN_BUTTON = "/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input"
FACEBOOK_CONTINUE_BUTTON = (
    "/html/body/div/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div"
)
LOGIN_WITH_GOOGLE_BUTTON = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[3]/div[1]/div[1]/div/div/button"
AD_EXIT_BUTTON = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/div/div/div/div/div/div[2]/span/button"
AD_WANT_TO_LEAVE_BUTTON = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/div/div/div/div/div/div[1]/div/div/main/div/div/div/div[2]/button[1]"
ACCEPT_BUTTON = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[3]/div[2]/div/div/div/div/div[1]/div/div/main/div/div/div/div/div/div[2]/button[2]"
# sign in Page
UNREGISTERED_EMAIL_ALERT = (
    "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[2]/div"
)
INCORRECT_PASSWORD_ALERT = (
    "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[2]/div"
)
# SIGNIN_BUTTON = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[3]/div/form/div[4]/div/button"
# LOGIN_BUTTON = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[2]/div/form/div[4]/div/button"
# Forget password
FORGET_PASSWORD_BUTTON = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[3]/div/div/div/div/button"
GMAIL_TEXTBOX = "identifierId"
NEXT_BUTTON = "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button"
GMAIL_PASSWORD_TEXTBOX = "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
PASSWORD_NEXT_BUTTON = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button"
FIRST_EMAIL = "/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[9]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[4]/div[2]"
SET_NEW_PASSWORD_LINK = "Set a New Password"
UPDATE_PASSWORD_BUTTON = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/form/div[2]/button"

# Events Page
IMAGE = "/html/body/div/div/div[2]/div/div[1]/img"  #! New
START_DATE = "/html/body/div/div/div[2]/div/div[2]/div[1]/time"  #! New
EVENT_TITLE = "/html/body/div/div/div[2]/div/div[2]/div[2]/h1"  #! New
DATE_TIME = "/html/body/div/div/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/p"  #! New
LOCATION = (
    "/html/body/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/p/strong"  #! New
)
EVENTS_DETAILS = "/html/body/div/div/div[2]/div/div[2]/div[4]/p"  #! New
TICKETS_INFO = "/html/body/div/div/div[2]/div/div[3]/div"  #! New
GET_TICKET_BUTTON = "/html/body/div/div/div[2]/div/div[3]/div/div"  #! New
EVENT_SUMMARY = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[2]/div[1]/p"
SIMPLIDIED_ORGANIZER_INFO = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[2]/div[2]/div"
SHARE_WITH_FRIENDS = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[2]/div[2]/section[2]/div/div[2]/div/div"
ORGANIZER_INFO = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[2]/div[2]"
OTHER_EVENTS_YOU_MAY_LIKE = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[2]/section/div/div[1]/section/div/div/div/div[1]"
# RESERVE_SPOT_BUTTON = "/html/body/div[1]/div/section/button"
RESERVE_SPOT_BUTTON = "//*[@id='root']/div/section/button"

CHECKOUT_BUTTON = "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/main/div/div[2]/div/div/div[3]/button"
TICKETS_BUTTON = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[3]/div/div[2]/button"
ADD_TICKET_BUTTON = "/html/body/div[1]/div/section/form/div/div/div/ul/li/div/div/div[1]/div[2]/div/button[2]"
LIKE_BUTTON = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[2]/div[2]/section[2]/div[1]/section/div/div[2]/div[3]/div/article/div[2]/div/span[2]/span/button"
SHARE_BUTTON = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[2]/div[2]/section[2]/div[1]/section/div/div[2]/div[3]/div/article/div[2]/div/span[1]/span/button"
FOLLOW_BUTTTON = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[2]/div[1]/section/div[2]/button"
REGISTER_PAGE = "/html/body/div[1]/div/div/div/div/div[1]"

# Landing page: #? Edited
EVENT_ELEMENT = "card Events_event-card__4cxKy"  #! New
EVENT_LIST_1 = "/html/body/div/div/div[3]/div/div/div/div["  #! New
EVENT_LIST_2 = "]/div"  #! New

LOCATION_PICKER = "location-text"
SEE_MORE_BUTTON = "See more"
SEE_MORE_PAGE = (
    "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/div/div/section[1]"
)

ALL_EVENT_DATE_1 = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/div/div/div/section/div/div[1]/div/div["
ALL_EVENT_DATE_2 = "]/div/div/article/div[1]/div[2]/div/div[1]/div"
ALL_EVENTS_LOCATION_1 = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/div/div/div/section[1]/div/div/div[2]/div["
ALL_EVENTS_LOCATION_2 = "]/div/div/article/div[1]/div[2]/div/div[2]/div[1]/div"
# Tabs:
TODAY_TAB = "today-link"  #! New
START_DATE_1 = "/html/body/div/div/div[3]/div/div/div/div["  #! New
START_DATE_2 = "]/div/div/h6[1]"  #! New
END_DATE_1 = "/html/body/div/div/div[3]/div/div/div/div["  #! New
END_DATE_2 = "]/div/div/h6[2]"  #! New
THIS_WEEKEND_TAB = "this-weekend-tab"  #! New

ALL_TAB = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/nav/ul/li[1]/button"
FOR_YOU_TAB = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/nav/ul/li[2]/button"
ONLINE_TAB = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/nav/ul/li[3]/button"
ONLINE_INFO_1 = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[2]/section/div[2]/section[2]/div/div/div[2]/p"
ONLINE_INFO_2 = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[2]/section/div[2]/section[2]/div/div/div[2]/p"

TODAY_EVENT_DATE_1 = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/div/div/div/section[1]/div/div/div/div["
TODAY_EVENT_DATE_2 = "]/div/div/article/div[1]/div[2]/div/div[1]/div"

WEEKEND_EVENT_DATE_1 = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/div/div/div/section[1]/div/div/div/div["
WEEKEND_EVENT_DATE_2 = "]/div/div/article/div[1]/div[2]/div/div[1]/div"

WOMENS_HISTORY_MONTH = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/nav/ul/li[7]/button"
FREE_TAB = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/nav/ul/li[8]/button"
FREE_INFO_1 = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[3]/div[2]/div[1]/div"
FREE_INFO_2 = (
    "/html/body/div[1]/div/section/form/div/div/div/ul/li/div/div/div[2]/div/span"
)
MUSIC_TAB = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/nav/ul/li[9]/button"
FOOD_DRINK_TAB = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/nav/ul/li[10]/button"
CHARITY_CAUSES_TAB = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/nav/ul/li[11]/button"
# Categories:
MUSIC_CATEGORY = "Music"
HOBBBIES_CATEGORY = "Hobbies"
VISUAL_ARTS_CATEGORY = "Performing & Visual Arts"
BUSINESS_CATEGORY = "Business"
HOLDIDAY_CATEGORY = "Holiday"
FOOD_DRINK_CATEGORY = "Food & Drink"
HEALTH_CATEGORY = "Health"
SPORTS_CATEGORY = "Sports & Fitness"

# ---------------- Creator's View ----------------#
# Beginning
ONLY_ONCE_LOCATION = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.Button[2]"
ACCOUNT_ICON = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]"
MANAGE_MY_EVENTS = "//android.widget.Button[@content-desc='Manage my events']"


# Basic Info Web Page
CREATE_EVENT_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button" # XPATH
SAVE_BUTTON = "//android.widget.Button[@content-desc='Save']"
EVENT_TITLE = "//android.view.View[@content-desc='Basic info']"
EVENT_NAME_FIELD = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[1]" # XPATH
EVENT_NAME_ERROR_MSG = "//android.view.View[@content-desc='Please enter event name ']"
EVENT_NAME_RATIO_PART1 = "//android.view.View[@content-desc='" # 0/75
EVENT_NAME_RATIO_PART2 = "']"
EVENT_TAGS_FIELD = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText"
EVENT_TAGS_TITLE = "//android.view.View[@content-desc='Tags']"
EVENT_TAG_RATIO_PART1 = "//android.view.View[@content-desc='" # 0/25
EVENT_TAG_RATIO_PART2 = "']"
EVENT_TAG_ADD_ID = "Tag"
EVENT_TAG_ADD = "//android.widget.Button[@content-desc='Add']"
EVENT_CATEGORY_MUSIC = "//android.widget.Button[@content-desc='Music']"
EVENT_CATEGORY_CHARITY = "//android.view.View[@content-desc='Charity & Causes']"
EVENT_CATEGORY_CHARITY_ID = "Charity & Causes"
EVENT_LOCATION_TITLE = "//android.view.View[@content-desc='Location']"
EVENT_VENUE_BUTTON = "//android.widget.Button[@content-desc='Venue']"
EVENT_VENUE_FIELD = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText"
EVENT_VENUE_ERROR_MSG = "//android.view.View[@content-desc='Please enter event location']"
EVENT_ONLINE_BUTTON = "//android.widget.Button[@content-desc='Online event']"
EVENT_TO_BE_ANNOUNCED = "//android.widget.Button[@content-desc='To be annonced']"
EVENT_VENUE_ERROR_MSG = "//android.view.View[@content-desc='Please enter event location']"
EVENT_DATE_TITLE = "//android.view.View[@content-desc='Date and time']"
EVENT_SINGLE_EVENT_BUTTON = "//android.widget.Button[@content-desc='Single event']"
EVENT_RECURRING_EVENT_BUTTON = "//android.widget.Button[@content-desc='Recurring Event']"
EVENT_RECURRING_MESSAGE = "	//android.view.View[@content-desc='You’ll be able to set a schedule for your recurring event in the next step. Event details and ticket types will apply to all instances.']"
EVENT_START_DATE_FIELD = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[1]"
EVENT_END_DATE_FIELD = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[2]"
EVENT_START_DATE_ERROR_MSG = "//android.view.View[@content-desc='Please enter event start date ']"
EVENT_START_DATE_CALENDAR = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[1]/android.widget.Button"
EVENT_END_DATE_CALENDAR = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[2]/android.widget.Button"
EVENT_DATE_CHOOSE_CALENDAR_PART1 = "//android.view.View[@content-desc='" # 12, Wednesday, April 12, 2023
EVENT_DATE_CHOOSE_CALENDAR_PART2 = "']"
EVENT_CALENDAR_NEXT_PART1 = "//android.view.View[@content-desc='SELECT DATE " # Fri, Apr 21
EVENT_CALENDAR_NEXT_PART2 = "']/android.widget.Button[4]"
EVENT_CALENDAR_PREV_PART1 = "//android.view.View[@content-desc='SELECT DATE " # Fri, Apr 21
EVENT_CALENDAR_PREV_PART2 = "']/android.widget.Button[3]"
EVENT_TIME_DROPDOWN = "//android.widget.Button[@content-desc='01:00']" # index 2 and 4
EVENT_CHOOSE_TIME_PART1 = "//android.view.View[@content-desc='" # 02:00
EVENT_CHOOSE_TIME_PART2 = "']" 
EVENT_CHOSEN_TIME_PART1 = "//android.widget.Button[@content-desc='" # 02:00
EVENT_CHOSEN_TIME_PART2 = "']"
EVENT_DISPLAY_START_TIME_BUTTON = "//android.widget.CheckBox[@content-desc='Display start time']"
EVENT_DISPLAY_END_TIME_BUTTON = "//android.widget.CheckBox[@content-desc='Display end time']"
EVENT_IMAGE_TITLE = "//android.view.View[@content-desc='Image upload']"
EVENT_IMAGE_UPLOAD_BUTTON = "//android.widget.Button[@content-desc='Upload Photo']"
EVENT_DESCRIPTION_TITLE = "//android.view.View[@content-desc='Description']"
EVENT_DESCRIPTION_FIELD = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[3]"

# Event List
EVENT_LIST_TITLE = "//android.view.View[@content-desc='hey there!']"
EXPORT_TO_CSV = "//android.widget.Button[@content-desc='Export to CSV']"
EVENT_LIST_FILTER = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.Button[1]"

# In between
#FIRST_EVENT = "//android.view.View[@content-desc='description Egyptian Fox Border Point, New Valley, Egypt Mon, May 15, 2023 at 2:00 AM']"
SECOND_EVENT = "//android.view.View[@content-desc='youssef Cairo, Egypt Sun, May 14, 2023 at 2:00 AM']"
MENU_DASHBOARD = "//android.widget.Button[@content-desc='Dashboard']"
MAIN_MENU_TICKETS = "//android.view.View[@content-desc='Tickets']"
MAIN_MENU_PUBLISH = "//android.view.View[@content-desc='Publish']"
MAIN_MENU_DASHBOARD = "//android.view.View[@content-desc='dashboard']"
MAIN_MENU_BASIC_INFO = "//android.view.View[@content-desc='Basic info']"

# Dashboard
DASHBOARD_TITLE = "//android.widget.Button[@content-desc='Dashboard']"

# -- Tickets
TICKETS_TITLE = "//android.widget.Button[@content-desc='Tickets']"
ADMISSION_BUTTON = "//android.widget.Button[@content-desc='Admission']"
ADMISSION_BUTTON_ID = "Admission"
PROMO_CODE_BUTTON = "//android.widget.Button[@content-desc='Promo code']"
PROMO_CODE_BUTTON_ID = "Promo code"
ADD_MORE_TICKETS = "//android.widget.Button[@content-desc='+ Add more tickets']"
ADD_MORE_TICKETS_ID = "+ Add more tickets"
REFRESH = "//android.widget.Button[@content-desc='Refresh']"
REFRESH_ID = "Refresh"

# Add more tickets
REGULAR = "//android.widget.Button[@content-desc='Regular']"
REGULAR_TITLE = "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[15]/span[3]/span/span"
VIP = "//android.widget.Button[@content-desc='VIP']" #content-desc
VIP_ID = "VIP"
VIP_TITLE = "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[15]/span[3]/span/span/b"
ADD_TICKETS_NAME = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[1]"
ADD_TICKETS_PRICE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[2]"
ADD_TICKETS_QUANTITY = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[3]"
ADD_TICKETS_DATE_AND_TIME = "//android.widget.Button[@content-desc='Date & time']"
ADD_TICKETS_DATE_AND_TIME_ID = "Date & time"
ADD_TICKETS_WHEN_SALES_END = "//android.view.View[@content-desc='When sales end']"
ADD_TICKETS_WHEN_SALES_END_ID = "When sales end"
ADD_TICKETS_EVENT_STARTS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.Button[2]"
ADD_TICKETS_EVENT_ENDS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.Button[4]"
ADD_TICKETS_EVENT_START_TIME = "(//android.widget.Button[@content-desc='02:00'])[1]"
ADD_TICKETS_EVENT_END_TIME= "(//android.widget.Button[@content-desc='02:00'])[2]"
ADD_TICKET_BTN = "//android.widget.Button[@content-desc='Add']"
ADD_TICKET_BTN_ID = "Add"
TICKET_ADDED_SUCCESSFULLY = "//android.view.View[@content-desc='The ticket was added successfully']"
ADD_TICKETS_GO_BACK = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button"
TICKET_CARDS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View/android.view.View"
THREE_DOTS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View/android.view.View[2]/android.view.View/android.widget.Button"
# view added tickets
TICKET_NAMES = "//android.widget.ScrollView//android.view.View//android.view.View//android.view.View//android.view.View[1]"
TICKET_PRICES = "//android.widget.ScrollView//android.view.View//android.view.View//android.view.View//android.view.View[3]"
TICKET_QUANTITIES = "//android.widget.ScrollView//android.view.View//android.view.View//android.view.View//android.view.View[5]"





