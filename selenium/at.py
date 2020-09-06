import schedule
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from pprint import pprint
from selenium import webdriver
import time
from tqdm import tqdm
from selenium.webdriver.common.keys import Keys

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('Client_secret.json', scope)
client = gspread.authorize(creds)

#sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1P6LyQeSYhxzD_J2lHrEVwDjP6l-zzomfmvxX9I1mxw8/edit#gid=1075061864").sheet1
url = "https://docs.google.com/spreadsheets/d/1IYK3B0qgJP_IM-XY23CpQTXjj2GYrjKFwQeLYGxAQIM/edit#gid=508842787"
sheet = client.open_by_url(url).sheet1

#data = sheet.get_all_records()  # Total data count


# ------------------------------------------------
# My Class Library
def lib():
    # 66
    try:
        cell = sheet.find('566 Amulya')
        pass
    except gspread.exceptions.CellNotFound:
        print('566 Absent')

    # 67
    try:
        cell = sheet.find('567 KRANTHI BASA')
        pass
    except gspread.exceptions.CellNotFound:
        print("567 Absent")

        # 68
    try:
        cell = sheet.find('568- SATISH BATHINA')
        pass
    except gspread.exceptions.CellNotFound:
        print("568 Absent")

    # 69
    try:
        cell = sheet.find('569 Bhargavi')
        pass
    except gspread.exceptions.CellNotFound:
        print("569 Absent")

    # 70
    try:
        cell = sheet.find('570- Harsha Sri Sameera')
        pass
    except gspread.exceptions.CellNotFound:
        print("570 Absent")

    # 71
    try:
        cell = sheet.find('571_ Pallavi')
        pass
    except gspread.exceptions.CellNotFound:
        print("571 Absent")
    # 72
    try:
        cell = sheet.find('572 CHAPPIDI NAVYAMANI')
        pass
    except gspread.exceptions.CellNotFound:
        print("572 Absent")

    # 73
    try:
        cell = sheet.find('573 __ Subrahmanyam')
        pass
    except gspread.exceptions.CellNotFound:
        print("573 Absent")
    # 74
    try:
        cell = sheet.find('574_vyshnavi')
        pass
    except gspread.exceptions.CellNotFound:
        print("574 Absent")
    # 75
    try:
        cell = sheet.find('575 CHITTI Govinda raju')
        pass
    except gspread.exceptions.CellNotFound:
        print("575 Absent")
    # 76
    try:
        cell = sheet.find('576__ MADHULIKA')
        pass
    except gspread.exceptions.CellNotFound:
        print("576 Absent")
    # 77
    try:
        cell = sheet.find('577 Chandana')
        pass
    except gspread.exceptions.CellNotFound:
        print("577 Absent")
    # 78
    try:
        cell = sheet.find('578____ Meghana Reddy')
        pass
    except gspread.exceptions.CellNotFound:
        print("578 Absent")
    # 79
    try:
        cell = sheet.find('579_ Naveen')
        pass
    except gspread.exceptions.CellNotFound:
        print("579 Absent")
    # 80
    try:
        cell = sheet.find('580_SAI REDDY DWARAMPUDI')
        pass
    except gspread.exceptions.CellNotFound:
        print("580 Absent")
    # 81
    try:
        cell = sheet.find('581_ Sanghavi')
        pass
    except gspread.exceptions.CellNotFound:
        print("581 Absent")
    # 82
    try:
        cell = sheet.find('582 - Durga sai prasad')
        pass
    except gspread.exceptions.CellNotFound:
        print("582 Absent")
    # 83
    try:
        cell = sheet.find('583 GEDDAM KOUSHIK')
        pass
    except gspread.exceptions.CellNotFound:
        print("583 Absent")
    # 84
    try:
        cell = sheet.find('584 Murali Krishna')
        pass
    except gspread.exceptions.CellNotFound:
        print("584 Absent")
    # 85
    try:
        cell = sheet.find('585_ Tarakesham')
        pass
    except gspread.exceptions.CellNotFound:
        print("585 Absent")
    # 86
    try:
        cell = sheet.find('577 Chandan')
        pass
    except gspread.exceptions.CellNotFound:
        print("586 Absent")
    # 87
    try:
        cell = sheet.find('587_ Durgesh')
        pass
    except gspread.exceptions.CellNotFound:
        print("587 Absent")
    # 88
    try:
        cell = sheet.find('588- KADAMATI ARUNA SRI')
        pass
    except gspread.exceptions.CellNotFound:
        print("588 Absent")
    # 89
    try:
        cell = sheet.find('589__varateja K')
        pass
    except gspread.exceptions.CellNotFound:
        print("589 Absent")
    # 90
    try:
        cell = sheet.find('590 Ramesh')
        pass
    except gspread.exceptions.CellNotFound:
        print("590 Absent")
    # 91
    try:
        cell = sheet.find('591__somesh kare')
        pass
    except gspread.exceptions.CellNotFound:
        print("591 Absent")
    # 92
    try:
        cell = sheet.find('592 __prem')
        pass
    except gspread.exceptions.CellNotFound:
        print("592 Absent")
    # 93
    try:
        cell = sheet.find('93_ABHI RAM')
        pass
    except gspread.exceptions.CellNotFound:
        print("593 Absent")
    # 94
    try:
        cell = sheet.find('594__Sanjay Karthik Koppula')
        pass
    except gspread.exceptions.CellNotFound:
        print("594 Absent")
    # 95
    try:
        cell = sheet.find('595_uday kumar')
        pass
    except gspread.exceptions.CellNotFound:
        print("595 Absent")
    # 96
    try:
        cell = sheet.find('596_RAGHURAM REDDY')
        pass
    except gspread.exceptions.CellNotFound:
        print("596 Absent")
    # 97
    try:
        cell = sheet.find('597_KOVVURI VENKATA RAMA DURGAPRASAD REDDY')
        pass
    except gspread.exceptions.CellNotFound:
        print("597 Absent")

    # 98
    try:
        cell = sheet.find('598 Thanush')
        pass
    except gspread.exceptions.CellNotFound:
        print("598 Absent")
    # 99
    try:
        cell = sheet.find('599_ Aeliya')
        pass
    except gspread.exceptions.CellNotFound:
        print("599 Absent")
    # A0
    try:
        cell = sheet.find('5A0 Shabana')
        pass
    except gspread.exceptions.CellNotFound:
        print("5A0 Absent")
    # A1
    try:
        cell = sheet.find('5A1_LOKESH VARMA M')
        pass
    except gspread.exceptions.CellNotFound:
        print("5A1 Absent")
    # A2
    try:
        cell = sheet.find('5A2 Anudeep')
        pass
    except gspread.exceptions.CellNotFound:
        print("5A2 Absent")
    # A3
    try:
        cell = sheet.find('5A3- DEVAKI')
        pass
    except gspread.exceptions.CellNotFound:
        print("5A3 Absent")
    # A4
    try:
        cell = sheet.find('5A4_ ISHWARYA')
        pass
    except gspread.exceptions.CellNotFound:
        print("5A4 Absent")
    # A5
    try:
        cell = sheet.find('5A5_ Sruthieswar')
        pass
    except gspread.exceptions.CellNotFound:
        print("5A5 Absent")

    # A6
    try:
        cell = sheet.find('5A6_VENKATA REDDY')
        pass
    except gspread.exceptions.CellNotFound:
        print("5A6 Absent")
    # A7
    try:
        cell = sheet.find('5A7- shanmukh reddy')
        pass
    except gspread.exceptions.CellNotFound:
        print("5A7 Absent")
    # A8
    try:
        cell = sheet.find('577 Chandan')
        pass
    except gspread.exceptions.CellNotFound:
        print("5A8 Absent")
    # A9
    try:
        cell = sheet.find('5A9_Girijesh')
        pass
    except gspread.exceptions.CellNotFound:
        print("5A9 Absent")
    # B0
    try:
        cell = sheet.find('5B0_suresh reddy')
        pass
    except gspread.exceptions.CellNotFound:
        print("5B0 Absent")
    # B1
    try:
        cell = sheet.find('577 Chandan')
        pass
    except gspread.exceptions.CellNotFound:
        print("5B1 Absent")
    # B2
    try:
        cell = sheet.find('5B2 MAHALAKSHMI')
        pass
    except gspread.exceptions.CellNotFound:
        print("5B2 Absent")
    # B3
    try:
        cell = sheet.find('5B3_RAJ PRAKASH')
        pass
    except gspread.exceptions.CellNotFound:
        print("5B3 Absent")
    # B4
    try:
        cell = sheet.find('5B4_jཛཛvศས')
        pass
    except gspread.exceptions.CellNotFound:
        print("5B4 Absent")
    # B5
    try:
        cell = sheet.find('5B5_Hemanth_Ayyappa_ Reddy')
        pass
    except gspread.exceptions.CellNotFound:
        print("5B5 Absent")
    # B6
    try:
        cell = sheet.find('5B6-SABYASACHI BANERJEE')
        pass
    except gspread.exceptions.CellNotFound:
        print("5B6 Absent")
    # B7
    try:
        cell = sheet.find('577 Chandan')
        pass
    except gspread.exceptions.CellNotFound:
        print("5B7 Absent")
    # B8
    try:
        cell = sheet.find('5b8 TEJASWI')
        pass
    except gspread.exceptions.CellNotFound:
        print("5B8 Absent")
    # B9
    try:
        cell = sheet.find('5B9 SENAPATHI VEERA VENKATA SATYANARAYANA')
        pass
    except gspread.exceptions.CellNotFound:
        print("5B9 Absent")
    # C0
    try:
        cell = sheet.find('5C0 - - - Sandeep')
        pass
    except gspread.exceptions.CellNotFound:
        print("5C0 Absent")
    # C1
    try:
        cell = sheet.find('5C1 SHAIK AMREEN')
        pass
    except gspread.exceptions.CellNotFound:
        print("5C1 Absent")
    # C2
    try:
        cell = sheet.find('5C2 Jiya')
        pass
    except gspread.exceptions.CellNotFound:
        print("5C2 Absent")
    # C3
    try:
        cell = sheet.find('5C3_ Sravya')
        pass
    except gspread.exceptions.CellNotFound:
        print("5C3 Absent")
    # C4
    try:
        cell = sheet.find('577 Chandan')
        pass
    except gspread.exceptions.CellNotFound:
        print("5C4 Absent")
    # C5
    try:
        cell = sheet.find('5c5 manju')
        pass
    except gspread.exceptions.CellNotFound:
        print("5C5 Absent")
    # C6
    try:
        cell = sheet.find('5C6 Chandrika')
        pass
    except gspread.exceptions.CellNotFound:
        print("5C6 Absent")
    # C7
    try:
        cell = sheet.find('5C7_Jhansi Manga Devi Uppu')
        pass
    except gspread.exceptions.CellNotFound:
        print("5C7 Absent")
    # C8
    try:
        cell = sheet.find('5C8- SURYA')
        pass
    except gspread.exceptions.CellNotFound:
        print("5C8 Absent")
    # C9
    try:
        cell = sheet.find('5C9 Vandana')
        pass
    except gspread.exceptions.CellNotFound:
        print("5C9 Absent")

lib()

# ------------------------
# Last step_deleting the spreadsheet
if __name__ == "__lib__":
    # stuff only to run when not called via 'import' here
    lib()
