# ---------------- This file is used to easily map references for elements to the ones already used ----------------#
# ---------------- Attendee's View ----------------#
# Login page
# "//android.view.View//android.widget.TextView[@text='Location/Online' and @class='android.widget.TextView']"
#! Phase 4:
PASSWORD_TEXTBOX = "//android.view.View//android.widget.EditText[@class='android.widget.EditText'][position() = 2]"
EMAIL_TEXTBOX = "//android.view.View//android.widget.EditText[@class='android.widget.EditText'][position() = 1]"
LOGIN_BUTTON = "//android.widget.Button[@content-desc='Log In']"
LANDING_PAGE = "//android.view.View//android.widget.ScrollView[@class='android.widget.ScrollView'][position() = 1]"
PROFILE_ICON = (
    "//android.view.View//android.view.View[@class='android.view.View'][position() = 2]"
)
SIGN_OUT_BUTTON = "//android.view.View//android.widget.Button[@content-desc='Sign out']"
# Invalid Login email or password
ERROR_WINDOW_OK_BUTTON = (
    "//android.view.View//android.widget.Button[@content-desc='OK']"
)
# ---------------------------------------------------------------------------------------------------
# sign up button in login page
WELCOME_OK_BUTTON = "//android.view.View//android.widget.Button[@content-desc='OK']"
# ---------------------------------------------------------------------------------------------------
SIGN_UP_EMAIL_TEXTBOX = "//android.widget.ScrollView//android.widget.EditText[@class='android.widget.EditText'][position() = 1]"
FIRT_NAME_TEXTBOX = "//android.widget.ScrollView//android.widget.EditText[@class='android.widget.EditText'][position() = 2]"
LAST_NAME_TEXTBOX = "//android.widget.ScrollView//android.widget.EditText[@class='android.widget.EditText'][position() = 3]"
SIGN_UP_PASSWORD_TEXTBOX = "//android.widget.ScrollView//android.widget.EditText[@class='android.widget.EditText'][position() = 4]"
CONFIRM_PASSWORD_TEXTBOX = "//android.widget.ScrollView//android.widget.EditText[@class='android.widget.EditText'][position() = 5]"
CREATE_ACOUNT_BUTON = (
    "//android.widget.ScrollView//android.widget.Button[@content-desc='Sign Up']"
)
# ---------------------------------------------------------------------------------------------------
# signup invalid tests
EMPTY_EMAIL_ALERT = '//android.widget.EditText//android.view.View[@content-desc="Email field can\'t be empty."]'
INVALID_EMAIL_ALERT = "//android.widget.EditText//android.view.View[@content-desc='Please Enter a valid email']"
FIRST_NAME_REQUIRED_ALERT = '//android.widget.EditText//android.view.View[@content-desc="First Name can\'t be empty"]'
LAST_NAME_REQUIRED_ALERT = '//android.widget.EditText//android.view.View[@content-desc="Last Name can\'t be empty"]'
PASSWORD_REQUIRED_ALERT = '//android.widget.EditText//android.view.View[@content-desc="Password field can\'t be empty"]'
INVALID_PASSWORD_ALERT = '//android.widget.EditText//android.view.View[@content-desc="Password must be at least 8 characters"]'
PASSWORD_MISMATCH_ALERT = '//android.widget.EditText//android.view.View[@content-desc="Password doesn\'t match"]'
# ---------------------------------------------------------------------------------------------------
# Events Page
EVENT = "//android.view.View[@index='0']//android.widget.ImageView[@index='0'and @class='android.widget.ImageView'][1]"
IMAGE = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1'and @class='android.widget.ScrollView']"
TICKETS_INFO = "//android.widget.ScrollView[@index='1']//android.view.View[@index='2']"
START_DATE = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1']//android.view.View[@index='2'and @class='android.view.View']"
EVENT_TITLE = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1']//android.view.View[@index='3'and @class='android.view.View']"
DATE_TIME = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1']//android.view.View[@index='6'and @class='android.view.View']"
LOCATION = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1']//android.view.View[@index='8'and @class='android.view.View']"

NO_TICKETS = "//android.view.View[@index='0']//android.view.View[@index='2' and @content-desc='No tickets available'and @class='android.view.View']"
# Booking
GET_TICKET_BUTTON = "//android.view.View[@index='2']//android.widget.Button[@index='0' and @content-desc='Get tickets' and @class='android.widget.Button']"
TICKETS_TYPES = "//android.view.View[@index='0']//android.widget.Button[@index='0'and @class='android.widget.Button']"
LEAVE_BUTTON = "//android.view.View[@index='0']//android.widget.Button[@index='3' and @content-desc='Leave' and @class='android.widget.Button']"
STAY_BUTTON = "//android.view.View[@index='0']//android.widget.Button[@index='2' and @content-desc='Stay' and @class='android.widget.Button']"

