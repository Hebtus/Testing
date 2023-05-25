import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import csv
import openpyxl

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
        elif type == "CLASS":
            item = WebDriverWait(Driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, val))
            )
        else:
            return None
    except:
        # print("Element not found.")
        return None
    return item


def check_not_found(driver, element, message):
    if element == None:
        print(message)
        assert element != None, message
        # driver.close()
        # exit()


def clear_textbox(element):
    element.send_keys(Keys.CONTROL, "a")
    element.send_keys(Keys.BACKSPACE)

def find_my_elements(Driver, type, val):
    try:
        if type == "XPATH":
            items = WebDriverWait(Driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, val))
            )
        elif type == "CSS_SELECTOR":
            items = WebDriverWait(Driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, val))
            )
    except:
        print("Element not found.")
    return items

def my_clear(element):
    element.send_keys(Keys.CONTROL, "a")
    element.send_keys(Keys.BACKSPACE)

# csv_to_excel.py
def csv_to_excel(csv_file, excel_file):
    csv_data = []
    with open(csv_file) as file_obj:
        reader = csv.reader(file_obj)
        for row in reader:
            csv_data.append(row)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in csv_data:
        sheet.append(row)
    workbook.save(excel_file)