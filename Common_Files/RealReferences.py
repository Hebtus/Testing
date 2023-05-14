# ---------------- This file is used to easily map references for elements to the ones already used ----------------#

# ---------------- Attendee's View ----------------#



# ----------- Hebtus Creator's View --------------#
# Log in and to creator's view
NAV_BAR_DROP_DOWN = "navbar-dropdown-container" # ID
DROPDOWN_LOGIN_CHOICE = "/html/body/div/div/div[1]/div/nav/div[2]/ul/li[1]/a"
EMAIL_FIELD = "email"
PASSWORD_FIELD = "password"
LOG_IN_BUTTON = "form--button-login"
MANAGE_MY_EVENTS = "/html/body/div/div/div[1]/div/nav/div[1]/a" # FULL XPATH

# Event list
GO_TO_EVENTLIST = "/html/body/div/div/div/span"
EVENT_HEADER = "event-list-header" # ID
FILTER_EVENTS_BUTTON = "choices-menu" # ID
FILTER_ALL_EVENTS = "choices-menu-all" # ID
FILTER_UPCOMING_EVENTS = "choices-menu-upcoming" # ID
FILTER_PAST_EVENTS = "choices-menu-past" # ID
EVENTS_LIST = "/html/body/div/div/div[2]/div[3]/table/tr" # XPATH
EVENT_PART1 = "/html/body/div/div/div[2]/div[3]/table/tr[" # partial XPATH
EVENT_TITLE_PART2 = "]/td[1]/div/div[2]/div/p[1]" # Rest of XPATH
EVENT_DATE_PART2 = "]/td[1]/div/div[2]/div/p[3]" # Rest of XPATH
EVENT_DRAFT_ONSALE_ENDED_STATUS_PART2 = "]/td[3]/div/div[2]" # Rest of XPATH
EVENT_SOLD_PART2 = "]/td[2]" # Rest of XPATH
EVENTS_SEARCH_BAR = "search-bar" # ID
DOWNLOAD_CSV = "/html/body/div/div/div[2]/div[4]"

# Basic info
CREATE_EVENT_BUTTON = "create-event-button" #ID
EVENT_TITLE_FIELD = "input-field-Event Title"  # ID
TAGS_FIELD = ":r0:"  # ID
EVENT_TYPE_DROPDOWN_FIELD = "select-type" # ID
EVENT_CATEGORY_DROPDOWN_FIELD = "select-category" # ID
EVENT_SUBCATEGORY_DROPDOWN_FIELD = "select-subcategory" # ID
EVENT_START_DATE_FIELD = ":r2:" # ID
EVENT_END_DATE_FIELD = ":r6:" # ID
EVENT_START_TIME_FIELD = ":r4:" # ID
EVENT_END_TIME_FIELD = ":r8:" # ID
TYPE_OPTIONS = "/html/body/div/div/div/div[2]/div[1]/div[2]/div[2]/select[1]/option"
CATEGORY_OPTIONS = "/html/body/div/div/div/div[2]/div[1]/div[2]/div[2]/select[2]/option"
SUBCATEGORY_OPTIONS = "/html/body/div/div/div/div[2]/div[1]/div[2]/div[2]/select[3]/option"
ADD_TAG = "add-tag-btn"
ALL_TAGS = "/html/body/div/div/div/div[2]/div[1]/div[2]/div[5]/div"
TAG_ERROR_MSG = "/html/body/div/div/div/div[2]/div[1]/div[2]/div[4]/div/div[2]/p[1]" # XPATH
LOCATION_TITLE = "/html/body/div/div/div/div[2]/div[2]/div[2]/h1"
VENUE_BUTTON = "/html/body/div/div/div/div[2]/div[2]/div[2]/div/div[1]" # XPATH
ONLINE_BUTTON = "/html/body/div/div/div/div[2]/div[2]/div[2]/div/div[2]" # XPATH
TO_BE_ANNOUNCED_BUTTON = "/html/body/div/div/div/div[2]/div[2]/div[2]/div/div[3]" # XPATH
SINGLE_EVENT = "single-event-panel"
DATE_AND_TIME_TITLE = "/html/body/div/div/div/div[2]/div[3]/div[2]/h1" # XPATH 
EVENT_START_DATE_MSG = "/html/body/div/div/div/div[2]/div[3]/div[2]/div[2]/div[1]/p[2]"
EVENT_END_DATE_MSG = "/html/body/div/div/div/div[2]/div[3]/div[2]/div[3]/div[1]/p[2]"
EVENT_TIME_ZONE_DROPDOWN = "/html/body/div/div/div/div[2]/div[3]/div[2]/div[4]/select"
EVENT_LANGUAGES_DROPDOWN = "select-event-page-lang"
SAVE_AND_CONTINUE_BUTTON = "/html/body/div/div/div/div[2]/div[4]/div/div"
SAVE_AND_CONTINUE_BUTTON2 = "/html/body/div/div/div[3]/div/div"
UPLOADED_IMAGE_HEBTUS = "/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/img"
UPLOAD_IMAGE_HEBTUS = "/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/input"
REMOVE_IMAGE = "/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]"
REMOVED_IMAGE = "/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div"
EVENT_DESCRIPTION = "/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/h1"
DESCRIPTON_TEXTAREA = "/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div/textarea"
#SAVE_AND_CONTINUE_BUTTON = "save-button"
# Tickets
TICKETS_TITLE = "/html/body/div/div/div[3]/div[1]/div[1]/h1"
ADD_TICKET_OUTER = "add-ticket--card"
TICKET_TITLE_TAB = "offcanvasRightLabel"
CLOSE_TICKET_FORM = "form-close"
PAID_TICKET = "paid-panel-changer"
FREE_TICKET = "free-panel-changer"
DONATION = "donation-panel-changer"
NAME_TICKET_FIELD = "input-field-Name"
QUANTITY_TICKET_FIELD = "input-field-Available Quantity"
PRICE_TICKET_FIELD = "input-field-Price"
SELECT_TICKET_TYPE = "select-ticket-type-dropdown"
START_DATE_TICKET = "start-date"
END_DATE_TICKET = "end-date"
START_TIME_TICKET = "start-time"
END_TIME_TICKET = "end-time"
ADD_TICKET_INNER = "form-save-ticket-btn"
CANCEL_BUTTON = "form-cancel-btn"
TICKETS_ERROR_MSG = "form-message-text"
FIRST_TICKET_CARD = "ticket--card-0"
FIRST_EVENT_TITLE = "ticket-card-title-0"
FIRST_EVENT_START_DATE = "ticket-card-start-date-0"
FIRST_EVENT_TICKET_COUNT = "ticket-card-capacity-0"
FIRST_EVENT_TICKET_EDIT = "ticket-card-edit-0"