# Checkout page
B_BACK_BUTTON = "//android.view.View[@index='0']//android.widget.Button[@index='0'and @class='android.widget.Button']"
B_FIRST_NAME_TB = "//android.view.View[@index='0']//android.widget.EditText[@index='1'and @class='android.widget.EditText']"
B_LAST_NAME_TB = "//android.view.View[@index='0']//android.widget.EditText[@index='2'and @class='android.widget.EditText']"
B_EMAIL_TB = "//android.view.View[@index='0']//android.widget.EditText[@index='3'and @class='android.widget.EditText']"
B_PHONE_NUM_TB = "//android.view.View[@index='0']//android.widget.EditText[@index='4'and @class='android.widget.EditText']"
B_GENDER_TB = "//android.view.View[@index='0']//android.widget.EditText[@index='5'and @class='android.widget.EditText']"
B_PROMOCODE_TB = "//android.view.View[@index='0']//android.widget.EditText[@index='6'and @class='android.widget.EditText']"

B_DONE_BUTTON = "//android.view.View[@index='0']//android.view.View[@index='7']//android.widget.Button[@index='0' and @content-desc='Done' and @class='android.widget.Button']"
B_SUMMARY_BUTTON = "//android.view.View[@index='0']//android.view.View[@index='7']//android.widget.Button[@index='1' and @content-desc='Order summary' and @class='android.widget.Button']"
SUMMARY_TICKET_1 = "//android.view.View[@index='0']//android.view.View[@index='2'and @class='android.view.View']"
SUMMARY_TICKET_2 = "//android.view.View[@index='0']//android.view.View[@index='5'and @class='android.view.View']"

ALERT_BACK_BUTTON = "//android.widget.FrameLayout[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.widget.Button[@index='0' and @content-desc='back' and @class='android.widget.Button']"

TIME_LIMIT_ALERT = "//android.view.View[@index='0']//android.widget.Button[@index='2' and @content-desc='Back to tickets' and @class='android.widget.Button']"
# Choose tickets page
TICKET_TYPE_1 = "//android.widget.Button[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.view.View[@index='0' and @class='android.view.View']"
TICKET_TYPE_2 = "//android.widget.Button[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.view.View[@index='1' and @class='android.view.View']"

PLUS_BUTTON_1 = "//android.widget.Button[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.widget.Button[@index='0'and @class='android.widget.Button']"
MINUS_BUTTON_1 = "//android.widget.Button[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.widget.Button[@index='1'and @class='android.widget.Button']"

PLUS_BUTTON_2 = "//android.widget.Button[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.view.View[@index='1']//android.widget.Button[@index='0'and @class='android.widget.Button']"

MINUS_BUTTON_2 = "//android.widget.Button[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.view.View[@index='1']//android.widget.Button[@index='1'and @class='android.widget.Button']"
BOOK_TICKET_BUTTON = "//android.view.View[@index='0']//android.widget.Button[@index='0']//android.widget.Button[@index='1' and @content-desc='Book tickets' and @class='android.widget.Button']"

CHOOSE_TICKET_ALERT = "//android.view.View[@index='0']//android.view.View[@index='1' and @content-desc='Please choose a ticket' and @class='android.view.View']"
CLOSE_ALERT = "//android.view.View[@index='0']//android.widget.Button[@index='2' and @content-desc='Close' and @class='android.widget.Button']"

EVENTS_DETAILS_1 = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1']//android.view.View[@index='4'and @class='android.view.View']"
EVENTS_DETAILS_2 = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1']//android.view.View[@index='5'and @class='android.view.View']"
# ---------------------------------------------------------------------------------------------------
# Landing page:
EVENT_1 = "//android.view.View[@index='"
EVENT_2 = (
    "']//android.widget.ImageView[@index='0'and @class='android.widget.ImageView'][1]"
)

EVENT_ELEMENT = "card Events_event-card__4cxKy"
EVENT_LIST_1 = "/html/body/div/div/div[3]/div/div/div/div["
EVENT_LIST_2 = "]/div"

