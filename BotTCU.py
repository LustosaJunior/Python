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

 
driver.get('https://pesquisa.apps.tcu.gov.br/#/pesquisa/integrada')
sleep(1.5)
campoPesquisar = driver.find_element_by_css_selector('#mat-input-0')
sleep(1.5)
campoPesquisar.send_keys(str(TARGET[1]))
sleep(1.5)
btnSearch = driver.find_element_by_xpath('//*[@id="conteudo-principal"]/app-agregador-pesquisa/div/section[1]/div[1]/app-cabecalho-campo-pesquisa/div/div/div/div/div/form/div/mat-form-field/div/div[1]/div[2]/button[2]').click()
sleep(25)
nadaEncontrado = driver.find_elements_by_css_selector('#conteudo-principal > app-pesquisa > app-pesquisa-todas-bases > div > div.container-grid > div > div > div.mdc-layout-grid__cell.mdc-layout-grid__cell--span-9-desktop.mdc-layout-grid__cell--span-8-tablet.mdc-layout-grid__cell--span-4-phone > app-resultado > div > div:nth-child(1) > div > div > div > h3')
if "Nenhum resultado encontrado na base" in nadaEncontrado:
    tela1 = driver.find_element_by_xpath('/html/body')
    
    tela1.screenshot(f'C:/Users/danie/Desktop/Junior/Robos/imagensTCU/imagensPesquisaIntegrada/PrintTCU{str(TARGET[1])}.png')

    with open(f"C:/Users/danie/Desktop/Junior/Robos/imagensTCU/imagensPesquisaIntegrada/PrintTCU{str(TARGET[1])}.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        #insert = f'INSERT INTO docsPython (NU_RS, dt_hr, DOC) values(1, GETDATE(),"{encoded_string}")'
        #insert = 'INSERT INTO docsPython (NU_RS, dt_hr) values(1, GETDATE())'
        cursor.execute(f'''UPDATE docsPython SET DOC_TCU = Convert(varbinary(max),%(encoded)s)  where NU_RS = {nu_rs}''', dict(encoded = encoded_string))
        conn.commit()
else:
    tela2 = driver.find_element_by_xpath('/html/body')
    
    tela2.screenshot(f'C:/Users/danie/Desktop/Junior/Robos/imagensTCU/imagensPesquisaIntegrada/PrintTCU{str(TARGET[1])}.png')

    with open(f"C:/Users/danie/Desktop/Junior/Robos/imagensTCU/imagensPesquisaIntegrada/PrintTCU{str(TARGET[1])}.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        #insert = f'INSERT INTO docsPython (NU_RS, dt_hr, DOC) values(1, GETDATE(),"{encoded_string}")'
        #insert = 'INSERT INTO docsPython (NU_RS, dt_hr) values(1, GETDATE())'
        cursor.execute(f'''UPDATE docsPython SET DOC_TCU = Convert(varbinary(max),%(encoded)s)  where NU_RS = {nu_rs}''', dict(encoded = encoded_string))
        conn.commit()


print("Carregando proximo processo")

sleep(10)

#Segunda Busca
driver.get('https://contasirregulares.tcu.gov.br/ordsext/f?p=105:1:::NO:2,3,4,5,6::')
sleep(1.5)
campoNome = driver.find_element_by_xpath('//*[@id="P1_NOME"]')
sleep(1.5)
campoNome.send_keys(str(TARGET[1]))
sleep(1.5)
campoCPF = driver.find_element_by_xpath('//*[@id="P1_CPF"]')
sleep(1.5)
campoCPF.send_keys("")
sleep(1.5)
campoCNPJ = driver.find_element_by_xpath('//*[@id="P1_CNPJ"]')
sleep(1.5)
campoCNPJ.send_keys("")
sleep(1.5)
clickBuscar = driver.find_element_by_xpath('//*[@id="B4545328987462459343"]').click()
sleep(0.5)

tela = driver.find_element_by_xpath('/html/body')

tela.screenshot(f'C:/Users/danie/Desktop/Junior/Robos/imagensTCU/imagensListaContasIrregulares/PrintTCU2{str(TARGET[1])}.png')

#with open(f"C:/Users/danie/Desktop/Junior/Robos/imagensTCU/imagensListaContasIrregulares/PrintTCU2{str(TARGET[1])}.png", "rb") as image_file:
   # encoded_string = base64.b64encode(image_file.read())
#insert = f'INSERT INTO docsPython (NU_RS, dt_hr, DOC) values(1, GETDATE(),"{encoded_string}")'
#insert = 'INSERT INTO docsPython (NU_RS, dt_hr) values(1, GETDATE())'
##conn.commit()


sleep(1)

driver.quit() 