# Publish
EVENT_NAME_1 = "/html/body/div/div/div[3]/div[1]/div/div/div["
EVENT_NAME_2 = "]/div/div/h4"
NEXT_PAGE_BUTTON = "next-page-button"
HEBTUS_LOGO = "/html/body/div/div/div[1]/div/nav/a/h3"
MY_EVENT_NAME = "NightGazing"
GO_TO_PUBLISH = "/html/body/div/div/div[2]/div[1]/div[2]/ul/li[4]/a/div/span"
PUBLISH_TITLE = "/html/body/div/div/div[2]/div[2]/h1"
PUBLISH_EVENT_TITLE = "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/span[1]"
PUBLISH_DATE_TITLE = "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/span[2]"
PUBLIC_RADIOBUTTON = "Public"
PRIVATE_RADIOBUTTON = "Private"
PUBLISH_NOW_RADIOBUTTON = "0"
SCHEDULE_LATER_RADIOBUTTON ="1"
SAVE_AND_CONTINUE_PUBLISH = "/html/body/div/div/div[3]/div/div"
ACCOUNT_NAVBAR = "/html/body/div/div/div[1]/nav/div[2]/a/div"
MANAGE_MY_EVENTS_PUBLISH = "/html/body/div/div/div[1]/nav/div[2]/ul/li[1]/a"
FIRST_EVENT_EVENTLIST = "/html/body/div/div/div[2]/div[3]/table/tr[2]/td[1]/div/div[2]/div/p[1]"
EDIT_FIRST_EVENTLIST = "/html/body/div/div/div[2]/div[3]/table/tr[2]/td[4]/div[1]"
ACCOUNT_NAVBAR2 = "navbar-dropdown-container"
MANAGE_MY_EVENTS2 = "/html/body/div/div/div[1]/div/nav/div[2]/ul/li[1]/a"
#Dashboard
DASHBOARD_TITLE = "/html/body/div/div/div[3]/div/div[1]/div[1]/h1"
EVENT_TO_TEST_EDIT = "64513144c879ea38608901d7"
EVENT_TO_TEST = "event-64513144c879ea38608901d7-growth"
GO_TO_DASHBOARD = "/html/body/div/div/div[2]/div[1]/div[2]/ul/li[5]/a/div/span"
DASHBOARD_URL = "copy-icon"
TEST_EVENT_PROFIT_EVENTLIST = "/html/body/div/div/div[2]/div[3]/table/tr[11]/td[2]"
DASHBOARD_RECENT_ORDER = "report-table-header-Recent orders"
RECENT_ORDERS_ROWS = "/html/body/div/div/div[3]/div/div[3]/div[2]/div/div[2]/table/tbody/tr"
RECENT_ORDERS_QUANTITY = "/html/body/div/div/div[3]/div/div[3]/div[2]/div/div[2]/table/tbody/tr/td[3]"
RECENT_ORDERS_PRICE = "/html/body/div/div/div[3]/div/div[3]/div[2]/div/div[2]/table/tbody/tr/td[4]"
ALL_TICKETS_HYPERLINK = "report-table-footer-tickets"
PUBLISH_HYPERLINK = "publish-event-task"
ATTENDEE_SUMMARY_REPORT_HYPERLINK = "/html/body/div/div/div[3]/div/div[3]/div[3]/div/div[2]/div/div[2]/div/a"
PAGE_VIEW_REPORTS_HYPERLINK = "/html/body/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[3]/p/a"
PUBLISH_YOUR_EVENT_IDENTIFIER = "/html/body/div/div/div[2]/div[2]/div[2]/p"

