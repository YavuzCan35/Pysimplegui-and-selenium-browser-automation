from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import selenium.common.exceptions
from selenium.webdriver.common.by import By
import json
import datetime
import sys
import os
from win10toast import ToastNotifier
toaster = ToastNotifier ( )
sys.setrecursionlimit(999999999)
PATH = "T:\indirilenler T\chromedriver.exe"
opt: Options = Options ( )
headless=str(input('Pencere görünmez olsun mu ?(Görünmez tavsiye edilir. Müdahalede bulunmak, programı yanıltabilir ve hata yaratabilir. Küçük harfle cevapla; evet/hayır    :'))


def headsiz():
    opt.add_argument ( '--headless' )
headless=str(headless)
if headless!='evet':
    print(headless)
else:
    print(headless)
    headsiz()


opt.add_argument ( 'log-level=1' )
opt.add_argument('--disable-gpu')
opt.add_argument("--window-size=1920,1080")
def açılış():
    global driver
    try:
        driver = webdriver.Chrome ( executable_path=PATH, options=opt )
    except selenium.common.exceptions.SessionNotCreatedException:
        print('Chromedriver needs to be updated.\n Go to : https://chromedriver.chromium.org/downloads \n Win32 edition \n Put it in the folder of this program.')
        quit()
    driver.get('https://shop.museumssonntag.berlin/#/tickets/time?museum_id=10&group=timeSlot&date=2021-12-05')
    driver.implicitly_wait(5)
    time.sleep(3)
açılış()
i=0
while True:
    try:
        driver.get('https://shop.museumssonntag.berlin/#/tickets/time?museum_id=10&group=timeSlot&date=2021-12-05')
        driver.implicitly_wait(10)
        a=driver.find_element_by_css_selector('.alert > .ng-scope')
        print('________________')
        try:
            print(a.text)
        except AttributeError:
            print(a)
        print(datetime.datetime.now())
        if a.text=='Bitte wählen Sie den 7. November, um verfügbare Zeitfenster anzuzeigen.' or a.text=='Zeitfenster für den nächsten Termin werden eine Woche vorher freigeschaltet.':
            print('Still waiting for it...')
            time.sleep(2)
            i=i+1
            print(i)
            time.sleep(300)
            pass
        else:
            while True:
                toaster.show_toast ( f"****MÜZE RANDEVUSU AÇILDI****",
                                     f"Müzeden randevu al berlin !", None, 15, False )
            print('Send Notification')
    except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.WebDriverException :
        print('Error!')
        driver.quit()
        açılış()
        pass


