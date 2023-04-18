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
WELCOME_OK_BUTTON = (
    "//android.view.View//android.widget.Button[@content-desc='OK']"  #! New
)
# ---------------------------------------------------------------------------------------------------
SIGN_UP_EMAIL_TEXTBOX = "//android.widget.ScrollView//android.widget.EditText[@class='android.widget.EditText'][position() = 1]"  #! New
FIRT_NAME_TEXTBOX = "//android.widget.ScrollView//android.widget.EditText[@class='android.widget.EditText'][position() = 2]"  #! New
LAST_NAME_TEXTBOX = "//android.widget.ScrollView//android.widget.EditText[@class='android.widget.EditText'][position() = 3]"  #! New
SIGN_UP_PASSWORD_TEXTBOX = "//android.widget.ScrollView//android.widget.EditText[@class='android.widget.EditText'][position() = 4]"  #! New
CONFIRM_PASSWORD_TEXTBOX = "//android.widget.ScrollView//android.widget.EditText[@class='android.widget.EditText'][position() = 5]"  #! New
CREATE_ACOUNT_BUTON = "//android.widget.ScrollView//android.widget.Button[@content-desc='Sign Up']"  #! New
# ---------------------------------------------------------------------------------------------------
# signup invalid tests
EMPTY_EMAIL_ALERT = '//android.widget.EditText//android.view.View[@content-desc="Email field can\'t be empty."]'  #! New
INVALID_EMAIL_ALERT = "//android.widget.EditText//android.view.View[@content-desc='Please Enter a valid email']"  #! New
FIRST_NAME_REQUIRED_ALERT = '//android.widget.EditText//android.view.View[@content-desc="First Name can\'t be empty"]'  #! New
LAST_NAME_REQUIRED_ALERT = '//android.widget.EditText//android.view.View[@content-desc="Last Name can\'t be empty"]'  #! New
PASSWORD_REQUIRED_ALERT = '//android.widget.EditText//android.view.View[@content-desc="Password field can\'t be empty"]'  #! New
INVALID_PASSWORD_ALERT = '//android.widget.EditText//android.view.View[@content-desc="Password must be at least 8 characters"]'  #! New
PASSWORD_MISMATCH_ALERT = '//android.widget.EditText//android.view.View[@content-desc="Password doesn\'t match"]'  #! New
# ---------------------------------------------------------------------------------------------------

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

#! ________________________________HERE_______________________________________
# Events Page
EVENT = "//android.view.View[@index='0']//android.widget.ImageView[@index='0'and @class='android.widget.ImageView'][1]"  #! New
IMAGE = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1'and @class='android.widget.ScrollView']"  #! New
TICKETS_INFO = "//android.widget.ScrollView[@index='1']//android.view.View[@index='2']"
GET_TICKET_BUTTON = "//android.view.View[@index='2']//android.widget.Button[@index='2' and @content-desc='Reserve a spot' and @class='android.widget.Button']"  #! New
PLUS_BUTTON = "//android.view.View[@index='2']//android.widget.Button[@index='0' and @class='android.widget.Button']"  #! New
MINUS_BUTTON = "//android.view.View[@index='2']//android.widget.Button[@index='1' and @class='android.widget.Button']"  #! New
START_DATE = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1']//android.view.View[@index='2'and @class='android.view.View']"  #! New
EVENT_TITLE = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1']//android.view.View[@index='3'and @class='android.view.View']"  #! New
DATE_TIME = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1']//android.view.View[@index='6'and @class='android.view.View']"  #! New
LOCATION = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1']//android.view.View[@index='8'and @class='android.view.View']"  #! New


EVENTS_DETAILS_1 = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1']//android.view.View[@index='4'and @class='android.view.View']"  #! New
EVENTS_DETAILS_2 = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1']//android.view.View[@index='5'and @class='android.view.View']"  #! New
# ---------------------------------------------------------------------------------------------------

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

SEE_MORE_BUTTON = "//android.view.View[@index='0']//android.widget.ScrollView[@index='1']//android.widget.Button[@content-desc='See more' and @index='2'and @class='android.widget.Button']"  #! New
HEBTUS_BUTTON = "//android.view.View[@index='0']//android.widget.Button[@content-desc='Hebtus' and @index='0'and @class='android.widget.Button']"  #! New
SEE_MORE_PAGE = "//android.widget.ScrollView[@index='1']//android.view.View[@index='0']//android.view.View[@index='0']//android.view.View[@index='0']//android.widget.ImageView[@index='0'and @class='android.widget.ImageView']"  #! New

LOCATION_PICKER = "location-text"

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

ALL_TAB = "//android.view.View[@index='0']//android.widget.Button[@content-desc='All' and @index='0'and @class='android.widget.Button']"  #! New
MUSIC_TAB = "//android.view.View[@index='1']//android.widget.Button[@content-desc='Music' and @index='0'and @class='android.widget.Button']"  #! New
FOOD_DRINK_TAB = "//android.view.View[@index='2']//android.widget.Button[@content-desc='Food & Drink' and @index='0'and @class='android.widget.Button']"  #! New
CHARITY_CAUSES_TAB = "//android.view.View[@index='3']//android.widget.Button[@content-desc='Charity & Causes' and @index='0'and @class='android.widget.Button']"  #! New
# ----------------------------------------------------------------

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
# Basic Info Web Page
EVENT_TITLE_FIELD = "event-basicInfo-title"  # ID
TAGS_FIELD = "tagging-form-field"  # ID