# ---------------- Creator's View ----------------#
# Navigation to creator's view
AD_EXIT_BUTTON = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/div/div/div/div/div/div[2]/span/button"
AD_WANT_TO_LEAVE_BUTTON = "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/main/div/div/div/div/div/div[1]/div/div/main/div/div/div/div[2]/button[1]"
SESSION_EXPIRED_TITLE = "//*[@id='content']/table/tbody/tr/td[2]/h2" # XPATH
# Basic Info Web Page
EVENT_TITLE_ERROR_MSG = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/aside" # XPATH
SCROLL_AMOUNT_FOR_TAG = "window.scrollBy(0,500)"
TAGS_INSERTED_FIELD = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div" # XPATH
TAGS_DELETE_BASE = "//*[@id='cross-chunky_svg__eds-icon--cross-chunky_svg']" # XPATH
VENUE_LOCATION_TITLE = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[2]/div[2]/div[1]/h1" # XPATH
VENUE_LOCATION_BUTTON_FIELD = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[1]/div/div[1]/label" #XPATH
VENUE_LOCATION_FIELD = "event-locationautocomplete-location" # ID
VENUE_ERROR_MSG = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/aside"
VENUE_OPTION_ONE_BUTTON = "//*[@id='ChIJXc3RyidBWBQREAMVl-pZIfE']/div[1]/button/div/div/div" #XPATH
VENUE_ADDRESS1_FIELD = "//*[@id='event-locationaddress1']" # XPATH
VENUE_ADDRESS2_FIELD = "//*[@id='event-locationaddress2']" # XPATH
VENUE_ADDRESS1_ERROR_MSG = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/fieldset/div[2]/div/div[2]/div/aside" # XPATH
VENUE_POSTAL_CODE_FIELD = "event-locationpostal" # ID
VENUE_POSTAL_CODE_ERROR_MSG = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/fieldset/div[6]/div/div[2]/div/aside" # XPATH
VENUE_CITY_FIELD = "event-locationcity" # ID
VENUE_STATE_FIELD = "event-locationregion" # ID
VENUE_COUNTRY_FIELD = "event-locationcountry" # ID
VENUE_SEARCH_LOCATION_BUTTON = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div/form/div[2]/div[2]/div[2]/div/div/div[2]/div/div[3]/button" # XPATH
ONLINE_EVENT_BUTTON_FIELD = "/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/label" # XPATH
VENUE_TO_BE_ANNOUNCED_BUTTON = "/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div/div/div[3]/label" # XPATH
ADD_MORE_TITLE = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div/form/div[4]/div/div/div[2]/h2" # XPATH
START_TIME_CHECKBOX = "//*[@id='check-chunky_svg__eds-icon--check-chunky_svg']" # XPATH
#SAVE_AND_CONTINUE_BUTTON = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/button[2]" # XPATH


# Basic Info Page 2
UPLOAD_IMAGE_BUTTON = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div/form/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/button/span" # XPATH
EVENT_SUMMARY_TITLE = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div/form/div[2]/div[2]/h1" # XPATH
EVENT_SUMMARY_FIELD = "event-design-summary"
EVENT_DESCRIPTION_FIELD = "/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div/form/div[3]/div[2]/div/div/div[1]/div/div[1]/div/div/section/main/div" # XPATH
EVENT_DESCRIPTION_TRASH = "trash-chunky_svg__eds-icon--trash-chunky_base" # ID
DESCRIPTION_BOLD_BUTTON = "/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div/form/div[3]/div[2]/div/div/div[1]/div/div[1]/div/div/section/header/div[2]/div[2]/span[1]/button/i/svg" # XPATH
DESCRIPTION_ITALLIC_BUTTON = "italic-chunky_svg__eds-icon--italic-chunky_svg" # ID

