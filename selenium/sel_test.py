# Code By JIYA ULL HAQ
# Started 7th may 2020 - Running
# --------------------------------------------------------------------
# Importing required packages
from datetime import datetime
import schedule
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from selenium import webdriver
import time
from tqdm import tqdm
from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains

# --------------------------------------------------------------------
# --------------------------------------------------------------------

N = input("\nNumber of sessions: ")  # Number of sessions you want to have...

Atn = input("Attendance? [y/n]: ")  # [(y/n) (yes/no) (Yes/No)] for attendance...
if Atn == 'y':
    atn = input("session? [1/2/both]: ")
else:
    pass
# --------------------------------------------------------
# --------------------------------------------------------

# Credentials:

mail_address = '19a91a05c2@aec.edu.in'
password = 'Aditya@1234'

mail_address1 = '19a91a0577@aec.edu.in'
password1 = 'Aditya@123'


def T1():
    # -
    print('Staring 1st session on:', )
    # -

    # 1. Reading data from SpreadSheet

    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name('Client_secret.json', scope)

    client = gspread.authorize(creds)
    sheet2 = client.open("Bot").sheet1

    data = sheet2.get_all_records()  # Total data count

    x = len(data) + 1
    cell = sheet2.cell(x, 3).value
    # Latest classroom
    print("* Your Link:", cell)

    # ----------------------------------------------------
    # ----------------------------------------------------
    # Chrome settings:

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-notification')
    chrome_options.add_extension('/Users/jiya/PythonProjects/selenium/Meet Attendance.crx')
    # chrome_options.add_argument("--mute-audio")
    # chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-infobars')
    prefs = {"profile.default_content_setting_values.notifications": 2,
             "profile.default_content_setting_values.media_stream_mic": 1,
             "profile.default_content_setting_values.media_stream_camera": 1,
             "profile.default_content_setting_values.geolocation": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome('/Users/jiya/PythonProjects/selenium/chromedriver', options=chrome_options)
    # -------------------------------------------------------
    # -------------------------------------------------------

    # User 1 Login
    url = 'https://accounts.google.com/signin/v2/identifier?hl=en&continue=http%3A%2F%2Fwww.google.co.in%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
    driver.get(url)
    driver.implicitly_wait(20)
    driver.find_element_by_xpath("//*[@id='identifierId']").send_keys(mail_address)
    driver.implicitly_wait(20)
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()
    driver.implicitly_wait(20)
    driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(password)
    driver.implicitly_wait(20)
    driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()
    driver.implicitly_wait(20)

    # --------------------------------------------------

    # 5. Session 1 ; User 1 join class
    driver.get(cell)

    # Commands:
    driver.implicitly_wait(20)
    driver.implicitly_wait(20)

    time.sleep(2)
    driver.refresh()
    time.sleep(3)

    elem = driver.find_element_by_xpath("/html/body")
    elem.send_keys(Keys.COMMAND + "d")
    elem.send_keys(Keys.COMMAND + 'e')
    time.sleep(2)

    # Enter Classroom
    driver.find_element_by_xpath(
        "//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span").click()
    time.sleep(10)

    # --------------------------------------------------------------------
    # User 2 Login
    driver.execute_script("window.open('https://www.google.com','new window')")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)

    driver.get(
        'https://accounts.google.com/signin/v2/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Fpli%3D1&csig=AF-SEnZz_1MDdyQr3PfT%3A1589523925&flowName=GlifWebSignIn&flowEntry=AddSession')

    driver.implicitly_wait(20)
    driver.find_element_by_xpath("//*[@id='identifierId']").send_keys(mail_address1)
    driver.implicitly_wait(20)
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()
    driver.implicitly_wait(20)
    driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(password1)
    driver.implicitly_wait(20)
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()
    driver.implicitly_wait(20)
    # -------------------------------------------------------
    # session 1 ; User 2 join class.
    driver.get(cell)

    # Commands:
    driver.implicitly_wait(20)

    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[1]/div[2]/div/div/a").click()
    driver.implicitly_wait(20)

    driver.find_element_by_xpath(
        "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[2]/div/div[1]/div/div[2]/div[1]").click()
    driver.implicitly_wait(20)
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(20)
    time.sleep(2)
    elem = driver.find_element_by_xpath("/html/body")
    elem.send_keys(Keys.COMMAND + 'd')
    elem.send_keys(Keys.COMMAND + 'e')
    time.sleep(2)

    # Enter Classroom
    driver.find_element_by_xpath(
        "//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span").click()

    #  driver.find_element_by_xpath("//*[@id='ow4']/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span/div/div/span[1]/svg").click()

    #   driver.switch_to.window(driver.window_handles[1])

    # driver.implicitly_wait(20)
    # driver.execute_script("window.open()")

    # driver.implicitly_wait(20)
    # driver.switch_to.window(driver.window_handles[2])
    # driver.find_element_by_xpath("/html/body").send_keys(Keys.COMMAND+'t')
    time.sleep(2)

    if atn == '1' or atn == 'both':
        driver.implicitly_wait(20)
        # Takes attendance
        driver.find_element_by_xpath(
            "/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span").click()
        time.sleep(5)
        # Directs to spreadsheet
        driver.find_element_by_xpath("//*[@id='attendanceicon']").click()
        driver.implicitly_wait(20)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[2])
        driver.find_element_by_xpath("//*[@id='docs-folder']").click()
        driver.implicitly_wait(20)
        time.sleep(4)
        driver.implicitly_wait(20)
        step_1 = ActionChains(driver)
        step_1.send_keys(Keys.DOWN, Keys.DOWN, Keys.RETURN)
        step_1.perform()

        driver.implicitly_wait(20)
        time.sleep(4)
        driver.implicitly_wait(20)

        step_2 = ActionChains(driver)
        step_2.send_keys(Keys.TAB, Keys.TAB, Keys.RETURN)
        step_2.perform()

        driver.implicitly_wait(20)
        time.sleep(4)
        driver.implicitly_wait(20)

        step_3 = ActionChains(driver)
        step_3.send_keys(Keys.TAB, Keys.TAB, Keys.RETURN)
        step_3.perform()

        atn_url = driver.current_url

        driver.implicitly_wait(20)

        _Close_Tab_ = ActionChains(driver)
        _Close_Tab_.send_keys(Keys.COMMAND + 'w')
        _Close_Tab_.perform()

        driver.switch_to.window(driver.window_handles[1])

        esc = ActionChains(driver)
        esc.send_keys(Keys.ESCAPE)
        esc.perform()

        driver.implicitly_wait(20)
        # Takes attendance
        driver.find_element_by_xpath(
            "/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span").click()
        time.sleep(5)


        sheet = client.open_by_url(atn_url).sheet1


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

    else:
        pass
    # -----------------------------------------------------------
    # -----------------------------------------------------------
    # Exit Class (session 1)
    time.sleep(int(4500))
    driver.quit()

    for i in tqdm(range(10)):
        time.sleep(0.1)

    now = datetime.now()
    dt_string0 = now.strftime("%I:%M %p")
    print("Exited 1st Session successfully on:", dt_string0)

    if N == str(1):
        exit()
    print("----------------------------------------------")


# -----------------------------------------------------------
# -----------------------------------------------------------


# ---------
T1()