SEE_MORE_BUTTON = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1']//android.widget.Button[@content-desc='See more' and @index='2'and @class='android.widget.Button']"
HEBTUS_BUTTON = "//android.view.View[@index='0']//android.widget.Button[@content-desc='Hebtus' and @index='0'and @class='android.widget.Button']"
SEE_MORE_PAGE = "//android.widget.ScrollView[@index='1']//android.view.View[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.widget.ImageView[@index='0'and @class='android.widget.ImageView']"

# location
LOCATION_TEXT = "//android.widget.ScrollView[@index='1']//android.view.View[@index='1' and @class='android.view.View']"
LOCATION_PICKER_TB = "//android.widget.ScrollView[@index='1']//android.widget.EditText[@index='6' and @class='android.widget.EditText']"
SEARCH_BUTTON = "//android.widget.ScrollView[@index='1']//android.widget.Button[@content-desc='Search' and @index='7' and @class='android.widget.Button']"
DROP_DOWN_MENU = "//android.widget.ScrollView[@index='1']//android.view.View[@index='5' and @class='android.view.View']"
CURRENT_LOCATION_BUTTON = "//android.view.View[@index='0']//android.widget.Button[@content-desc='use current Location' and @index='0'and @class='android.widget.Button']"
# tabs
ALL_TAB = "//android.view.View[@index='0']//android.widget.Button[@content-desc='All' and @index='0'and @class='android.widget.Button']"
MUSIC_TAB = "//android.view.View[@index='1']//android.widget.Button[@content-desc='Music' and @index='0'and @class='android.widget.Button']"
FOOD_DRINK_TAB = "//android.view.View[@index='2']//android.widget.Button[@content-desc='Food & Drink' and @index='0'and @class='android.widget.Button']"
CHARITY_CAUSES_TAB = "//android.view.View[@index='3']//android.widget.Button[@content-desc='Charity & Causes' and @index='0'and @class='android.widget.Button']"
ONLINE_TAB = "//android.widget.HorizontalScrollView[@index='8']//android.view.View[@index='2']//android.widget.Button[@content-desc='Online' and @index='0'and @class='android.widget.Button']"
TODAY_TAB = "//android.widget.HorizontalScrollView[@index='8']//android.view.View[@index='0']//android.widget.Button[@content-desc='Today' and @index='0'and @class='android.widget.Button']"
THIS_WEEKEND_TAB = "//android.widget.HorizontalScrollView[@index='8']//android.view.View[@index='1']//android.widget.Button[@content-desc='This Weekend' and @index='0'and @class='android.widget.Button']"
FREE_TAB = "//android.widget.HorizontalScrollView[@index='8']//android.view.View[@index='2']//android.widget.Button[@content-desc='Free' and @index='0'and @class='android.widget.Button']"

# Categories:
MUSIC_CATEGORY = "//android.view.View[@index='10']//android.view.View[@index='0']//android.view.View[@index='0']//android.view.View[@content-desc='Music' and @index='0'and @class='android.view.View']"
FOOD_DRINK_CATEGORY = "//android.view.View[@index='10']//android.view.View[@index='0']//android.view.View[@index='1']//android.view.View[@content-desc='Food & Drink' and @index='0'and @class='android.view.View']"
CHARITY_CATEGORY = "//android.view.View[@index='0']//android.view.View[@index='0']//android.view.View[@index='2']//android.view.View[@content-desc='Charity & Causes' and @index='0'and @class='android.view.View']"
#!END ---------------------------------------------------------------------------------------------------

EMAIL_ALREADY_USED_ALERT = (
    "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[2]/div"
)
EMAIL_DONT_MATCH_ALERT = "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/form/div[1]/div[2]/div/div[2]/div/aside"


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

# Landing page:
EVENT_ELEMENT = "card Events_event-card__4cxKy"
EVENT_LIST_1 = "/html/body/div/div/div[3]/div/div/div/div["
EVENT_LIST_2 = "]/div"


