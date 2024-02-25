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
from discord import Webhook, RequestsWebhookAdapter
import discord.errors
import sys
import os
import arayüz
sys.setrecursionlimit(999999999)
print('Lütfen giriş yaptıktan sonra "ogame.gameforge.com/game/index.php?page=ingame&component=preferences&mode=reloaded&selectedTab=1", chat kutucuklarını deaktive edin!')

discordlinki0="https://discord.com/api/webhooks/"
PATH = "chromedriver.exe"

profil=str(input('Her yeni kullanıcı ve serverı, kaydetmek ve kullanmak için özgün bir profil adı girin:'))

dirname, filename = os.path.split ( os.path.abspath ( __file__ ) )
pathname = os.path.join ( dirname, f'{profil}.txt' )
arayüz.arayüz(pathname)
x=input('Discord kanalına webhook ile bildirim almak ister misin ? evet ise "evet" yazınız   :')
if x=='evet' or x=='EVET' or x=='Evet':
    y=input('Webhooklinki bu ise 1 yaz:\nhttps://discord.com/api/webhooks/')
    if y=='1':
        discordlinki= 'https://discord.com/api/webhooks/'
    else:
        discordlinki = input (
        'Lütfen, bildirim atılacak DİSCORD webhookunu buraya giriniz! parantez olmadan (https://discord.com/api/webhooks/...)        :' )
else:
    discordlinki ='https://discord.com/api/webhooks/'

webhook=Webhook.from_url (discordlinki,    adapter=RequestsWebhookAdapter ( ) )

veriagı=[0 for i in range(0,99)]
if os.path.exists ( pathname ):
    data = [line.strip ( ) for line in open ( pathname )]
    for iiii in range(len(data)):
        if data[iiii]!=None or data[iiii]!='' or data[iiii]!=' ' or data[iiii]!='    ' or data[iiii]!='\n':
            veriagı[iiii]=data[iiii]
        else:
            veriagı[iiii] = 0
else:
    print('Profil bulunamadı.')
    quit()

selectedserver=veriagı[2]
def verilerupdate():
    global veriagı,arastırmayapcakgezegen,mindeutsartı,ogezegendekiarastırmalabhedefi,araştırmalabhedefi,\
        robotfabrikasıhedefi,tershanehedefi,roketsilosuhedefi,nanithedefi,minbilgisaytek,mincasusluktek,minkalkantek,\
        minlazertek,minenerjitek,minyanmalı,minimpuls,minastro,hafifavcıhedefi,agıravcıhedefi,sondahed,ltransporthedefi,\
        ktransporthedefi,kolonigemhed,recyclerhedefi,roketatar,hafiflazer,agırlazer,iyontopu,gaustopu,plazmatopu,yakalayıcı,gar,\
        miniyon, minhiptek, minhipit, minplazma, minarasagı, mingravitasyon, minsilah, minzırh,solaruyduhedef,paletlihedef,kruvazörhedefi, \
        komutahedefi,fırfırhedefi,bombardımanhedefi,muhriphedefi,ölümyıldızıhedef,azrailhedef,kasifhedef,tershaneüretimiyapmaşartıkristalseivyesi
    if os.path.exists ( pathname ):
        data = [line.strip ( ) for line in open ( pathname )]
    for iiiii in range ( len ( data ) ):
        if data[iiiii] != None and data[iiiii] != '' and data[iiiii] != ' ' and data[iiiii] != '    ' and data[iiiii] != '\n' and data[iiiii] !='0' :
            veriagı[iiiii] = data[iiiii]
        else:
            veriagı[iiiii] = int(0)
    arastırmayapcakgezegen=       int(veriagı[5])-1
    mindeutsartı= int(veriagı[6])
    ogezegendekiarastırmalabhedefi=int(veriagı[7])
    araştırmalabhedefi=  int(veriagı[8])
    robotfabrikasıhedefi=   int(veriagı[9])
    tershanehedefi=           int(veriagı[10])
    roketsilosuhedefi= int(veriagı[11])
    nanithedefi=     int(veriagı[12])
    minbilgisaytek=       int(veriagı[13])
    mincasusluktek=       int(veriagı[14])
    minkalkantek=   int(veriagı[15])
    minlazertek=       int(veriagı[16])
    minenerjitek=    int(veriagı[17])
    minyanmalı=      int(veriagı[18])
    minimpuls=    int(veriagı[19])
    minastro= int(veriagı[20])
    miniyon= int(veriagı[21])
    minhiptek= int(veriagı[22])
    minhipit= int(veriagı[23])
    minplazma= int(veriagı[24])
    minarasagı= int(veriagı[25])
    mingravitasyon= int(veriagı[26])
    minsilah= int(veriagı[27])
    minzırh= int(veriagı[28])
    hafifavcıhedefi=int(veriagı[29])
    agıravcıhedefi=int(veriagı[30])
    sondahed=int(veriagı[31])
    ltransporthedefi=int(veriagı[32])
    ktransporthedefi=int(veriagı[33])
    kolonigemhed=int(veriagı[34])
    recyclerhedefi=int(veriagı[35])
    solaruyduhedef=int(veriagı[36])
    paletlihedef=int(veriagı[37])
    kruvazörhedefi=int(veriagı[38])
    komutahedefi=int(veriagı[39])
    fırfırhedefi=int(veriagı[40])
    bombardımanhedefi=int(veriagı[41])
    muhriphedefi=int(veriagı[42])
    ölümyıldızıhedef=int(veriagı[43])
    azrailhedef=int(veriagı[44])
    kasifhedef=int(veriagı[45])
    tershaneüretimiyapmaşartıkristalseivyesi=int(veriagı[46])
    roketatar=int(veriagı[47])
    hafiflazer=int(veriagı[48])
    agırlazer=int(veriagı[49])
    iyontopu=int(veriagı[50])
    gaustopu=int(veriagı[51])
    plazmatopu=int(veriagı[52])
    yakalayıcı=int(veriagı[53])
    gar=int(veriagı[54])
verilerupdate()


def tershaneüretimitoplu(gezegen,şart, hafifavcıhedefi, agıravcıhedefi, sondahed, ltransporthedefi, ktransporthedefi,
                         kolonigemhed, recyclerhedefi, solaruyduhedef, paletlihedef, kruvazörhedefi, komutahedefi,
                         fırfırhedefi, bombardımanhedefi, muhriphedefi, ölümyıldızıhedef, azrailhedef, kasifhedef):
    if checkshipyardque()=='empty':
        if şart<gezegen.madenlerclass.kristal.currentlevel:
            gezegen.madenlerclass.kristal.gereken()
            if şart<gezegen.madenlerclass.kristal.currentlevel:
                üretgemisavunma ( gezegen.gemiler.sonda, sondahed )
                üretgemisavunma ( gezegen.gemiler.kolonigemisi, kolonigemhed )
                üretgemisavunma ( gezegen.gemiler.ltransporter, ltransporthedefi )
                üretgemisavunma ( gezegen.gemiler.knakliye, ktransporthedefi )
                üretgemisavunma ( gezegen.gemiler.geridönüsüm, recyclerhedefi )
                üretgemisavunmasüreklikontrol ( gezegen.gemiler.solaruydu, solaruyduhedef )
                üretgemisavunma ( gezegen.gemiler.paletli, paletlihedef )
                üretgemisavunma ( gezegen.gemiler.havcı, hafifavcıhedefi )
                üretgemisavunma ( gezegen.gemiler.agıravcı, agıravcıhedefi )
                üretgemisavunma ( gezegen.gemiler.kruvazör, kruvazörhedefi )
                üretgemisavunma ( gezegen.gemiler.komuta, komutahedefi )
                üretgemisavunma ( gezegen.gemiler.fırkateyn, fırfırhedefi )
                üretgemisavunma ( gezegen.gemiler.bombardıman, bombardımanhedefi )
                üretgemisavunma ( gezegen.gemiler.muhrip, muhriphedefi )
                üretgemisavunma ( gezegen.gemiler.ölümyıldızı, ölümyıldızıhedef )
                üretgemisavunma ( gezegen.gemiler.azrail, azrailhedef )
                üretgemisavunma ( gezegen.gemiler.kasif, kasifhedef )
        else:
            pass

def savunmaüretimitoplu(gezegen,şart, roketatar, hafiflazer, agırlazer, iyontopu, gaustopu,
                         plazmatopu, yakalayıcı, gar):
    if checkshipyardque()=='empty':
        if şart<gezegen.madenlerclass.kristal.currentlevel:
            gezegen.madenlerclass.kristal.gereken()
            if şart<gezegen.madenlerclass.kristal.currentlevel:
                üretgemisavunmasüreklikontrol ( gezegen.savunma.yakalayıcıroket, yakalayıcı )
                üretgemisavunma ( gezegen.savunma.gar, gar )
                üretgemisavunmasüreklikontrol ( gezegen.savunma.roketatar, roketatar )
                üretgemisavunmasüreklikontrol ( gezegen.savunma.hlazer, hafiflazer )
                üretgemisavunmasüreklikontrol ( gezegen.savunma.alazer, agırlazer )
                üretgemisavunmasüreklikontrol ( gezegen.savunma.iyontopu, iyontopu )
                üretgemisavunmasüreklikontrol ( gezegen.savunma.gaustopu, gaustopu )
                üretgemisavunmasüreklikontrol ( gezegen.savunma.plazmatopu, plazmatopu )
        else:
            pass

def arastır(gezegen,minbilgisaytek,mincasusluktek,minkalkantek,minlazertek,minenerjitek,minyanmalı,minimpuls,minastro,miniyon,minhiptek,minhipit,minplazma,minarasagı,mingravitasyon,minsilah,minzırh):
    if checkresearchque()=='empty':
        teknikarttırma ( minbilgisaytek, gezegen.researchclass.bilgisayartek )
        teknikarttırma ( mincasusluktek, gezegen.researchclass.casusluktek )
        teknikarttırma ( minkalkantek, gezegen.researchclass.kalkantek )
        teknikarttırma ( minlazertek, gezegen.researchclass.lazertek )
        teknikarttırma ( minenerjitek, gezegen.researchclass.energytek )
        teknikarttırma ( minyanmalı, gezegen.researchclass.yanmalimotor )
        teknikarttırma ( minimpuls, gezegen.researchclass.impulsitici )
        teknikarttırma ( minastro, gezegen.researchclass.astro )
        teknikarttırma ( miniyon, gezegen.researchclass.iyon )
        teknikarttırma ( minhiptek, gezegen.researchclass.hipuztek )
        teknikarttırma ( minhipit, gezegen.researchclass.hipuziticisi )
        teknikarttırma ( minplazma, gezegen.researchclass.plazmatek )
        teknikarttırma ( minarasagı, gezegen.researchclass.arastırmaagı )
        teknikarttırma ( mingravitasyon, gezegen.researchclass.gravitasyon )
        teknikarttırma ( minsilah, gezegen.researchclass.silahtek )
        teknikarttırma ( minzırh, gezegen.researchclass.zırhtek )


