from datetime import date, datetime
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.phantomjs
import lxml.html    
import requests   
import clipboard
import os
from os import getenv
import pyautogui
import keyboard
import sys
import random
import tempfile
import zipfile
import traceback
from pathlib import Path
from io import BytesIO
from zipfile import ZipFile
import pymssql
import pyperclip
import json
import re
import tkinter.messagebox
import ctypes
import win32gui
import win32ui
import lxml.html as lhtml
from win32api import GetSystemMetrics
import pywinauto
import urllib
from ftplib import FTP  
import fileinput
import base64

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.minimize_window()
sleep(1)

nu_rs = sys.argv[1]
print(nu_rs)

conn = pymssql.connect(server='999.99.999.999', user='sa', password='!user@', database='banco')
cursor = conn.cursor()
cursor.execute(f"SELECT * from RS_MAZARS_FIS_2 WHERE NU_RS = {nu_rs}")
row = cursor.fetchall()

TARGET = (row[0])
PALAVRASCHAVE = (row[0])

for x in row:
  print(x)


driver.get('https://www.google.com/');
search_box = driver.find_element_by_name('q')
search_box.send_keys('linkedin')
search_box.submit()
sleep(1) 
inputEnter = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div[1]/a/h3/span').click()
sleep(8)
inputPessoa = driver.find_element_by_xpath('/html/body/main/section[1]/div[2]/ul/li[2]/a').click()
sleep(6)
inputFirstName = driver.find_element_by_xpath('/html/body/div/header/nav/section[1]/section[1]/form/section[1]/input')
nome = str(TARGET[1])
x = nome.split(" ")
print(x)
inputFirstName.send_keys(str(x[0]))
sleep(4)
inputLastName = driver.find_element_by_xpath('/html/body/div/header/nav/section[1]/section[1]/form/section[2]/input')
sleep(4)
inputLastName.send_keys(str(x[1]))
inputLastName.submit()
sleep(10)

tela1 = driver.find_element_by_xpath('/html/body')
    
tela1.screenshot(f'C:/Users/danie/Desktop/Junior/Robos/ImagensLinkedIn/ImagensPesquisaIntegrada/PrintLinkedIn{str(TARGET[1])}.png')

with open(f"C:/Users/danie/Desktop/Junior/Robos/ImagensLinkedIn/ImagensPesquisaIntegrada/PrintLinkedIn{str(TARGET[1])}.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    #insert = f'INSERT INTO docsPython (NU_RS, dt_hr, DOC) values(1, GETDATE(),"{encoded_string}")'
    #insert = 'INSERT INTO docsPython (NU_RS, dt_hr) values(1, GETDATE())'
    cursor.execute(f'''UPDATE docsPython SET DOC_LINKEDIN = Convert(varbinary(max),%(encoded)s)  where NU_RS = {nu_rs}''', dict(encoded = encoded_string))
    conn.commit()

driver.quit()