# Navigation to Event List Page from Basic Info Page
NAVIGATE_TO_EVENTS = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[1]/button/div/div" # XPATH

# Event List Page
EVENT_SEARCH_BAR = "//*[@id='search-filter-form']" # XPATH
EVENTS_LIST_PAST_OR_DRAFT = "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/section/div/div[2]/div[3]/div[2]/ul/li"
EVENT_DATE_ONE = "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/section/div/div[2]/div[3]/div[2]/ul/li/div/div/div[1]/a/div/div/div[1]/div/div/div[2]/div[1]/p[3]"
EVENT_PRICE_PART1 = "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/section/div/div[2]/div[4]/div[2]/ul/li[" # Partial XPATH
EVENT_PRICE_PART2 = "]/div/div/div[1]/a/div/div/div[1]/div/div/div[2]/div[2]/div[1]/p" # Rest of XPATH
EVENT_PRIVATE_OR_PUBLIC_PART1 = "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/section/div/div[2]/div[4]/div[2]/ul/li[" # Partial XPATH
EVENT_PRIVATE_OR_PUBLIC_PART2 = "]/div/div/div[1]/a/div/div/div[1]/div/div/div[2]/div[2]/div[3]/span" # Rest of XPATH
EVENT_GROSS_PART1 = "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/section/div/div[2]/div[4]/div[2]/ul/li[" # Partial XPATH
EVENT_GROSS_PART2 = "]/div/div/div[1]/a/div/div/div[2]/div/div/div/div[2]/p" # Rest of XPATH
FILTER_EVENTS_BUTTON_GENERAL = "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/section/div/div[2]/div[2]/div/div[2]/div/div/div/a/div/div/span/span[1]" # XPATH
FILTER_DRAFTS_EVENTS = "//*[@id='draft']/div/button/div/div/div" # XPATH
THREE_DOTS_EVENT_BUTTON = "vertical-dots-chunky_svg__eds-icon--vertical-dots-chunky_svg" # ID
EVENT_PROMOTE_ON_EVENTBRITE_CHOICE = "//*[@id='eb-promote']/div/a/div/div/div" # XPATH
EVENT_VIEW_CHOICE = "//*[@id='view']/div/a/div/div/div" # XPATH
EVENT_EDIT_CHOICE = "//*[@id='edit']/div/a/div/div/div" # XPATH
EVENT_COPY_URL_CHOICE = "//*[@id='copyUrl']/div[1]/span/div/div/div/div/div" # XPATH
EVENT_COPY_EVENT_CHOICE = "//*[@id='copyEvent']/div/a/div/div/div" # XPATH
EVENT_DELETE_CHOICE = "//*[@id='delete']/div/button/div/div/div" # XPATH

# Deleting draft event
EVENT_DELETED_TITLE = "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/section/div/div[2]/div[3]/div[2]/ul/li[1]/div/div/div[1]/a/div/div/div[1]/div/div/div[2]/p"
EVENT_DELETED_TITLE_ONE = "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/section/div/div[2]/div[3]/div[2]/ul/li/div/div/div[1]/a/div/div/div[1]/div/div/div[2]/p"
CSV_EXPORT_BUTTON = "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/section/div/div[2]/footer/a" # XPATH

# Event Promote on Eventbrite page
EVENT_PROMOTE_ON_EVENTBRITE_TITLE = "//*[@id='eba-create-wrapper']/div[1]/div/div[1]/div[1]" # XPATH
# Event View
EVENT_VIEW_TITLE = "//*[@id='root']/div/div/div[2]/div/div/div/div[1]/div/main/div/div[2]/div/div[2]/div[1]/h1" # XPATH
# Edit Event 
EVENT_EDIT_TITLE = "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div/form/div[1]/div[2]/div[1]/h1" # XPATH
# Copy Event
EVENT_COPY_TITLE = "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/section/div/div/form/div/div[2]/div[1]/h1" # XPATH
# Dashboard
EVENT_DASHBOARD_TITLE = "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/section/div/div/div[1]/div[1]/h1" # XPATH
EVENT_DASHBOARD_LINK = "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/section/div/div/div[1]/div[5]/div[2]/div/div[1]/div[2]" # XPATH