headless=str(input('Pencere görünmez olsun mu ?(Görünmez tavsiye edilir. Müdahalede bulunmak, programı yanıltabilir ve hata yaratabilir. Küçük harfle cevapla; evet/hayır    :'))


opt: Options = Options ( )
def headsiz():
    opt.add_argument ( '--headless' )
headless=str(headless)
if headless!='evet':
    print(headless)
else:
    print(headless)
    headsiz()
opt.add_argument ( 'log-level=2' )
opt.add_argument('--disable-gpu')
opt.add_argument("--window-size=1920,1080")
opt.add_argument('--no-sandbox')
opt.add_experimental_option('useAutomationExtension', False)
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
opt.add_experimental_option("prefs", prefs)
def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath )
        return True
    except selenium.common.exceptions.NoSuchElementException:
        return False

def check_displayed_by_css(xpath):
    try:
        if driver.find_element(By.CSS_SELECTOR, xpath ).is_displayed()==True:
            return True
    except selenium.common.exceptions.NoSuchElementException:
        return False
def check_displayed_by_classname(xpath):
    try:
        if driver.find_element(By.CLASS_NAME, xpath ).is_displayed()==True:
            return True
    except selenium.common.exceptions.NoSuchElementException:
        return False

def açılış():
    global driver
    try:
        driver = webdriver.Chrome ( executable_path=PATH, options=opt )
    except selenium.common.exceptions.SessionNotCreatedException:
        print('Chromedriver needs to be updated.\n Go to : https://chromedriver.chromium.org/downloads \n Put it in the folder of this program. win32')
        quit()
    driver.get('https://lobby.ogame.gameforge.com/en_GB/')
    driver.implicitly_wait(5)
    time.sleep(3)
##çerezleri kabulet
def acceptcookies():
    try:
        try:
            driver.find_element(By.CSS_SELECTOR,'.cookiebanner4 > :nth-child(2)').click()
            driver.implicitly_wait(5)
        except selenium.common.exceptions.WebDriverException:
            acceptcookies()
    except selenium.common.exceptions.NoSuchElementException:
        try:
            a=check_displayed_by_css('.cookiebanner4 > :nth-child(2)')
            if a:
                acceptcookies()
            else:
                pass
        except selenium.common.exceptions.NoSuchElementException:
            pass

#login
def login():
    try:
        xpath=driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/ul[1]/li[1]').click()
        driver.implicitly_wait(5)
        #mail
        xpath=driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]').send_keys(veriagı[0])
        driver.implicitly_wait(5)
        #pass
        xpath=driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]').send_keys(veriagı[1])
        driver.implicitly_wait(5)
        print(veriagı[2])
        #submitloginbutton
        xpath=driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/form[1]/p[1]/button[1]' )
        driver.implicitly_wait(5)
        xpath.click()
        driver.implicitly_wait(5)
    except selenium.common.exceptions.NoSuchElementException:
        login()