ALL_EVENT_DATE_1 = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/div/div/div/section/div/div[1]/div/div["
ALL_EVENT_DATE_2 = "]/div/div/article/div[1]/div[2]/div/div[1]/div"
ALL_EVENTS_LOCATION_1 = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/div/div/div/section[1]/div/div/div[2]/div["
ALL_EVENTS_LOCATION_2 = "]/div/div/article/div[1]/div[2]/div/div[2]/div[1]/div"


START_DATE_1 = "/html/body/div/div/div[3]/div/div/div/div["
START_DATE_2 = "]/div/div/h6[1]"
END_DATE_1 = "/html/body/div/div/div[3]/div/div/div/div["
END_DATE_2 = "]/div/div/h6[2]"


# ----------------------------------------------------------------

FOR_YOU_TAB = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/nav/ul/li[2]/button"
ONLINE_INFO_1 = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[2]/section/div[2]/section[2]/div/div/div[2]/p"
ONLINE_INFO_2 = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[2]/section/div[2]/section[2]/div/div/div[2]/p"

TODAY_EVENT_DATE_1 = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/div/div/div/section[1]/div/div/div/div["
TODAY_EVENT_DATE_2 = "]/div/div/article/div[1]/div[2]/div/div[1]/div"

WEEKEND_EVENT_DATE_1 = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/div/div/div/section[1]/div/div/div/div["
WEEKEND_EVENT_DATE_2 = "]/div/div/article/div[1]/div[2]/div/div[1]/div"

WOMENS_HISTORY_MONTH = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/section[2]/div/div/div[2]/div/div/nav/ul/li[7]/button"
FREE_INFO_1 = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[3]/div[2]/div[1]/div"
FREE_INFO_2 = (
    "/html/body/div[1]/div/section/form/div/div/div/ul/li/div/div/div[2]/div/span"
)

HOBBBIES_CATEGORY = "Hobbies"
VISUAL_ARTS_CATEGORY = "Performing & Visual Arts"
BUSINESS_CATEGORY = "Business"
HOLDIDAY_CATEGORY = "Holiday"
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
EVENT_DESCRIPTION_FIELD = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText"

# Basic info to rest
BASIC_INFO_MAIN_MENU_BTN = "//android.widget.Button[@content-desc='press']"

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
ADD_TICKETS_EVENT_STARTS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[2]"
ADD_TICKETS_EVENT_ENDS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[3]"
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

# Promo code:
PROMO_CODE = "//android.widget.Button[@content-desc='Promo code']"
ADD_A_CODE = "//android.widget.Button[@content-desc='Add a code']"
CODE_NAME = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]"
NUMBER_OF_USES = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]"
PROMO_PRICE_BTN = "//android.widget.Button[@content-desc='Price']"
PROMO_PRICE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[3]"
PROMO_PERCENTAGE_BTN = "//android.widget.Button[@content-desc='Percentage']"
PROMO_PERCENTAGE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[3]"
ADD_PROMO = "//android.widget.Button[@content-desc='Add']"
PROMO_BACK = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button"
PROMO_REFRESH = "//android.widget.Button[@content-desc='Refresh']"
PROMO_ADDED_NAME = "//android.widget.HorizontalScrollView//android.view.View[@index='3']"
PROMO_CODE_TYPE = "//android.widget.HorizontalScrollView//android.view.View[@index='4']" #percantage
PROMO_CODE_DISCOUNT = "//android.widget.HorizontalScrollView//android.view.View[@index='1']" #65.0
PROMO_CODE_USES = "//android.widget.HorizontalScrollView//android.view.View[@index='5']"
PROMO_CODE_OPTIONS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.HorizontalScrollView/android.widget.Button"
PROMO_CODE_EDIT = "//android.widget.Button[@content-desc='edit']"
PROMO_CODE_DELETE = "//android.widget.Button[@content-desc='delete']"

# Publish
PUBLISH_THE_EVENT = "//android.widget.Button[@content-desc='Publish The event']"
EVENT_PUBLISHED = "//android.view.View[@content-desc='The event is now published']"
MAKE_EVENT_PUBLIC = "//android.widget.Button[@content-desc='Make the event public']"
MAKE_EVENT_PRIVATE = "//android.widget.Button[@content-desc='Make The event private']"

# Dashboard
DASHBOARD_MENU_CHOICE = "//android.view.View[@content-desc='dashboard']"
DASHBOARD_REFRESH = "//android.widget.Button[@content-desc='refresh']"
ADD_ATTENDEE = "//android.widget.Button[@content-desc='add attendee']"
DASHBOARD_DELETE = "//android.widget.Button[@content-desc='Delete event']"

#Add attendee
ATTENDEE_FIRST_NAME = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[1]"
ATTENDEE_LAST_NAME = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[2]"
ATTENDEE_PHONE_NUMBER = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[3]"
ATTENDEE_GENDER = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[4]"
ATTENDEE_EMAIL = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[5]"
ATTENDEE_PRICE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[6]"
ATTENDEE_QUANTITY = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[6]"
ADD_ATTENDEE_END_BTN = "//android.widget.Button[@content-desc='add']"
TICKETS_SOLD = "//android.widget.HorizontalScrollView//android.view.View//android.view.View[@index='1']" 
TICKET_ADDED_TABLE = "(//android.view.View[@content-desc='Regular'])[1]"
