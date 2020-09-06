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

feed = client.
print(feed)