def removeclassname(xpath):
    #"openX_interstitial"
    q = check_displayed_by_classname ( xpath )
    print(q)
    if q == True:
        element = driver.find_element(By.CLASS_NAME, xpath )
        driver.execute_script ( """
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element )
def enteraserver():
    global veriagı
    #playbutton
    try:
        xpath=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/a/button').click()
        driver.implicitly_wait(5)
    except selenium.common.exceptions.NoSuchElementException:
        xpath = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/a/button' ).click ( )
        driver.implicitly_wait ( 5 )
    #my server list
    time.sleep(1)
    print(check_displayed_by_classname("openX_interstitial"))
    try:
        removeclassname("openX_interstitial")
        removeclassname("openX_interstitial")
        removeclassname("openX_interstitial")
        removeclassname("openX_interstitial")
    except selenium.common.exceptions.ElementClickInterceptedException:
        removeclassname ( "openX_interstitial" )
        removeclassname ( "openX_interstitial" )
        removeclassname ( "openX_interstitial" )
        removeclassname ( "openX_interstitial" )
    try:
        t=driver.find_element(By.CSS_SELECTOR,'#accountlist > .ReactTable' ).find_elements(By.CSS_SELECTOR,'.server-name-cell > div')
    except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.ElementClickInterceptedException :
        enteraserver()
    def allmyservers():
        myservers=[]
        print(t)
        for i in t:
            print(i.text)
            myservers.append(i.text)
        print(myservers)
        return myservers
    def opentheserver(selectedserver):
        try:
            ind=allmyservers().index(selectedserver)
            driver.implicitly_wait(5)
            driver.find_element(By.CSS_SELECTOR,f'#accountlist > .ReactTable > .rt-table > .rt-tbody > :nth-child({ind+1}) > .rt-tr > .action-cell > .btn').click()
            driver.implicitly_wait(5)
        except ValueError:
            time.sleep ( 1 )
            try:
                xpath = driver.find_element(By.XPATH,
                    '/html/body/div[1]/div/div/div/div[2]/section[1]/div[2]/div/div/div[1]/div[2]' )
                new = str ( xpath.text ).split ( )
                print ( new )
                opentheserver(selectedserver)
            except selenium.common.exceptions.NoSuchElementException:
                pass
                opentheserver(selectedserver)
    opentheserver(selectedserver)
    #yenisekmede hesap açıldı, SON SEKMEYE GEÇ
    sekmeler=driver.window_handles
    driver.switch_to.window(sekmeler[-1])
    driver.implicitly_wait(5)
    #driver.minimize_window()
def kapanış():
    try:
        driver.quit ( )
        tamgiriş()
    except selenium.common.exceptions.InvalidSessionIdException:
        pass

#kaynak url alınıyor:
def arrayyap(s):
    s=s.split()
    myservers=[]
    for i in s:
        myservers.append(str(i))
    return myservers
def sourceurl():
    global servercode
    driver.implicitly_wait(5)
    time.sleep(3)
    c=str(driver.current_url)
    servercode=c.split('=')[0]+'='
#genelbakış
def genelbakis():
    genelbakis=servercode+'ingame&component=overview'
    driver.get(genelbakis)
    driver.implicitly_wait(5)
#mesajlar
def mesajlar():
    mesajlar=servercode+'messages'
    driver.get(mesajlar)
    driver.implicitly_wait(5)
#kaynaklar
def kaynaklar():
    kaynaklar=servercode+'ingame&component=supplies'
    driver.get(kaynaklar)
    driver.implicitly_wait(5)
def tesislerurl():
    kaynaklar=servercode+'ingame&component=facilities'
    driver.get(kaynaklar)
    driver.implicitly_wait(5)
def arastırmaurl():
    kaynaklar=servercode+'ingame&component=research'
    driver.get(kaynaklar)
    driver.implicitly_wait(5)
def converttonumber(x):
    if type(x)==str:
        if 'm' in x or 'M' in x:
            if ',' in x:
                x = x.replace ( ',', '.' )
            if 'm' in x:
                x = x.split ( 'm' )[0]
                if ',' in x:
                    x = x.replace ( ',', '.' )
                x = float ( x )
            elif 'M' in x:
                x = x.split ( 'M' )[0]
                if ',' in x:
                    x = x.replace ( ',', '.' )
                x=float(x)
            x = float ( x ) * 1000000
            x = int ( x )
        elif (',' in x ) and (('m' not in x) or ('M' not in x)):
            x=x.replace ( '.', '' )
            x = x.replace ( ',', '.' )
            x=float(x)
            x = int ( x )
        else:
            if ('m' in x) or ('M' in x):
                if 'm' in x:
                    x=x.split('m')[0]
                    if ',' in x:
                        x = x.replace ( ',', '.' )
                elif 'M' in x:
                    x=x.split('M')[0]
                    if ',' in x:
                        x = x.replace ( ',', '.' )
                x=float(x)*1000000
                x = int ( x )
            else:
                x = x.replace ( '.', '' )
        x=int(x)
        return int ( float (x))
    else:
        try:
            return int(float(x.text.replace('.','')))
        except AttributeError:
            return int(float ( int ( str(x).replace ( '.', '' ) ) ))
madenler=['metal','kristal','deut','enerji','darkmatter']
def mevcutmadenler():
    global metalmevcut,kristalmevcut,deutmevcut,enerjimevcut,darkmattermevcut
    try:
        getkaynaklar=driver.find_element(By.ID,'resourcesbarcomponent').text
        kaynaklartemp=arrayyap(getkaynaklar)
        metalmevcut=converttonumber(kaynaklartemp[0])
        madenler[0]=converttonumber(kaynaklartemp[0])
        kristalmevcut=converttonumber(kaynaklartemp[1])
        madenler[1]=converttonumber(kaynaklartemp[1])
        deutmevcut=converttonumber(kaynaklartemp[2])
        madenler[2]=converttonumber(kaynaklartemp[2])
        enerjimevcut=converttonumber(kaynaklartemp[3])
        madenler[3]=converttonumber(kaynaklartemp[3])
        darkmattermevcut=converttonumber(kaynaklartemp[4])
        madenler[4]=converttonumber(kaynaklartemp[4])
        return metalmevcut,kristalmevcut,deutmevcut,enerjimevcut,darkmattermevcut
    except selenium.common.exceptions.NoSuchElementException or TypeError:
        pass

#üretim binaları
def checkconstructionque():
    if driver.current_url ==  servercode+'ingame&component=supplies' or driver.current_url ==  servercode+'ingame&component=overview' or driver.current_url ==  servercode+'ingame&component=facilities':
        pass
    else:
        genelbakis()
    driver.implicitly_wait(5)
    try:
        contructionque = driver.find_element(By.CSS_SELECTOR,
            '#productionboxbuildingcomponent > .content-box-s > .content > .construction' ).text
        if arrayyap(contructionque)[0]=='Keine' or arrayyap(contructionque)[0]=='Bina' or arrayyap(contructionque)[0]=='No' :
            print ( '_____' )
            print('There is no construction')
            print ( '_____' )
            return 'empty'
        else:
            print(contructionque)
            return 'full'
    except selenium.common.exceptions.NoSuchElementException:
        pass
def checkresearchque():
    if driver.current_url ==  servercode+'ingame&component=research' or driver.current_url ==  servercode+'ingame&component=overview':
        pass
    else:
        genelbakis()
    driver.implicitly_wait(5)
    try:
        contructionque = driver.find_element(By.CSS_SELECTOR,
            '#productionboxresearchcomponent > .content-box-s > .content > .construction' ).text
        if arrayyap(contructionque)[0]=='Zurzeit' or arrayyap(contructionque)[0]=='Şuan' or arrayyap(contructionque)[0]=='No' :
            print ( '_____' )
            print('There is no research.')
            print ( '_____' )
            return 'empty'
        else:
            print(contructionque)
            return 'full'
    except selenium.common.exceptions.NoSuchElementException:
        pass

def checkshipyardque():
    if driver.current_url ==  servercode+'ingame&component=shipyard' or driver.current_url ==  servercode+'ingame&component=overview' or driver.current_url ==  servercode+'ingame&component=defenses':
        pass
    else:
        genelbakis()
    driver.implicitly_wait ( 5 )
    try:
        contructionque = driver.find_element(By.CSS_SELECTOR,'#productionboxshipyardcomponent > .content-box-s > .content > .construction' ).text
        if arrayyap ( contructionque )[0] == 'Keine' or arrayyap ( contructionque )[0] == 'Gemi'  or arrayyap ( contructionque )[0] == 'Gemi/Savunma':
            print ( 'There is no ship/defence unit in construction.' )
            return 'empty'
        else:
            print('___________')
            print(contructionque)
            print('___________')
            return 'full'
    except selenium.common.exceptions.NoSuchElementException:
        pass
#kaynakayarları
servercode=''
class depo:
    metalkapasitesi=0
    kristalkapasitesi=0
    deutkapasitesi=0

    def __init__(self):
        print('Depo görevlisi on')
    @classmethod
    def update(cls):
        try:
            if driver.current_url!=servercode + 'resourceSettings' :
                driver.get (servercode + 'resourceSettings'  )
            driver.implicitly_wait ( 5 )
            cls.metalkapasitesi = converttonumber (
                driver.find_element(By.XPATH, '(.//*[@class="mainRS"]//span)[178]' ).text )
            cls.kristalkapasitesi = converttonumber (
                driver.find_element(By.XPATH, '(.//*[@class="mainRS"]//span)[179]' ).text )
            cls.deutkapasitesi = converttonumber (
                driver.find_element(By.XPATH, '(.//*[@id="inhalt"]//span)[180]' ).text )
            driver.get ( servercode + 'ingame&component=supplies' )
            driver.implicitly_wait ( 5 )
        except selenium.common.exceptions.NoSuchElementException:
            pass
class planet:
    def __init__(self):
        self.waittime=0
        self.mevcutmetal=0
        self.mevcutkristal=0
        self.mevcutdeut=0
        self.mevcutsolar=0
        self.mevcutdarkmatter=0
        self.madenlerclass=self.Madenlerclass()
        self.researchclass=self.Researchclass()
        self.tesisler=self.Tesisler()
        self.gemiler=self.Ships()
        self.savunma=self.Defenses()
    class Madenlerclass:
        def __init__(self):
            self.metal=self.Metal()
            self.kristal=self.Kristal()
            self.deut=self.Deut()
            self.solar=self.Solar()
            self.metaldeposu=self.Metaldeposu()
            self.krisdeposu=self.Krisdeposu()
            self.deutdeposu=self.Deutdeposu()
        class Metal:
            def __init__(self):
                self.name   =  'metalMine'
                self.url    =   servercode+'ingame&component=supplies'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    kaynaklar()
            def gereken(self):
                self.checkurl()
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a==True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                        driver.implicitly_wait(5)
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                        a = check_displayed_by_css ( '.level' )
                        if a == True:
                            level=driver.find_element(By.CSS_SELECTOR,'.level').text
                            level=[int(n) for n in level.split() if n.isdigit()]
                            self.currentlevel=level[0]
                        return True
                    except ValueError:
                        print('value error')
                        return False
                except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                    print(f'Error for .technology.{self.name} > .icon')
                    kapanış()
                    return False
            def yükselt(self):
                print('Metal upgrade.')
                try:
                    self.checkurl()
                    if self.gereken()==True:
                        if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                            a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                            if a == True:
                                driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                driver.implicitly_wait(5)
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                    driver.implicitly_wait(5)
                                    return True
                            else:
                                kapanış()
                        else:
                            return False
                    checkconstructionque ( )
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class Kristal:
            def __init__(self):
                self.name   =  'crystalMine'
                self.url    =   servercode+'ingame&component=supplies'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    kaynaklar()
            def gereken(self):
                self.checkurl()
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a==True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                        driver.implicitly_wait(5)
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                        a = check_displayed_by_css ( '.level' )
                        if a == True:
                            level=driver.find_element(By.CSS_SELECTOR,'.level').text
                            level=[int(n) for n in level.split() if n.isdigit()]
                            self.currentlevel=level[0]
                        return True
                    except ValueError:
                        print('value error')
                        return False
                except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                    print(f'Error for .technology.{self.name} > .icon')
                    kapanış()
                    return False
            def yükselt(self):
                try:
                    self.checkurl()
                    if self.gereken()==True:
                        if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                            a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                            if a == True:
                                driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                driver.implicitly_wait(5)
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                    driver.implicitly_wait(5)
                                    return True
                            else:
                                kapanış()
                        else:
                            return False
                    checkconstructionque ( )
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class Deut:
            def __init__(self):
                self.name   =  'deuteriumSynthesizer'
                self.url    =   servercode+'ingame&component=supplies'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    kaynaklar()
            def gereken(self):
                self.checkurl()
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a==True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                        driver.implicitly_wait(5)
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                        a = check_displayed_by_css ( '.level' )
                        if a == True:
                            level=driver.find_element(By.CSS_SELECTOR,'.level').text
                            level=[int(n) for n in level.split() if n.isdigit()]
                            self.currentlevel=level[0]
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                    print(f'Error for .technology.{self.name} > .icon')
                    kapanış()
                    return False
            def yükselt(self):
                try:
                    self.checkurl()
                    if self.gereken()==True:
                        if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                            a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                            if a == True:
                                driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                driver.implicitly_wait(5)
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                    driver.implicitly_wait(5)
                                    return True
                            else:
                                kapanış()
                        else:
                            return False
                    checkconstructionque ( )
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class Solar:
            def __init__(self):
                self.name   =  'solarPlant'
                self.url    =   servercode+'ingame&component=supplies'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    kaynaklar()
            def gereken(self):
                self.checkurl()
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a==True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                        driver.implicitly_wait(5)
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                        a = check_displayed_by_css ( '.level' )
                        if a == True:
                            level=driver.find_element(By.CSS_SELECTOR,'.level').text
                            level=[int(n) for n in level.split() if n.isdigit()]
                            self.currentlevel=level[0]
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                    print(f'Error for .technology.{self.name} > .icon')
                    kapanış()
                    return False
            def yükselt(self):
                try:
                    self.checkurl()
                    if self.gereken()==True:
                        if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                            a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                            if a == True:
                                driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                driver.implicitly_wait(5)
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                    driver.implicitly_wait(5)
                                    return True
                            else:
                                kapanış()
                        else:
                            return False
                    checkconstructionque ( )
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class Metaldeposu:
            def __init__(self):
                self.name   =  'metalStorage'
                self.url    =   servercode+'ingame&component=supplies'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    kaynaklar()
            def gereken(self):
                self.checkurl()
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a==True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                        driver.implicitly_wait(5)
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                        a = check_displayed_by_css ( '.level' )
                        if a == True:
                            level=driver.find_element(By.CSS_SELECTOR,'.level').text
                            level=[int(n) for n in level.split() if n.isdigit()]
                            self.currentlevel=level[0]
                        return True
                    except ValueError:
                        print('value error')
                        return False
                except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                    print(f'Error for .technology.{self.name} > .icon')
                    kapanış()
                    return False
            def yükselt(self):
                try:
                    self.checkurl()
                    if self.gereken()==True:
                        if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                            a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                            if a == True:
                                driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                driver.implicitly_wait(5)
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                    driver.implicitly_wait(5)
                                    return True
                            else:
                                kapanış()
                        else:
                            return False
                    checkconstructionque ( )
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class Krisdeposu:
            def __init__(self):
                self.name   =  'crystalStorage'
                self.url    =   servercode+'ingame&component=supplies'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    kaynaklar()
            def gereken(self):
                self.checkurl()
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a==True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                        driver.implicitly_wait(5)
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                        a = check_displayed_by_css ( '.level' )
                        if a == True:
                            level=driver.find_element(By.CSS_SELECTOR,'.level').text
                            level=[int(n) for n in level.split() if n.isdigit()]
                            self.currentlevel=level[0]
                        return True
                    except ValueError:
                        print('value error')
                        return False
                except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                    print(f'Error for .technology.{self.name} > .icon')
                    kapanış()
                    return False
            def yükselt(self):
                try:
                    self.checkurl()
                    if self.gereken()==True:
                        if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                            a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                            if a == True:
                                driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                driver.implicitly_wait(5)
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                    driver.implicitly_wait(5)
                                    return True
                            else:
                                kapanış()
                        else:
                            return False
                    checkconstructionque ( )
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class Deutdeposu:
            def __init__(self):
                self.name   =  'deuteriumStorage'
                self.url    =   servercode+'ingame&component=supplies'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    kaynaklar()
            def gereken(self):
                self.checkurl()
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a==True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                        driver.implicitly_wait(5)
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                        a = check_displayed_by_css ( '.level' )
                        if a == True:
                            level=driver.find_element(By.CSS_SELECTOR,'.level').text
                            level=[int(n) for n in level.split() if n.isdigit()]
                            self.currentlevel=level[0]
                        return True
                    except ValueError:
                        print('value error')
                        return False
                except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
                    print(f'Error for .technology.{self.name} > .icon')
                    kapanış()
                    return False
            def yükselt(self):
                try:
                    self.checkurl()
                    if self.gereken()==True:
                        if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                            a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                            if a == True:
                                driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                driver.implicitly_wait(5)
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                    driver.implicitly_wait(5)
                                    return True
                            else:
                                kapanış()
                        else:
                            return False
                    checkconstructionque ( )
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
    class Researchclass:
        def __init__(self):
            self.energytek=self.Energytek()
            self.yanmalimotor=self.combustionDriveTechnology()
            self.impulsitici=self.impulseDriveTechnology()
            self.casusluktek=self.espionageTechnology()
            self.bilgisayartek=self.computerTechnology()
            self.astro=self.astrophysicsTechnology()
            self.kalkantek=self.shieldingTechnology()
            self.lazertek=self.laserTechnology()
            self.iyon=self.ionTechnology()
            self.hipuztek=self.hyperspaceTechnology()
            self.hipuziticisi=self.hyperspaceDriveTechnology()
            self.plazmatek=self.plasmaTechnology()
            self.arastırmaagı=self.researchNetworkTechnology()
            self.gravitasyon=self.gravitonTechnology()
            self.silahtek=self.weaponsTechnology()
            self.zırhtek=self.armorTechnology()

        class Energytek:
            def __init__(self):
                self.name   =  'energyTechnology '
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()
            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<1:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.gereken()
                    if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel < 1:
                        planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class laserTechnology:
            def __init__(self):
                self.name   =  'laserTechnology'
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()

            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].researchclass.energytek.currentlevel<2:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.energytek.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.energytek.currentlevel<2:
                        planetlist[arastırmayapcakgezegen].researchclass.energytek.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
            pass
        class ionTechnology :
            def __init__(self):
                self.name   =  'ionTechnology'
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()
            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].researchclass.energytek.currentlevel<4:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.energytek.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.energytek.currentlevel<4:
                        planetlist[arastırmayapcakgezegen].researchclass.energytek.yükselt()
                    else:
                        self.buildable = 1
                if planetlist[arastırmayapcakgezegen].researchclass.lazertek.currentlevel<5:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.lazertek.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.lazertek.currentlevel<5:
                        planetlist[arastırmayapcakgezegen].researchclass.lazertek.yükselt()
                    else:
                        self.buildable = 1
                if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<4:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.gereken()
                    if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<4:
                        planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
            pass
        class hyperspaceTechnology :
            def __init__(self):
                self.name   =  'hyperspaceTechnology'
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()
            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].researchclass.energytek.currentlevel<5:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.energytek.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.energytek.currentlevel<5:
                        planetlist[arastırmayapcakgezegen].researchclass.energytek.yükselt()
                    else:
                        self.buildable = 1
                if planetlist[arastırmayapcakgezegen].researchclass.kalkantek.currentlevel<5:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.kalkantek.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.kalkantek.currentlevel<5:
                        planetlist[arastırmayapcakgezegen].researchclass.kalkantek.yükselt()
                    else:
                        self.buildable = 1
                if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<7:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.gereken()
                    if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<7:
                        planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
            pass
        class plasmaTechnology :
            def __init__(self):
                self.name   =  'plasmaTechnology'
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()
            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].researchclass.energytek.currentlevel<8:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.energytek.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.energytek.currentlevel<8:
                        planetlist[arastırmayapcakgezegen].researchclass.energytek.yükselt()
                    else:
                        self.buildable = 1
                if planetlist[arastırmayapcakgezegen].researchclass.lazertek.currentlevel<10:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.lazertek.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.lazertek.currentlevel<10:
                        planetlist[arastırmayapcakgezegen].researchclass.lazertek.yükselt()
                    else:
                        self.buildable = 1
                if planetlist[arastırmayapcakgezegen].researchclass.iyon.currentlevel<5:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.iyon.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.iyon.currentlevel<5:
                        planetlist[arastırmayapcakgezegen].researchclass.iyon.yükselt()
                    else:
                        self.buildable = 1
                if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<4:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.gereken()
                    if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<4:
                        planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
            pass
        class combustionDriveTechnology  :
            def __init__(self):
                self.name   =  'combustionDriveTechnology '
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()
            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].researchclass.energytek.currentlevel<1:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.energytek.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.energytek.currentlevel<1:
                        planetlist[arastırmayapcakgezegen].researchclass.energytek.yükselt()
                    else:
                        self.buildable = 1
                if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<1:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.gereken()
                    if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<1:
                        planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
            pass
        class impulseDriveTechnology  :
            def __init__(self):
                self.name   =  'impulseDriveTechnology '
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()
            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].researchclass.energytek.currentlevel<1:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.energytek.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.energytek.currentlevel<1:
                        planetlist[arastırmayapcakgezegen].researchclass.energytek.yükselt()
                    else:
                        self.buildable = 1
                if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<2:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.gereken()
                    if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<2:
                        planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
            pass
        class hyperspaceDriveTechnology  :
            def __init__(self):
                self.name   =  'hyperspaceDriveTechnology'
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()
            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].researchclass.hipuztek.currentlevel<3:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.hipuztek.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.hipuztek.currentlevel<3:
                        planetlist[arastırmayapcakgezegen].researchclass.hipuztek.yükselt()
                    else:
                        self.buildable = 1
                if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<7:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.gereken()
                    if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<7:
                        planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
            pass
        class espionageTechnology  :
            def __init__(self):
                self.name   =  'espionageTechnology '
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()
            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<3:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.gereken()
                    if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<3:
                        planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
            pass
        class computerTechnology   :
            def __init__(self):
                self.name   =  'computerTechnology '
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()
            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<1:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.gereken()
                    if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<1:
                        planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
            pass
        class astrophysicsTechnology   :
            def __init__(self):
                self.name   =  'astrophysicsTechnology '
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()
            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].researchclass.casusluktek.currentlevel<4:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.casusluktek.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.casusluktek.currentlevel<4:
                        planetlist[arastırmayapcakgezegen].researchclass.casusluktek.yükselt()
                    else:
                        self.buildable = 1
                if planetlist[arastırmayapcakgezegen].researchclass.impulsitici.currentlevel<3:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.impulsitici.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.impulsitici.currentlevel<3:
                        planetlist[arastırmayapcakgezegen].researchclass.impulsitici.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
            pass
        class researchNetworkTechnology   :
            def __init__(self):
                self.name   =  'researchNetworkTechnology'
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()
            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].researchclass.bilgisayartek.currentlevel<10:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.bilgisayartek.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.bilgisayartek.currentlevel<10:
                        planetlist[arastırmayapcakgezegen].researchclass.bilgisayartek.yükselt()
                    else:
                        self.buildable = 1
                if planetlist[arastırmayapcakgezegen].researchclass.hipuztek.currentlevel<8:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.hipuztek.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.hipuztek.currentlevel<8:
                        planetlist[arastırmayapcakgezegen].researchclass.hipuztek.yükselt()
                    else:
                        self.buildable = 1
                if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<10:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.gereken()
                    if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<10:
                        planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
            pass
        class gravitonTechnology   :
            def __init__(self):
                self.name   =  'gravitonTechnology'
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()
            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<12:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.gereken()
                    if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<12:
                        planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
            pass
        class weaponsTechnology   :
            def __init__(self):
                self.name   =  'weaponsTechnology'
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()
            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<4:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.gereken()
                    if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<4:
                        planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
            pass
        class shieldingTechnology   :
            def __init__(self):
                self.name   =  'shieldingTechnology'
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()
            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].researchclass.energytek.currentlevel<3:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].researchclass.energytek.gereken()
                    if planetlist[arastırmayapcakgezegen].researchclass.energytek.currentlevel<3:
                        planetlist[arastırmayapcakgezegen].researchclass.energytek.yükselt()
                    else:
                        self.buildable = 1
                if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<6:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.gereken()
                    if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<6:
                        planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
            pass
        class armorTechnology   :
            def __init__(self):
                self.name   =  'armorTechnology'
                self.url    =   servercode+'ingame&component=research'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
                self.buildable=1
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    arastırmaurl()
            def pregereken(self):
                if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<2:
                    self.buildable=0
                    planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.gereken()
                    if planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.currentlevel<2:
                        planetlist[arastırmayapcakgezegen].tesisler.arastırmalab.yükselt()
                    else:
                        self.buildable = 1
            def gereken(self):
                self.pregereken()
                if self.buildable==1:
                    self.checkurl()
                    try:
                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                        if a == True:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a==True:
                            pass
                        else:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                            driver.implicitly_wait(5)
                        try:
                            a = check_displayed_by_css ( '.costs > ul > .metal' )
                            if a == True:
                                self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                            a = check_displayed_by_css ( '.costs > ul > .crystal' )
                            if a == True:
                                self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                            a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                            if a == True:
                                self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                            a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                            if a == True:
                                self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                            a = check_displayed_by_css ( '.build_duration > .value' )
                            if a == True:
                                self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                            a = check_displayed_by_css ( '.level' )
                            if a == True:
                                level=driver.find_element(By.CSS_SELECTOR,'.level').text
                                level=[int(n) for n in level.split() if n.isdigit()]
                                self.currentlevel=level[0]
                            return True
                        except ValueError:
                            return False
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def yükselt(self):
                if checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
            pass
    class Tesisler:
        def __init__(self):
            self.robot=self.Robot()
            self.tershane=self.Shipyard ()
            self.arastırmalab=self.ResearchLaboratory()
            self.nanit=self.Nanit()
            self.roketsilosu=self.Rocketsilo()
        class Robot:
            def __init__(self):
                self.name   =  'roboticsFactory'
                self.url    =   servercode+'ingame&component=facilities'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    tesislerurl()
            def gereken(self):
                self.checkurl()
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a==True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                        driver.implicitly_wait(5)
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                        a = check_displayed_by_css ( '.level' )
                        if a == True:
                            level=driver.find_element(By.CSS_SELECTOR,'.level').text
                            level=[int(n) for n in level.split() if n.isdigit()]
                            self.currentlevel=level[0]
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                if checkconstructionque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class Shipyard:
            def __init__(self):
                self.name   =  'shipyard '
                self.url    =   servercode+'ingame&component=facilities'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    tesislerurl()
            def gereken(self):
                self.checkurl()
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a==True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                        driver.implicitly_wait(5)
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                        a = check_displayed_by_css ( '.level' )
                        if a == True:
                            level=driver.find_element(By.CSS_SELECTOR,'.level').text
                            level=[int(n) for n in level.split() if n.isdigit()]
                            self.currentlevel=level[0]
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                if checkconstructionque()=='empty' and checkshipyardque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class ResearchLaboratory :
            def __init__(self):
                self.name   =  'researchLaboratory'
                self.url    =   servercode+'ingame&component=facilities'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    tesislerurl()
            def gereken(self):
                self.checkurl()
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a==True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                        driver.implicitly_wait(5)
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                        a = check_displayed_by_css ( '.level' )
                        if a == True:
                            level=driver.find_element(By.CSS_SELECTOR,'.level').text
                            level=[int(n) for n in level.split() if n.isdigit()]
                            self.currentlevel=level[0]
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                if checkconstructionque()=='empty' and checkresearchque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class Nanit :
            def __init__(self):
                self.name   =  'naniteFactory'
                self.url    =   servercode+'ingame&component=facilities'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    tesislerurl()
            def gereken(self):
                self.checkurl()
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a==True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                        driver.implicitly_wait(5)
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                        a = check_displayed_by_css ( '.level' )
                        if a == True:
                            level=driver.find_element(By.CSS_SELECTOR,'.level').text
                            level=[int(n) for n in level.split() if n.isdigit()]
                            self.currentlevel=level[0]
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                if checkconstructionque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class Rocketsilo :
            def __init__(self):
                self.name   =  'missileSilo'
                self.url    =   servercode+'ingame&component=facilities'
                self.gerekenmetal=0
                self.gerekenkristal=0
                self.gerekendeut=0
                self.gerekenenerji=0
                self.currentlevel=0
                self.buildtime=0
            def checkurl(self):
                if driver.current_url==self.url:
                    pass
                else:
                    tesislerurl()
            def gereken(self):
                self.checkurl()
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon')
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a=check_displayed_by_css('.costs > ul > .metal') or check_displayed_by_css('.costs > ul > .crystal') or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a==True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                        driver.implicitly_wait(5)
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .metal').text)
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .crystal').text)
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut=converttonumber(driver.find_element(By.CSS_SELECTOR,'.costs > ul > .deuterium').text)
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji=converttonumber(driver.find_element(By.CSS_SELECTOR,'.additional_energy_consumption > .value').text)
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime=driver.find_element(By.CSS_SELECTOR,'.build_duration > .value').text
                        a = check_displayed_by_css ( '.level' )
                        if a == True:
                            level=driver.find_element(By.CSS_SELECTOR,'.level').text
                            level=[int(n) for n in level.split() if n.isdigit()]
                            self.currentlevel=level[0]
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                if checkconstructionque()=='empty':
                    try:
                        self.checkurl()
                        if self.gereken()==True:
                            if metalmevcut>=self.gerekenmetal and kristalmevcut>=self.gerekenkristal and deutmevcut>=self.gerekendeut:
                                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                if a == True:
                                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon').click()
                                    driver.implicitly_wait(5)
                                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon > .upgrade' )
                                    if a == True:
                                        driver.find_element(By.CSS_SELECTOR,f'.technology.{self.name} > .icon > .upgrade').click()
                                        driver.implicitly_wait(5)
                                        return True
                            else:
                                return False
                        checkconstructionque ( )
                    except selenium.common.exceptions.NoSuchElementException:
                        return False
                else:
                    return False
            def cancel(self):
                #cancelconstruction
                self.checkurl()
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR,'.abort_link').click()
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
    class Ships:
        def __init__(self):
            self.ltransporter=self.Largetransporter()
            self.havcı=self.Havcı()
            self.geridönüsüm=self.Recycler()
            self.agıravcı=self.fighterHeavy()
            self.kruvazör=self.cruiser()
            self.komuta=self.battleship()
            self.fırkateyn=self.interceptor()
            self.bombardıman=self.bomber()
            self.muhrip=self.destroyer()
            self.ölümyıldızı=self.deathstar()
            self.azrail=self.reaper()
            self.kasif=self.explorer()
            self.knakliye=self.transporterSmall()
            self.kolonigemisi=self.colonyShip()
            self.sonda=self.espionageProbe()
            self.solaruydu=self.solarSatellite()
            self.paletli=self.resbuggy()
        class Largetransporter:
            def __init__(self):
                self.name = 'transporterLarge'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 5 )
                                        a = check_displayed_by_css ( '#build_amount' )
                                        if a == True:
                                            amount=str(amount)+'\n'
                                            try:
                                                driver.find_element(By.CSS_SELECTOR,'#build_amount').send_keys(amount)
                                            except selenium.common.exceptions.ElementNotInteractableException:
                                                pass
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class Havcı:
            def __init__(self):
                self.name = 'fighterLight'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 3)
                                        b = driver.find_element(By.ID,'build_amount').is_enabled()
                                        print(b)
                                        if b == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.ID,'build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class fighterHeavy:
            def __init__(self):
                self.name = 'fighterHeavy'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 3)
                                        b = driver.find_element(By.ID,'build_amount').is_enabled()
                                        print(b)
                                        if b == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.ID,'build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class cruiser :
            def __init__(self):
                self.name = 'cruiser'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 3)
                                        b = driver.find_element(By.ID,'build_amount').is_enabled()
                                        print(b)
                                        if b == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.ID,'build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class battleship :
            def __init__(self):
                self.name = 'battleship'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 3)
                                        b = driver.find_element(By.ID,'build_amount').is_enabled()
                                        print(b)
                                        if b == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.ID,'build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class interceptor  :
            def __init__(self):
                self.name = 'interceptor'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber(level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 3)
                                        b = driver.find_element(By.ID,'build_amount').is_enabled()
                                        print(b)
                                        if b == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.ID,'build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )    #fırkateyn
        class bomber :
            def __init__(self):
                self.name = 'bomber'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 3)
                                        b = driver.find_element(By.ID,'build_amount').is_enabled()
                                        print(b)
                                        if b == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.ID,'build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class destroyer :
            def __init__(self):
                self.name = 'destroyer'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 3)
                                        b = driver.find_element(By.ID,'build_amount').is_enabled()
                                        print(b)
                                        if b == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.ID,'build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class deathstar :
            def __init__(self):
                self.name = 'deathstar'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 3)
                                        b = driver.find_element(By.ID,'build_amount').is_enabled()
                                        print(b)
                                        if b == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.ID,'build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class reaper :
            def __init__(self):
                self.name = 'reaper'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 3)
                                        b = driver.find_element(By.ID,'build_amount').is_enabled()
                                        print(b)
                                        if b == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.ID,'build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class explorer :
            def __init__(self):
                self.name = 'explorer'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 3)
                                        b = driver.find_element(By.ID,'build_amount').is_enabled()
                                        print(b)
                                        if b == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.ID,'build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class transporterSmall :
            def __init__(self):
                self.name = 'transporterSmall'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 3)
                                        b = driver.find_element(By.ID,'build_amount').is_enabled()
                                        print(b)
                                        if b == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.ID,'build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class colonyShip :
            def __init__(self):
                self.name = 'colonyShip'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 3)
                                        b = driver.find_element(By.ID,'build_amount').is_enabled()
                                        print(b)
                                        if b == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.ID,'build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class espionageProbe :
            def __init__(self):
                self.name = 'espionageProbe'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 3)
                                        b = driver.find_element(By.ID,'build_amount').is_enabled()
                                        print(b)
                                        if b == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.ID,'build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class solarSatellite :
            def __init__(self):
                self.name = 'solarSatellite'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 5 )
                                        a = check_displayed_by_css ( '#build_amount' )
                                        if a == True:
                                            amount=str(amount)+'\n'
                                            try:
                                                driver.find_element(By.CSS_SELECTOR,'#build_amount').send_keys(amount)
                                            except selenium.common.exceptions.ElementNotInteractableException:
                                                pass
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class resbuggy :
            def __init__(self):
                self.name = 'resbuggy'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 3)
                                        b = driver.find_element(By.ID,'build_amount').is_enabled()
                                        print(b)
                                        if b == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.ID,'build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class Recycler:
            def __init__(self):
                self.name = 'recycler'
                self.url = servercode + 'ingame&component=shipyard'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        try:
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        except selenium.common.exceptions.ElementClickInterceptedException:
                            WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.CSS_SELECTOR( f'.technology.{self.name} > .icon' )))
                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 3)
                                        b = driver.find_element(By.ID,'build_amount').is_enabled()
                                        print(b)
                                        if b == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.ID,'build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
    class Defenses:
        def __init__(self):
            self.roketatar=self.rocketLauncher()
            self.hlazer=self.laserCannonLight()
            self.alazer=self.laserCannonHeavy()
            self.gaustopu=self.gaussCannon()
            self.iyontopu=self.ionCannon()
            self.plazmatopu=self.plasmaCannon()
            self.skalkan=self.shieldDomeSmall()
            self.lkalkan=self.shieldDomeLarge()
            self.yakalayıcıroket=self.missileInterceptor()
            self.gar=self.missileInterplanetary()
        class rocketLauncher :
            def __init__(self):
                self.name = 'rocketLauncher '
                self.url = servercode + 'ingame&component=defenses'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR,
                                f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber ( level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 5 )
                                        a = check_displayed_by_css ( '#build_amount' )
                                        if a == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.CSS_SELECTOR,'#build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class laserCannonLight :
            def __init__(self):
                self.name = 'laserCannonLight'
                self.url = servercode + 'ingame&component=defenses'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber(level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 5 )
                                        a = check_displayed_by_css ( '#build_amount' )
                                        if a == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.CSS_SELECTOR,'#build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class laserCannonHeavy :
            def __init__(self):
                self.name = 'laserCannonHeavy'
                self.url = servercode + 'ingame&component=defenses'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber(level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 5 )
                                        a = check_displayed_by_css ( '#build_amount' )
                                        if a == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.CSS_SELECTOR,'#build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class gaussCannon  :
            def __init__(self):
                self.name = 'gaussCannon'
                self.url = servercode + 'ingame&component=defenses'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber(level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 5 )
                                        a = check_displayed_by_css ( '#build_amount' )
                                        if a == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.CSS_SELECTOR,'#build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class ionCannon  :
            def __init__(self):
                self.name = 'ionCannon'
                self.url = servercode + 'ingame&component=defenses'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber(level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 5 )
                                        a = check_displayed_by_css ( '#build_amount' )
                                        if a == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.CSS_SELECTOR,'#build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class plasmaCannon    :
            def __init__(self):
                self.name = 'plasmaCannon'
                self.url = servercode + 'ingame&component=defenses'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber(level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 5 )
                                        a = check_displayed_by_css ( '#build_amount' )
                                        if a == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.CSS_SELECTOR,'#build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )    #fırkateyn
        class shieldDomeSmall   :
            def __init__(self):
                self.name = 'shieldDomeSmall'
                self.url = servercode + 'ingame&component=defenses'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber(level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 5 )
                                        a = check_displayed_by_css ( '#build_amount' )
                                        if a == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.CSS_SELECTOR,'#build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class shieldDomeLarge   :
            def __init__(self):
                self.name = 'shieldDomeLarge'
                self.url = servercode + 'ingame&component=defenses'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber(level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 5 )
                                        a = check_displayed_by_css ( '#build_amount' )
                                        if a == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.CSS_SELECTOR,'#build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class missileInterceptor   :
            def __init__(self):
                self.name = 'missileInterceptor'
                self.url = servercode + 'ingame&component=defenses'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber(level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 5 )
                                        a = check_displayed_by_css ( '#build_amount' )
                                        if a == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.CSS_SELECTOR,'#build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
        class missileInterplanetary   :
            def __init__(self):
                self.name = 'missileInterplanetary'
                self.url = servercode + 'ingame&component=defenses'
                self.gerekenmetal = 0
                self.gerekenkristal = 0
                self.gerekendeut = 0
                self.gerekenenerji = 0
                self.currentlevel = 0
                self.buildtime = 0
                self.mevcutadet=0
                self.hedefmiktar=0
            def checkurl(self):
                if driver.current_url == self.url:
                    pass
                else:
                    driver.get(self.url)
            def gereken(self):
                self.checkurl ( )
                try:
                    a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                    if a == True:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                        '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                    if a == True:
                        pass
                    else:
                        driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                        driver.implicitly_wait ( 5 )
                    try:
                        a = check_displayed_by_css ( '.costs > ul > .metal' )
                        if a == True:
                            self.gerekenmetal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .metal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .crystal' )
                        if a == True:
                            self.gerekenkristal = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .crystal' ).text )
                        a = check_displayed_by_css ( '.costs > ul > .deuterium' )
                        if a == True:
                            self.gerekendeut = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.costs > ul > .deuterium' ).text )
                        a = check_displayed_by_css ( '.additional_energy_consumption > .value' )
                        if a == True:
                            self.gerekenenerji = converttonumber (
                                driver.find_element(By.CSS_SELECTOR, '.additional_energy_consumption > .value' ).text )
                        a = check_displayed_by_css ( '.build_duration > .value' )
                        if a == True:
                            self.buildtime = driver.find_element(By.CSS_SELECTOR, '.build_duration > .value' ).text
                        a = check_displayed_by_css (f'.technology.{self.name} > .icon'  )
                        if a == True:
                            level = driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon > .amount' ).text
                            self.mevcutadet = converttonumber(level)
                        return True
                    except ValueError:
                        return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def yükselt(self):
                try:
                    self.checkurl ( )
                    if self.hedefmiktar>self.mevcutadet:
                        if self.gereken ( ) == True:
                            if self.hedefmiktar>self.mevcutadet:
                                amount = self.hedefmiktar - self.mevcutadet
                                üret = []
                                if self.gerekenmetal > 0:
                                    üret.append ( metalmevcut / self.gerekenmetal )
                                if self.gerekenkristal > 0:
                                    üret.append ( kristalmevcut / self.gerekenkristal )
                                if self.gerekendeut > 0:
                                    üret.append ( deutmevcut / self.gerekendeut )
                                ürett = True
                                for ür in üret:
                                    if ür < 1:
                                        ürett = False
                                if ürett == True:
                                    if min ( üret )<amount:
                                        amount = min ( üret )
                                if metalmevcut >= self.gerekenmetal and kristalmevcut >= self.gerekenkristal and deutmevcut >= self.gerekendeut:
                                    try:
                                        a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                                        if a == True:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                                            '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                                        if a == True:
                                            pass
                                        else:
                                            driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                                        driver.implicitly_wait ( 5 )
                                        a = check_displayed_by_css ( '#build_amount' )
                                        if a == True:
                                            amount=str(amount)+'\n'
                                            driver.find_element(By.CSS_SELECTOR,'#build_amount').send_keys(amount)
                                            time.sleep(1)
                                            driver.implicitly_wait ( 5 )
                                            return True
                                        else:
                                            return False
                                    except selenium.common.exceptions.NoSuchElementException:
                                        return False
                                else:
                                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    return False
            def cancel(self):
                # cancelconstruction
                self.checkurl ( )
                a = check_displayed_by_css ( f'.technology.{self.name} > .icon' )
                if a == True:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                a = check_displayed_by_css ( '.costs > ul > .metal' ) or check_displayed_by_css (
                    '.costs > ul > .crystal' ) or check_displayed_by_css ( '.costs > ul > .deuterium' )
                if a == True:
                    pass
                else:
                    driver.find_element(By.CSS_SELECTOR, f'.technology.{self.name} > .icon' ).click ( )
                    driver.implicitly_wait ( 5 )
                driver.find_element(By.CSS_SELECTOR, '.abort_link' ).click ( )
                driver.implicitly_wait ( 5 )
                time.sleep ( 2 )
                driver.find_element(By.XPATH, './/*[@class="yes"]' ).click ( )
                checkconstructionque ( )
#filo hareketlerini kontrol et.
def checkfleetmoves():
    global filledevent,detaylımoves
    driver.implicitly_wait(5)
    try:
        time.sleep(2)
        allmoves = driver.find_element(By.ID, 'messages_collapsed' ).text
        allmoves=arrayyap(allmoves)
        if allmoves[0]=='LADEN' or allmoves[0]=='LOADING' or allmoves[0]=='YÜKLENİYOR':
            time.sleep(2)
            allmoves = driver.find_element(By.ID, 'messages_collapsed' ).text
            allmoves=arrayyap(allmoves)
            if allmoves[0]=='LADEN' or allmoves[0]=='LOADING' or allmoves[0]=='YÜKLENİYOR':
                time.sleep(2)
                allmoves = driver.find_element(By.ID, 'messages_collapsed' ).text
                allmoves = arrayyap ( allmoves )
                if allmoves[0] == 'LADEN' or allmoves[0] == 'LOADING' or allmoves[0] == 'YÜKLENİYOR':
                    time.sleep ( 2 )
        detaylımoves =driver.find_element(By.ID, 'eventboxContent' )
        driver.execute_script ( 'arguments[0].style = "display";', detaylımoves )
        detaylımoves =driver.find_element(By.ID, 'eventContent' )
        filledevent = driver.find_element(By.ID, 'eventboxFilled' ).text
        filledevent=arrayyap(filledevent)
        attackalert = driver.find_element(By.ID, 'attack_alert' ).text
        attackalert=arrayyap(attackalert)
        blankevent=driver.find_element(By.ID,'eventboxBlank').text
        blankevent=arrayyap(blankevent)
        loadingevent=driver.find_element(By.ID,'eventboxLoading').text
        loadingevent=arrayyap(loadingevent)
        if len(loadingevent)!=0:
            print('Loadingevent=',loadingevent)
        print ( 'allmoves=',allmoves )
        if len(filledevent)!=0:
            print ( 'filledevent=',filledevent )
        if len(blankevent)!=0:
            print ( 'blankevent=',blankevent )
        if len(attackalert)!=0:
            print ( 'attackalert=',attackalert )
        try:
            if len(blankevent)==0:
                print('Fleet move detected')
                if len(filledevent)>=6:
                    if len(attackalert)!=0 or filledevent[3]=='feindlich' or filledevent[3]=='düşmanca' or filledevent[3]=='hostile' or filledevent[5]=='feindlich' or filledevent[5]=='düşmanca' or filledevent[5]=='hostile':
                        print('-----------------')
                        print('Danger!')
                        return 'danger'
                    else:
                        print('+++++++++++++++++')
                        print ( 'You are safe !' )
                        return 'Fleet move detected'
                else:
                    if len(attackalert)!=0 or filledevent[3]=='feindlich' or filledevent[3]=='düşmanca' or filledevent[3]=='hostile':
                        print('-----------------')
                        print('Danger!')
                        return 'danger'
                    else:
                        print('+++++++++++++++++')
                        print ( 'You are safe !' )
                        return 'Fleet move detected'
            else:
                print('_____')
                print('You are safe !')
                return 'safe'
        except IndexError:
            if len(blankevent)==0:
                print ( 'Fleet move detected' )
                try:
                    if len(attackalert)!=0 or filledevent[3]=='feindlich' or filledevent[5]=='feindlich' or filledevent[3]=='düşmanca' or filledevent[5]=='düşmanca' or filledevent[3]=='hostile' or filledevent[5]=='hostile' :
                        print('-----------------')
                        print('attackalert=',attackalert)
                        print('len(attackalert)=',len(attackalert))
                        print('Danger!')
                        print('-----------------')
                        return 'danger'
                    else:
                        print('You are safe !')
                        return 'Fleet move detected'
                except IndexError:
                    if len ( attackalert ) != 0:
                        print ( '-----------------' )
                        print ( 'attackalert=', attackalert )
                        print ( 'len(attackalert)=', len ( attackalert ) )
                        print ( 'Danger!' )
                        print ( '-----------------' )
                        return 'danger'
                    print(allmoves)
    except selenium.common.exceptions.NoSuchElementException:
        pass
def checkfinalfleetmoves(timecheck,waitingtimeseconds):
    global timecheck1
    if checkfleetmoves ( ) == 'danger' and datetime.datetime.now ( ).timestamp ( ) > timecheck + waitingtimeseconds:
        timecheck1 = datetime.datetime.now ( ).timestamp ( )
        webhook.send (
            f'DANGER! Fleet move detected at {datetime.datetime.fromtimestamp ( int ( datetime.datetime.now ( ).timestamp ( ) ) )} in {veriagı[2]}.\n{filledevent}\n{detaylımoves.text}\n__________________________' )


def planetnumber():
    global numberofplanets,planetclick,t
    driver.implicitly_wait(5)
    time.sleep(1)
    planetclick=[]
    def xex():
        global t,planetclick
        try:
            t=driver.find_element(By.ID,'planetList').find_elements(By.CSS_SELECTOR,'div')
            planetclick=[0 for i in t]
            for i in range(len(t)):
                a=t[i].find_element(By.CSS_SELECTOR,'a').get_attribute('href')
                planetclick[i]=a
            t=arrayyap(driver.find_element(By.ID,'planetList').text)
            print(t)
        except selenium.common.exceptions.NoSuchElementException:
            print('planetnumber error')
            pass
        if (None in planetclick ) or (0 in planetclick):
            print('non')
            xex()
    xex()
    print ( planetclick )
    numberofplanets = int ( len ( t ) / 2 )


def gettheplanet(x):
    try:
        driver.implicitly_wait(5)
        try:
            driver.get(planetclick[x])
        except IndexError or selenium.common.exceptions.WebDriverException:
            pass
        driver.implicitly_wait(5)
    except selenium.common.exceptions.NoSuchElementException or IndexError:
        pass
def üretgemisavunma(x,hedefmiktarı):
    x.hedefmiktar=hedefmiktarı
    if x.hedefmiktar>0:
        print(f'{x.name} hedefi {hedefmiktarı}.')
        if checkshipyardque ( ) == 'empty':
            if x.mevcutadet < x.hedefmiktar:
                if x.gereken ( ) != False:
                    print ( f'{x.name} adeti = {x.mevcutadet}' )
                    if x.mevcutadet < x.hedefmiktar:
                        if x.yükselt ( ):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
    else:
        return False
def üretgemisavunmasüreklikontrol(x,hedefmiktarı):
    x.hedefmiktar=hedefmiktarı
    if x.hedefmiktar>0:
        print(f'{x.name} hedefi {hedefmiktarı}.')
        if checkshipyardque ( ) == 'empty':
            if x.gereken ( ) != False:
                print ( f'{x.name} adeti = {x.mevcutadet}' )
                if x.mevcutadet < x.hedefmiktar:
                    if x.yükselt ( ):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
    else:
        return False

def teknikarttırma(minimumseviye,x):
    print(f'{x.name} tek seviyesi:',x.currentlevel)
    if x.currentlevel < minimumseviye:
        if checkresearchque()=='empty':
            if x.gereken ( ) != False:
                if x.currentlevel < minimumseviye:
                    if x.yükselt ( ):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
    else:
        return False
def tesisarttırma(tesis,minimumseviye):
    driver.implicitly_wait(3)
    if tesis.currentlevel < minimumseviye:
        if checkconstructionque ( ) == 'empty':
            tesis.gereken ( )
            if tesis.currentlevel < minimumseviye:
                print ( f'{tesis.name} seviyesi:', tesis.currentlevel )
                if tesis.yükselt ( )==True:
                    print ( f'Tesis {tesis.name}yükseltiliyor' )
                    return True
                else:
                    return False
            else:
                return False
    else:
        return False

def tesislerasama1(selectedplanet,mindeutsev,minlabsev,minrobotseviyesi,mintershanesev,minnanitsev,minroksil):
    if mindeutsev<selectedplanet.madenlerclass.deut.currentlevel:
        if tesisarttırma(selectedplanet.tesisler.arastırmalab,minlabsev)==False:
            if tesisarttırma ( selectedplanet.tesisler.robot, minrobotseviyesi ) == False:
                if tesisarttırma ( selectedplanet.tesisler.tershane, mintershanesev ) == False:
                    if tesisarttırma ( selectedplanet.tesisler.nanit, minnanitsev ) == False:
                        if tesisarttırma ( selectedplanet.tesisler.roketsilosu, minroksil ) == False:
                            pass
    else:
        if selectedplanet.madenlerclass.deut.gereken ( ):
            pass
        if mindeutsev < selectedplanet.madenlerclass.deut.currentlevel:
            if tesisarttırma(selectedplanet.tesisler.arastırmalab,minlabsev)==False:
                if tesisarttırma ( selectedplanet.tesisler.robot, minrobotseviyesi ) == False:
                    if tesisarttırma ( selectedplanet.tesisler.tershane, mintershanesev ) == False:
                        if tesisarttırma ( selectedplanet.tesisler.nanit, minnanitsev ) == False:
                            if tesisarttırma ( selectedplanet.tesisler.roketsilosu, minroksil ) == False:
                                pass
        else:
            pass


def totalkaynaklar():
    theplanet=planetlist[-1]
    try:
        theplanet.mevcutmetal, theplanet.mevcutkristal, theplanet.mevcutdeut, theplanet.mevcutsolar, theplanet.mevcutdarkmatter = mevcutmadenler ( )
    except TypeError:
        pass
    tempmet = 0;    tempkris = 0;    tempdeut = 0
    try:
        for theplanet in planetlist:
            tempmet+=theplanet.mevcutmetal
            tempkris+=theplanet.mevcutkristal
            tempdeut+=theplanet.mevcutdeut
        for theplanet in planetlist:
            try:
                print ( f'Gezegen {planetlist.index ( theplanet ) + 1} Current levels=', 'Metal:',
                        theplanet.madenlerclass.metal.currentlevel, 'Kristal:',
                        theplanet.madenlerclass.kristal.currentlevel, 'Deut:',
                        theplanet.madenlerclass.deut.currentlevel )
                if theplanet.mevcutmetal!=0 and theplanet.mevcutkristal!=0 and theplanet.mevcutdeut!=0:
                    print (
                        f'Metal: {int(theplanet.mevcutmetal/1000)}k  ,Kristal: {int(theplanet.mevcutkristal/1000)}k  ,Deut: {int(theplanet.mevcutdeut/1000)}k' )
                else:
                    print (
                        f'Metal: {theplanet.mevcutmetal} ,Kristal: {theplanet.mevcutkristal}  ,Deut: {theplanet.mevcutdeut}' )
            except ValueError:
                pass
        if tempmet!= 0 and tempkris != 0 and tempdeut!= 0:
            print ( f'Toplam btg kaynaklar=   Metal:{int(tempmet/1000)}k       Kristal:{int(tempkris/1000)}k     Deut:{int(tempdeut/1000)}k' )
        else:
            print (
                f'Toplam btg kaynaklar=   Metal:{tempmet}     Kristal:{tempkris}    Deut:{tempdeut}' )
        print('_____')
        ha = 0;    la = 0; gd=0
        for theplanet in planetlist:
            ha+=theplanet.gemiler.havcı.mevcutadet
            la+=theplanet.gemiler.ltransporter.mevcutadet
            gd+=theplanet.gemiler.geridönüsüm.mevcutadet
        print ( f'Toplam btg Gemiler=   L.taşıyıcı:{ha}         H.avcı:{la}          GD:{gd}  ' )
        print('_____')
    except ValueError:
        pass

def tamgiriş():
    global planetlist,timecheck2
    açılış()
    acceptcookies()
    login()
    timecheck2=int(datetime.datetime.now ( ).timestamp ( ))
    enteraserver()
    sourceurl()
    time.sleep(3)
    planetnumber()
    planetlist=[""]
    while planetlist==[""]:
        planetlist=[planet() for i in range(numberofplanets)]
    for theplanet in planetlist:
        try:
            gettheplanet ( planetlist.index ( theplanet ) )
            if checkfleetmoves ( ) == 'danger':
                webhook.send (
                    f'DANGER! Fleet move detected at {datetime.datetime.fromtimestamp ( int ( datetime.datetime.now ( ).timestamp ( ) ) )} in {veriagı[2]}.\n{filledevent}\n{detaylımoves.text}\n__________________________' )
            print ( 'Gezegen no:', planetlist.index ( theplanet ) + 1 )
            depo.update ( )
            try:
                theplanet.mevcutmetal, theplanet.mevcutkristal, theplanet.mevcutdeut, theplanet.mevcutsolar, theplanet.mevcutdarkmatter = mevcutmadenler ( )
            except TypeError:
                pass
            theplanet.madenlerclass.metal.gereken ( )
            theplanet.madenlerclass.kristal.gereken ( )
            theplanet.madenlerclass.deut.gereken ( )
            theplanet.gemiler.havcı.gereken()
            theplanet.gemiler.ltransporter.gereken()
            theplanet.gemiler.geridönüsüm.gereken()
            print ( f'Mevcut hafif avcı={theplanet.gemiler.havcı.mevcutadet}' )
            print ( f'Mevcut l tasıyıcı={theplanet.gemiler.ltransporter.mevcutadet}' )
            print ( 'Geri dönüsüm adeti=', theplanet.gemiler.geridönüsüm.mevcutadet )
            print ( '_____' )
            print ( 'DEPO KAPASİTELERİ=', depo.metalkapasitesi, depo.kristalkapasitesi, depo.deutkapasitesi )
            print ( '_____' )
        except ValueError or IndexError:
            pass


tamgiriş()
timecheck1=int(datetime.datetime.now().timestamp ( ))
waitfor_timecheck1=15
timecheck2=int(datetime.datetime.now ( ).timestamp ( ))
timecheck3=int(datetime.datetime.now().timestamp ( ))
timecheck4=0
filledevent='Fleet moves Check'
while True:
    try:
        time.sleep ( 5 )
        print ( f'========================================================================\n{veriagı[2]}' )
        print ( datetime.datetime.fromtimestamp ( int ( datetime.datetime.now ( ).timestamp ( ) ) ) )
        print ( '_____' )
        if datetime.datetime.now ( ).timestamp ( ) > timecheck3+200:
            planetnumber ( )
            timecheck3=datetime.datetime.now ( ).timestamp ( )
        if numberofplanets > len ( planetlist ):
            planetlist = [planet() for i in range(numberofplanets)]
            print('Warning new planet')
        totalkaynaklar()
        time.sleep ( 25 )
        checkfinalfleetmoves(timecheck1,waitfor_timecheck1)
        for theplanet in planetlist:
            print ( '++++++++++++++++' )
            try:
                print ( f'Gezegen no: {planetlist.index ( theplanet ) + 1}\n{veriagı[2]}' )
            except ValueError:
                pass
            print ( '_____' )
            print ( 'Current levels=', 'Metal:', theplanet.madenlerclass.metal.currentlevel, 'Kristal:',
                    theplanet.madenlerclass.kristal.currentlevel, 'Deut:',
                    theplanet.madenlerclass.deut.currentlevel )
            print ( f'Mevcut hafif avcı={theplanet.gemiler.havcı.mevcutadet}' )
            print ( f'Mevcut l tasıyıcı={theplanet.gemiler.ltransporter.mevcutadet}' )
            print ( 'Geri dönüsüm adeti=', theplanet.gemiler.geridönüsüm.mevcutadet )
            print ( '_____' )
            if datetime.datetime.now ( ).timestamp ( ) > theplanet.waittime:
                print('processing...')
                starttime=datetime.datetime.now ( ).timestamp ( )
                try:
                    gettheplanet ( planetlist.index ( theplanet ) )
                except ValueError:
                    time.sleep(2)
                    planetnumber ( )
                    planetlist = [planet ( ) for i in range ( numberofplanets )]
                    try:
                        gettheplanet ( planetlist.index ( theplanet ) )
                    except ValueError:
                        kapanış()
                        break
                time.sleep(2)
                checkfinalfleetmoves(timecheck1,0)
                try:
                    try:
                        theplanet.mevcutmetal, theplanet.mevcutkristal, theplanet.mevcutdeut, theplanet.mevcutsolar, theplanet.mevcutdarkmatter = mevcutmadenler ( )
                    except TypeError:
                        pass
                    print ( '_____' )
                    print (
                        f'Metal: {theplanet.mevcutmetal}  ,Kristal: {theplanet.mevcutkristal}  ,Deut: {theplanet.mevcutdeut}  ,Solar: {theplanet.mevcutsolar}  ,Darkmatter: {theplanet.mevcutdarkmatter}' )
                    print ( '_____' )
                    ##########  ARASTIRMA ##############
                    try:
                        if planetlist.index ( theplanet ) == arastırmayapcakgezegen:
                            if checkresearchque ( ) == 'empty':
                                arastır(theplanet,minbilgisaytek,mincasusluktek,minkalkantek,minlazertek,minenerjitek,minyanmalı,minimpuls,minastro,miniyon,minhiptek,minhipit,minplazma,minarasagı,mingravitasyon,minsilah,minzırh)
                                genelbakis()
                    except ValueError:
                        break
                    if checkconstructionque ( ) == 'empty':
                        try:
                            theplanet.mevcutmetal, theplanet.mevcutkristal, theplanet.mevcutdeut, theplanet.mevcutsolar, theplanet.mevcutdarkmatter = mevcutmadenler ( )
                        except TypeError:
                            pass
                        depo.update ( )
                        print ( '_____' )
                        print ( 'DEPO KAPASİTELERİ=', depo.metalkapasitesi, depo.kristalkapasitesi, depo.deutkapasitesi )
                        print ( '_____' )
                        if depo.metalkapasitesi > theplanet.mevcutmetal and depo.kristalkapasitesi > theplanet.mevcutkristal and depo.deutkapasitesi > theplanet.mevcutdeut:
                            if theplanet.mevcutsolar <= 0:
                                print ( '+++++++' )
                                print ( 'yükselt Solar ' )
                                print ( '+++++++' )
                                if theplanet.madenlerclass.solar.yükselt ( ) == True:
                                    pass
                            else:
                                print ( 'Solara gerek yok.' )
                                ###########maden üretimi##########
                                if checkconstructionque ( ) == 'empty':
                                    try:
                                        theplanet.madenlerclass.metal.gereken ( )
                                        theplanet.madenlerclass.kristal.gereken ( )
                                        theplanet.madenlerclass.deut.gereken ( )
                                    except selenium.common.exceptions.StaleElementReferenceException:
                                        webhook.send ( 'StaleElementReferenceException, yeniden giriş yapılıyor.' )
                                        print ( 'StaleElementReferenceException, yeniden giriş yapılıyor.2' )
                                        kapanış()
                                        pass
                                    print ( 'Current levels=', theplanet.madenlerclass.metal.currentlevel,
                                            theplanet.madenlerclass.kristal.currentlevel,
                                            theplanet.madenlerclass.deut.currentlevel )
                                    if theplanet.madenlerclass.metal.currentlevel < theplanet.madenlerclass.kristal.currentlevel + int(veriagı[3]) and int(veriagı[3])!=99 :
                                        print ( '+++++++' )
                                        print ( 'yükselt Metal ' )
                                        print ( '+++++++' )
                                        if theplanet.madenlerclass.metal.yükselt ( ) == True:
                                            pass
                                        durationoftheloop = datetime.datetime.now ( ).timestamp ( ) - starttime
                                        theplanet.waittime = datetime.datetime.now ( ).timestamp ( ) + (
                                                int ( durationoftheloop ) * len ( planetlist ))
                                    else:
                                        if theplanet.madenlerclass.kristal.currentlevel < theplanet.madenlerclass.deut.currentlevel + int(veriagı[4]) and ( int(veriagı[4])!=99 and int(veriagı[4])!=100):
                                            print ( '+++++++' )
                                            print ( 'yükselt kristal ' )
                                            print ( '+++++++' )
                                            if theplanet.madenlerclass.kristal.yükselt ( ) == True:
                                                pass
                                            durationoftheloop = datetime.datetime.now ( ).timestamp ( ) - starttime
                                            theplanet.waittime = datetime.datetime.now ( ).timestamp ( ) + (
                                                    int ( durationoftheloop ) * len ( planetlist ))
                                        else:
                                            if int(veriagı[4])!=100 and int(veriagı[4])!=101:
                                                print ( '+++++++' )
                                                print ( 'yükselt Deut' )
                                                print ( '+++++++' )
                                                if theplanet.madenlerclass.deut.yükselt ( ) == True:
                                                    pass
                                                durationoftheloop = datetime.datetime.now ( ).timestamp ( ) - starttime
                                                theplanet.waittime = datetime.datetime.now ( ).timestamp ( ) + (
                                                        int ( durationoftheloop ) * len ( planetlist ))
                                else:
                                    durationoftheloop = datetime.datetime.now ( ).timestamp ( ) - starttime
                                    theplanet.waittime = datetime.datetime.now ( ).timestamp ( ) + (
                                            int ( durationoftheloop ) * len ( planetlist ))
                        else:
                            if depo ( ).metalkapasitesi <= theplanet.mevcutmetal:
                                if theplanet.madenlerclass.metaldeposu.yükselt ( ) == True:
                                    pass
                            else:
                                if depo ( ).kristalkapasitesi <= theplanet.mevcutkristal:
                                    if theplanet.madenlerclass.krisdeposu.yükselt ( ) == True:
                                        pass
                                else:
                                    if depo ( ).deutkapasitesi <= theplanet.mevcutdeut:
                                        if theplanet.madenlerclass.deutdeposu.yükselt ( ) == True:
                                            pass
                            durationoftheloop = datetime.datetime.now ( ).timestamp ( ) - starttime
                            theplanet.waittime = datetime.datetime.now ( ).timestamp ( ) + (
                                    int ( durationoftheloop ) * len ( planetlist ))
                    if checkconstructionque()=='empty':
                        ########TESİSLER###############
                        if planetlist.index ( theplanet ) == 0:
                            tesislerasama1 ( theplanet, mindeutsartı, ogezegendekiarastırmalabhedefi,
                                             robotfabrikasıhedefi, tershanehedefi, nanithedefi, roketsilosuhedefi )
                            pass
                        else:
                            tesislerasama1 ( theplanet, mindeutsartı, araştırmalabhedefi, robotfabrikasıhedefi,
                                             tershanehedefi, nanithedefi, roketsilosuhedefi )
                            pass
                    ###########tershanedeki üretim############
                    if checkshipyardque ( ) == 'empty':
                        savunmaüretimitoplu ( theplanet, tershaneüretimiyapmaşartıkristalseivyesi, roketatar,
                                              hafiflazer, agırlazer, iyontopu, gaustopu, plazmatopu, yakalayıcı,
                                              gar )
                        tershaneüretimitoplu ( theplanet, tershaneüretimiyapmaşartıkristalseivyesi, hafifavcıhedefi,
                                               agıravcıhedefi, sondahed, ltransporthedefi, ktransporthedefi,
                                               kolonigemhed, recyclerhedefi, solaruyduhedef, paletlihedef,
                                               kruvazörhedefi, komutahedefi, fırfırhedefi, bombardımanhedefi,
                                               muhriphedefi, ölümyıldızıhedef, azrailhedef, kasifhedef )
                        print ( 'LTransporter adeti=', theplanet.gemiler.ltransporter.mevcutadet )
                        print ( 'H.avcı adeti=', theplanet.gemiler.havcı.mevcutadet )
                        print ( 'Geri dönüsüm adeti=', theplanet.gemiler.geridönüsüm.mevcutadet )
                    durationoftheloop = datetime.datetime.now ( ).timestamp ( ) - starttime
                    theplanet.waittime = datetime.datetime.now ( ).timestamp ( ) + (
                            int ( durationoftheloop ) * len ( planetlist ))
                except TypeError:
                    durationoftheloop = datetime.datetime.now ( ).timestamp ( ) - starttime
                    theplanet.waittime = datetime.datetime.now ( ).timestamp ( ) + (int(durationoftheloop)*len(planetlist))
                    pass
            else:
                print ( '_____' )
                print (
                    f'Metal: {theplanet.mevcutmetal}  ,Kristal: {theplanet.mevcutkristal}  ,Deut: {theplanet.mevcutdeut}  ,Solar: {theplanet.mevcutsolar}  ,Darkmatter: {theplanet.mevcutdarkmatter}' )
                print ( '_____' )
                print ( f'In cooldown for {int ( theplanet.waittime - datetime.datetime.now ( ).timestamp ( ) )} seconds' )
            print('______')
            print ( datetime.datetime.fromtimestamp ( int ( datetime.datetime.now ( ).timestamp ( ) ) ) )
        if datetime.datetime.now ( ).timestamp ( ) > timecheck2 + 300:
            if driver.current_url == 'https://lobby.ogame.gameforge.com/de_DE/hub' or driver.current_url == 'https://lobby.ogame.gameforge.com/tr_TR/hub' or driver.current_url == 'https://lobby.ogame.gameforge.com/en_GB/hub' or driver.current_url == 'https://lobby.ogame.gameforge.com/de_DE/' or driver.current_url == 'https://lobby.ogame.gameforge.com/tr_TR/' or driver.current_url == 'https://lobby.ogame.gameforge.com/en_GB/':
                print ( 'DETECTED' )
                driver.quit()
                tamgiriş()
            timecheck2 = datetime.datetime.now ( ).timestamp ( )
            genelbakis ( )
            kaynaklar()
            genelbakis()
        else:
            pass
    except selenium.common.exceptions.StaleElementReferenceException or TypeError or selenium.common.exceptions.WebDriverException or selenium.common.exceptions.NoSuchElementException or AttributeError:
        webhook.send('StaleElementReferenceException, yeniden giriş yapılıyor.')
        print('StaleElementReferenceException, yeniden giriş yapılıyor.')
        driver.quit()
        tamgiriş()
        pass

