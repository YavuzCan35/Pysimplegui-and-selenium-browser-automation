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
from discord import Webhook, RequestsWebhookAdapter
webhook = Webhook.from_url (
    "https://discord.com/api/webhooks/324234asdfasd...................",
    adapter=RequestsWebhookAdapter ( ) )
toaster = ToastNotifier ( )
sys.setrecursionlimit(999999999)
PATH = "T:\indirilenler T\chromedriver.exe"
opt: Options = Options ( )
#window of the browser visible or not:
headless=str(input('Pencere görünmez olsun mu ?(Görünmez tavsiye edilir. Müdahalede bulunmak, programı yanıltabilir ve hata yaratabilir. Küçük harfle cevapla; evet/hayır    :'))


def headsiz():
    opt.add_argument ( '--headless' )
headless=str(headless)
if headless!='evet':
    print(headless)
else:
    print(headless)
    headsiz()
links=["https://www.notebooksbilliger.de/handys+smartphones/apple+iphone+13+pro+max/apple+iphone+13+pro+max+256gb+graphit+737241","https://www.notebooksbilliger.de/handys+smartphones/apple+iphone+13+pro+max/apple+iphone+13+pro+max+256gb+silber+737238","https://www.notebooksbilliger.de/handys+smartphones/apple+iphone+13+pro+max/apple+iphone+13+pro+max+256gb+sierrablau+737240","https://www.notebooksbilliger.de/handys+smartphones/apple+iphone+13+pro+max/apple+iphone+13+pro+max+256gb+gold+737242"]

opt.add_argument ( 'log-level=1' )
opt.add_argument('--disable-gpu')
opt.add_argument("--window-size=1920,1080")
opt.add_argument('--no-sandbox')
opt.add_experimental_option('useAutomationExtension', False)
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("start-maximized")
opt.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36')
def açılış():
    global driver
    try:
        driver = webdriver.Chrome ( executable_path=PATH, options=opt )
    except selenium.common.exceptions.SessionNotCreatedException:
        print('Chromedriver needs to be updated.\n Go to : https://chromedriver.chromium.org/downloads \n Win32 edition \n Put it in the folder of this program.')
        quit()
    time.sleep(3)
açılış()
for i in range(1,len(links)):
    driver.switch_to.new_window ( links[i] )
tursayacı=0
while True:
    for i,v in enumerate(links):
        sekmeler = driver.window_handles
        driver.switch_to.window(sekmeler[i])
        driver.get ( v )
        driver.implicitly_wait ( 10 )
        print(sekmeler)
        if i==-1: #saturn içindi
            try:
                a = driver.find_element(by=By.CSS_SELECTOR, value='.StyledConsentLayerCTAs-g0yhcr-11 > :nth-child(1)' )
                a.click ( )
            except selenium.common.exceptions.NoSuchElementException:
                pass
            driver.refresh()
            driver.implicitly_wait(5)
            a = driver.find_element(by=By.CSS_SELECTOR, value=':nth-child(3) > :nth-child(1) > .StyledAvailabilityHeadingWrapper-sc-901vi5-2 > .BaseTypo-sc-1jga2g7-0' )
            try:
                print ( a.text )
            except AttributeError:
                print ("a=",a )
            if a.text == 'Leider keine Lieferung möglich':
                print ( 'Still waiting for it...' )
                time.sleep ( 2 )
                tursayacı = tursayacı + 1
                print ( tursayacı )
                time.sleep ( 3 )
            else:
                while True:
                    webhook.send (
                        f"Iphone geldi! saturn" )
                    toaster.show_toast ( f"****İphone geldi lo****",
                                         f"saturn.de", None, 15, False )
                print ( 'İphone geldi bildirim gönderildi.' )
        elif i>=0:
            try:
                a = driver.find_element_by_xpath ( "//button[@id='uc-btn-deny-banner']" )
                a.click ( )
            except selenium.common.exceptions.NoSuchElementException:
                print('could not find it')
                pass
            driver.implicitly_wait(5)
            try:
                a = driver.find_element(by=By.XPATH, value="//button[@type='submit'][contains(.,'Jetzt vorbestellen')]" )
            except selenium.common.exceptions.NoSuchElementException:
                try:
                    a=driver.find_element(by=By.XPATH,value="//button[@type='submit'][contains(.,'In den Warenkorb')]")
                except selenium.common.exceptions.NoSuchElementException:
                    toaster.show_toast ( f"Kod hatası",
                                         f"Nbb sitesindeki iki elementte bulunamıyor.", None, 15, False )
            driver.delete_all_cookies ( )
            try:
                print ( a.text )
            except AttributeError:
                print ("a=",a )
            if a.text=="  Jetzt vorbestellen":
                print('Still waiting for it...')
                time.sleep ( 2 )
                tursayacı = tursayacı + 1
                print ( tursayacı )
                time.sleep ( 3 )
            else:
                while True:
                    webhook.send (
                        f"Iphone geldi! Notebooksbilliger: {v}" )
                    toaster.show_toast ( f"****İphone geldi lo****",
                                         f"nbb sitesinde", None, 15, False )
                print ( f'İphone geldi. bildirim gönderildi. {v}' )
        print ( datetime.datetime.now ( ) )
        print ( '________________' )
    time.sleep(300)


"""    except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.WebDriverException :
        print('Error!')
        driver.quit()
        açılış()
        pass"""
