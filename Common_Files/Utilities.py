import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def find_my_element(Driver, type, val):
    try:
        if type == "ID":
            item = WebDriverWait(Driver, 20).until(
                EC.presence_of_element_located((By.ID, val))
            )
        elif type == "XPATH":
            item = WebDriverWait(Driver, 20).until(
                EC.presence_of_element_located((By.XPATH, val))
            )
        elif type == "LINK_TEXT":
            item = WebDriverWait(Driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, val))
            )
        else:
            return None
    except:
        # print("Element not found.")
        return None
    return item


def check_not_found(driver, element, message):
    # assert element != None, message
    if element == None:
        print(message)
        # driver.close()
        # exit()


def clear_textbox(element):
    element.send_keys(Keys.CONTROL, "a")
    element.send_keys(Keys.BACKSPACE)
