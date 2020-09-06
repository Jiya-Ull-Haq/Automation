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
import at
# --------------------------------------------------------------------
# --------------------------------------------------------------------

N = input("\nNumber of sessions: ")  # Number of sessions you want to have...
Atn = input("Attendance? [y/n]: ")  # [(y/n) (yes/no) (Yes/No)] for attendance...
if Atn == 'y':
    atn = input("session? [1/2/both]: ")
else:pass


t1 = input('\n* Session 1 Entry Time (Format = 00:00): ')  # Entry time for 1st session
print("----------------------------------------------")
print("Time in seconds: \n")
print("3hrs = 10800 seconds")
print("2hr = 7200 seconds")
print("1hr 45 mins = 6300 seconds")
print("1hr 30 mins = 5400 seconds")
print("1hr 15 mins = 4500 seconds")
print("1hr = 3600 seconds")
print("45 mins = 2700 seconds")
print("30 mins =  1800 seconds \n15 mins = 900 seconds\n")
e1 = input('* Session 1 Exit Time (Format in Seconds): ')  # Timer for the EXIT of the 1st session
print("----------------------------------------------\n")

# --------------------------------------------------------

t2 = input('* Session 2 Time (0 for Nill): ')  # Entry time for 2nd session
if t2 == '0':
    t2 = '00:00'
e2 = input('* Session 2 Exit Time (Format in Seconds): ')  # Timer for the EXIT of the 2nd session

print("\n----------------------------------------------")

print("Your Timer has started...")
# --------------------------------------------------------
# --------------------------------------------------------

# --------------------------------------------------------
# --------------------------------------------------------

# Credentials:

mail_address = '19a91a05c2@aec.edu.in'
password = 'Aditya@1234'

mail_address1 = '19a91a0577@aec.edu.in'
password1 = 'Aditya@123'


# mail_address =
# password =

# mail_address1 =
# password1 =
# -------------------------------------------------------
# -------------------------------------------------------

def T1():
    # -
    print('Staring 1st session on:', t1)
    # -

    # 1. Reading data from SpreadSheet

    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name('Client_secret.json', scope)

    client = gspread.authorize(creds)
    sheet = client.open("Bot").sheet1

    data = sheet.get_all_records()  # Total data count

    x = len(data) + 1
    cell = sheet.cell(x, 3).value
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
    # -----------------------------------------------------------
    # -----------------------------------------------------------
    # Exit Class (session 1)

    time.sleep(int(e1))
    driver.quit()

    for i in tqdm(range(10)):
        time.sleep(0.1)

    now = datetime.now()
    dt_string0 = now.strftime("%I:%M %p")
    print("Exited 1st Session successfully on:",dt_string0)

    if N == str(1):
        exit()
    print("----------------------------------------------")
    print("Timer for 2nd session has started...")

    # -----------------------------------------------------------
    # -----------------------------------------------------------


def T2():
    # -

    print('Staring 2nd session on:', t2)
    # -

    # Session 2
    # 1. Reading data from SpreadSheet

    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name('Client_secret.json', scope)

    client = gspread.authorize(creds)
    sheet = client.open("Bot").sheet1

    data = sheet.get_all_records()  # Total data count

    x = len(data) + 1
    cell = sheet.cell(x, 3).value
    # Latest classroom
    print("* Your Link:", cell)

    # ----------------------------------------------------
    # ----------------------------------------------------
    # Chrome settings:

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-notification')
    # chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-infobars')
    prefs = {"profile.default_content_setting_values.notifications": 2,
             "profile.default_content_setting_values.media_stream_mic": 1,
             "profile.default_content_setting_values.media_stream_camera": 1,
             "profile.default_content_setting_values.geolocation": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome('/Users/jiya/PythonProjects/selenium/chromedriver', options=chrome_options)

    # -------------------------------------------------------
    # -------------------------------------------------------

    # 1. Session 2 ; User 1 login
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

    # 2. Session 2 ; User 1 join

    driver.get(cell)

    # Commands:
    driver.implicitly_wait(20)
    # driver.find_element_by_xpath("//*[@id='yDmH0d']/div[2]/div/div[2]/div[3]/div/span/span").click()
    driver.implicitly_wait(20)

    # button = driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/div[3]/div")
    # button.click()

    time.sleep(2)
    driver.refresh()
    time.sleep(3)

    elem = driver.find_element_by_xpath("/html/body")
    elem.send_keys(Keys.COMMAND + "d")
    elem.send_keys(Keys.COMMAND + 'e')
    time.sleep(2)
    # driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/div[3]/div").click()

    # Enter Classroom
    driver.find_element_by_xpath(
        "//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span").click()
    time.sleep(10)

    # --------------------------------------------------------------------
    # 3. Session 2 ; User 2 Login
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
    driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()
    driver.implicitly_wait(20)
    # -------------------------------------------------------
    # 4. Session 2 ; User 2 Join
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

    # ------------------------------------------
    # ------------------------------------------

    # Exit Class
    time.sleep(int(e2))
    driver.quit()



    for i in tqdm(range(10)):
        time.sleep(0.1)

    now1 = datetime.now()
    dt_string1 = now1.strftime("%I:%M %p")
    print("Exited 2nd Session Successfully on:", dt_string1)

    print("----------------------------------------------")
    if N == str(2):
        exit()
    # ------------------------------------------
    # ------------------------------------------


# -----------------------------------------------------
# -----------------------------------------------------
# LOOPS
def t2_1():
    schedule.every().day.at(t2).do(T2)
    while True:
        schedule.run_pending()
        time.sleep(1)


schedule.every().day.at(t1).do(T1)
while True:
    t2_1()

# -----------------------------------------------------
# -----------------------------------------------------
