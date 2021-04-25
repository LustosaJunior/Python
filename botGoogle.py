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
import selenium_util


#Primeira Busca
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.minimize_window()
sleep(1)

nu_rs = sys.argv[1]
print(nu_rs)

conn = pymssql.connect(server='999.99.999.999', user='sa', password='!user@', database='banco')
cursor = conn.cursor()
cursor.execute(f"SELECT * from DADOS WHERE NU_RS = {nu_rs}")
row = cursor.fetchall()

TARGET = (row[0])
PALAVRASCHAVE = (row[0])

for x in row:
  print(x)

driver.get('https://www.google.com.br/')
sleep(1.5)

inputPesquisa = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')

inputPesquisa.send_keys(str(TARGET[1]) + ' ' + str(PALAVRASCHAVE[2]))

btnPesquisa = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[3]/center/input[1]').click()
sleep(2.5)
google = driver.find_element_by_xpath('/html/body')
google.screenshot(f'C:/Users/danie/Desktop/Junior/Robos/imagensGoogle/PrintGoogle{str(TARGET[1])}.png')

with open(f"C:/Users/danie/Desktop/Junior/Robos/imagensGoogle/PrintGoogle{str(TARGET[1])}.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
#insert = f'INSERT INTO docsPython (NU_RS, dt_hr, DOC_GOOGLE) values({nu_rs}, GETDATE(),"{encoded_string}")'
#insert = f'INSERT INTO docsPython (NU_RS, dt_hr) values({nu_rs}, GETDATE())'
cursor.execute(f'''UPDATE docsPython SET DOC_GOOGLE = Convert(varbinary(max),%(encoded)s)  where NU_RS = {nu_rs}''', dict(encoded = encoded_string))
conn.commit()
sleep(2.5)
driver.close()