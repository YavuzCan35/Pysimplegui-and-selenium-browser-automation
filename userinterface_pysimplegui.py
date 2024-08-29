import PySimpleGUI as sg
import os  # to work with windows OS


# get pathname to current file
#dirname, filename = os.path.split ( os.path.abspath ( __file__ ) )
# add desired file name for saving to path
#pathname0 = os.path.join ( dirname, 'results.txt' )
def createwindow():
    sg.ChangeLookAndFeel ( 'GreenTan' )
    sg.SetOptions ( font=('Calibri', 12, 'bold') )
    sg.theme('DarkGrey14')     # Please always add color to your window
    """layout00 = [
        [sg.Text ( 'Kademeler Madenler(önce aşağıdan görüntüleye basın,sonra değiştirebilirsiniz)' )],
        [sg.Text ( 'Metal, kristalden kaç kademe daha yüksek olsun?' ), sg.InputText ( size=(3, 1), key='_m0_' )],
        [sg.Text ( 'Kristal, deuttan kaç kademe daha yüksek olsun'), sg.InputText ( size=(3, 1), key='_m1_' )],
        [sg.Text ( 'Kontrol içindir boş bırakın'), sg.InputText ( size=(3, 1), key='_m2_' )],
        [sg.Text ( 'Kademeler Tesisler' )],
        [sg.Text ( '(Deneme sırasına göredir. Arttıramayacaksa sonrakini dener)' )],
        [sg.Text ( 'Arastırma yapılacak kaçıncı gezegen'), sg.InputText ( size=(3, 1), key='_m3_' )],
        [sg.Text ( 'Arastırma gezegenindeki Lab'), sg.InputText ( size=(3, 1), key='_m4_' )],
        [sg.Text ( 'Diğer gezegenlerdeki Lab'), sg.InputText ( size=(3, 1), key='_m5_' )],
        [sg.Text ( 'Robot', size=(10, 1) ), sg.InputText ( size=(3, 1), key='_m6_' )],
        [sg.Text ( 'Tershane', size=(10, 1) ), sg.InputText ( size=(3, 1), key='_m7_' )],
        [sg.Text ( 'Nanit', size=(10, 1) ), sg.InputText ( size=(3, 1), key='_m8_' )],
        [sg.Text ( 'Roketsilosu', size=(10, 1) ), sg.InputText ( size=(6, 1), key='_m9_' )],
        [sg.Text ( 'Kademeler araştırma' )],
        [sg.Text ( 'İmpuls', size=(10, 1) ), sg.InputText ( size=(6, 1), key='_m10_' )],
        [sg.Text ( 'Bilgisayar', size=(10, 1) ), sg.InputText ( size=(6, 1), key='_m11_' )],
        [sg.ReadButton ( 'KAYDET', key='_save_' ), sg.Text ( 'Kademe hedeflerini KAYDET' )],
        [sg.ReadButton ( 'GÖRÜNTÜLE', key='_display_' ), sg.Text ( 'Kayıtlı olan kademe hedeflerini GÖRÜNTÜLE' )],
        [sg.Multiline (key='_multiline_' )]]"""
    # The tab 1, 2, 3 layouts - what goes inside the tab
    tab00_layout = [[sg.Text('Profil seçimi/oluşumu')],
                   [sg.Text ( 'Profil adı' ),
                    sg.InputText ( key='_prof_' )],
                    [sg.Button('Onayla')]
                   ]
    tab0_layout = [[sg.Text('GİRİS')],
                   [sg.Text ( 'E-mail:' ),
                    sg.InputText ( size=(25, 1), key='_giris0_' )],
                   [sg.Text ( 'Sifre:' ), sg.InputText ( size=(25, 1), key='_giris1_', password_char='*' )],
                   [sg.Text ( 'Server:' ), sg.InputText ( size=(25, 1), key='_giris2_' )],
                    [sg.Button('Onayla(kayıtlı olanın üzerine yazar)')],
                    [sg.Button('Kayıtlı olanı görüntüle')],
                    [sg.Button('Kayıtlı olanı Sil')]
                   ]
    tab1_layout = [ [sg.Text ( 'Kademeler Madenler(önce aşağıdan görüntüleye basın,sonra değiştirebilirsiniz)' )],
                    [sg.Text ( 'Metal, kristalden kaç kademe daha yüksek olsun?(3)\ndurdurma kodları:(99 metal)' ),sg.InputText ( size=(3, 1), key='_0' )],
                    [sg.Text ( 'Kristal, deuttan kaç kademe daha yüksek olsun?(5)\ndurdurma kodları:(99kris)(100deu+kris)(101deu)' ), sg.InputText ( size=(3, 1), key='_1' )],
                    [sg.Text ( 'Araştırma için kaçıncı gezegen kullanılacak?' ), sg.InputText ( size=(3, 1), key='_2' )],
                    [sg.Text ( 'Kademeler Tesisler' )],
                    [sg.Text ( '(Deneme sırasına göredir. Arttıramayacaksa sonrakini dener)' )],
                    [sg.Text ( 'Tesis inşaatına başlamadan kaç seviye deut madeni olsun?' ), sg.InputText ( size=(3, 1), key='_3' )],
                    [sg.Text ( 'Arastırma gezegenindeki Lab' ), sg.InputText ( size=(3, 1), key='_4' )],
                    [sg.Text ( 'Diğer gezegenlerdeki Lab' ), sg.InputText ( size=(3, 1), key='_5' )],
                    [sg.Text ( 'Robot kademeleri'), sg.InputText ( size=(3, 1), key='_6' )],
                    [sg.Text ( 'Tershane kademeleri'), sg.InputText ( size=(3, 1), key='_7' )],
                    [sg.Text ( 'Roketsilosu kademeleri'), sg.InputText ( size=(3, 1), key='_8' )],
                    [sg.Text ( 'Nanit kademeleri' ), sg.InputText ( size=(6, 1), key='_9' )],
                    [sg.ReadButton ( 'KAYDET', key='_save_' ), sg.Text ( 'Kademe hedeflerini KAYDET ve BAŞLAT' )],
                    [sg.ReadButton ( 'GÖRÜNTÜLE', key='_display_' ),sg.Text ( 'Kayıtlı olan kademe hedeflerini GETİR' )],
                    [sg.Multiline ( key='_multiline_' )]]
    tab2_layout = [[sg.Text ( 'Kademeler araştırma' )],
                    [sg.Text ( 'Bilgisayar'), sg.InputText ( size=(6, 1), key='_10' )],
                    [sg.Text ( 'Casusluk' ), sg.InputText ( size=(6, 1), key='_11' )],
                    [sg.Text ( 'Kalkan' ), sg.InputText ( size=(6, 1), key='_12' )],
                    [sg.Text ( 'Lazer' ), sg.InputText ( size=(6, 1), key='_13' )],
                    [sg.Text ( 'Enerji' ), sg.InputText ( size=(6, 1), key='_14' )],
                    [sg.Text ( 'Yanmalı motor' ), sg.InputText ( size=(6, 1), key='_15' )],
                    [sg.Text ( 'İmpuls' ), sg.InputText ( size=(6, 1), key='_16' )],
                    [sg.Text ( 'Astro'), sg.InputText ( size=(6, 1), key='_17' )],
                    [sg.Text ( 'İyon' ), sg.InputText ( size=(6, 1), key='_18' )],
                    [sg.Text ( 'Hiper uzay teknolojisi' ), sg.InputText ( size=(6, 1), key='_19' )],
                    [sg.Text ( 'Hiper uzay iticisi' ), sg.InputText ( size=(6, 1), key='_20' )],
                    [sg.Text ( 'Plazma teknolojisi' ), sg.InputText ( size=(6, 1), key='_21' )],
                    [sg.Text ( 'Gar Araştırma ağı'), sg.InputText ( size=(6, 1), key='_22' )],
                    [sg.Text ( 'Gravitasyon'), sg.InputText ( size=(6, 1), key='_23' )],
                    [sg.Text ( 'Silah tek' ), sg.InputText ( size=(6, 1), key='_24' )],
                    [sg.Text ( 'Zırh tek'), sg.InputText ( size=(6, 1), key='_25' )]]
    tab3_layout = [[sg.Text('Gemi üretimi')]
                    ,[sg.Text ( 'H.Avcı'), sg.InputText ( size=(6, 1), key='_26' )]
                    ,[sg.Text ( 'A.avcı'), sg.InputText ( size=(6, 1), key='_27' )]
                    ,[sg.Text ( 'Sonda'), sg.InputText ( size=(6, 1), key='_28' )]
                    ,[sg.Text ( 'Büyük nakliye'), sg.InputText ( size=(6, 1), key='_29' )]
                    ,[sg.Text ( 'Küçük nakliye'), sg.InputText ( size=(6, 1), key='_30' )]
                    ,[sg.Text ( 'Koloni'), sg.InputText ( size=(6, 1), key='_31' )]
                    ,[sg.Text ( 'Geri dönüşüm gemisi'), sg.InputText ( size=(6, 1), key='_32' )]
                    ,[sg.Text ( 'Solar uydu'), sg.InputText ( size=(6, 1), key='_33' )]
                    ,[sg.Text ( 'Paletli kaynak arttıran/Crawler'), sg.InputText ( size=(6, 1), key='_34' )]
                    ,[sg.Text ( 'Kruvazör'), sg.InputText ( size=(6, 1), key='_35' )]
                    ,[sg.Text ( 'Komuta'), sg.InputText ( size=(6, 1), key='_36' )]
                    ,[sg.Text ( 'Fırkateyn'), sg.InputText ( size=(6, 1), key='_37' )]
                    ,[sg.Text ( 'Bombardıman'), sg.InputText ( size=(6, 1), key='_38' )]
                    ,[sg.Text ( 'Muhrip'), sg.InputText ( size=(6, 1), key='_39' )]
                    ,[sg.Text ( 'Ölüm yıldızı'), sg.InputText ( size=(6, 1), key='_40' )]
                    ,[sg.Text ( 'Azrail/Reaper'), sg.InputText ( size=(6, 1), key='_41' )]
                    ,[sg.Text ( 'Kaşif/Pathfinder'), sg.InputText ( size=(6, 1), key='_42' )]
                    ,[sg.Text ( 'Tershane üretim şartı, Kristal kademesi'), sg.InputText ( size=(6, 1), key='_43' )]]
    tab4_layout = [[sg.Text('Savunma üretimi')],
                   [sg.Text ( 'roket atıcı' ), sg.InputText ( size=(6, 1), key='_44' )],
                   [sg.Text ( 'Hafif lazer' ), sg.InputText ( size=(6, 1), key='_45' )],
                   [sg.Text ( 'Ağır lazer' ), sg.InputText ( size=(6, 1), key='_46' )],
                   [sg.Text ( 'İyon topu' ), sg.InputText ( size=(6, 1), key='_47' )],
                   [sg.Text ( 'Gaus topu' ), sg.InputText ( size=(6, 1), key='_48' )],
                   [sg.Text ( 'Plazma topu' ), sg.InputText ( size=(6, 1), key='_49' )],
                   [sg.Text ( 'Yakalayıcı roketler' ), sg.InputText ( size=(6, 1), key='_50' )],
                   [sg.Text ( 'Gezegenler arası balistik füze' ), sg.InputText ( size=(6, 1), key='_51' )],
                   [sg.Text ( 'Büyük kalkan' ), sg.InputText ( size=(6, 1), key='_52' )],
                   [sg.Text ( 'Küçük kalkan' ), sg.InputText ( size=(6, 1), key='_53' )]]

    #key rangelevel for boxes
    #tabkeys hhere
    # The TabgGroup layout - it must contain only Tabs
    tab_group_layout = [[sg.Tab('Giriş', tab0_layout, visible=True, key='-giris-'),
                         sg.Tab('Binalar', tab1_layout,visible=False, font='Courier 15', key='-TAB1-'),
                         sg.Tab('Araştırma', tab2_layout, visible=False, key='-TAB2-'),
                         sg.Tab('Gemiler', tab3_layout, visible=False, key='-TAB3-'),
                         sg.Tab('Savunma', tab4_layout, visible=False, key='-TAB4-')
                         ]]
    # The window layout - defines the entire window
    layout = [[sg.TabGroup(tab_group_layout,
                           enable_events=True,
                           key='-TABGROUP-')],
              [sg.Text('Make tab number'), sg.Input(key='-IN-', size=(3,1)), sg.Button('Invisible'), sg.Button('Visible'), sg.Button('Select')]]
    return sg.Window ( 'Ogame bot yc', layout, no_titlebar=False )
# needs validation and try/catch error checking, will crash if blank or text entry for marks
keyrangeforlevelboxes=range(0,54)
tab_keys = ('-giris-','-TAB1-','-TAB2-','-TAB3-','-TAB4-')


def arayüz(pathname):
    global data,window,layout
    window = createwindow()
    kayıtlıdata=[]
    while True:
        button, value = window.Read ( )  # value is a dictionary holding name and marks (4)
        if button is not None:
            # initialise variables
            index = ''
            # needs validation and try/catch error checking, will crash if blank or text entry for marks

            if button == 'Kayıtlı olanı görüntüle':
                if os.path.exists ( pathname ):
                    data = [line.strip ( ) for line in open ( pathname )]
                    print('Profil bulundu.')
                    #print(data)
                    #print(type(data))
                    # create single string to display in multiline object.
                    if len(data)>=3:
                        kayıtlıdata=data
                        for i in range(0,3):
                            window[f'_giris{i}_'].update ( data[i] )

            if button == 'Onayla(kayıtlı olanın üzerine yazar)':

                f = open ( pathname, 'w' )
                #print ( value )
                for i in range(0,3):
                    index = f'_giris{i}_'
                    thedataprint = value[index]
                    print ( thedataprint, file=f )
                if len(kayıtlıdata)>3:
                    for ii in range(3,len(kayıtlıdata)):
                        print ( kayıtlıdata[ii], file=f )
                f.close ( )
                data = [line.strip ( ) for line in open ( pathname )]
                logindata=data
                window[tab_keys[0]].update ( visible=False )
                window[tab_keys[1]].update ( visible=True )
                window[tab_keys[1]].select()
                window[tab_keys[2]].update ( visible=True )
                window[tab_keys[2]].select()
                window[tab_keys[3]].update ( visible=True )
                window[tab_keys[3]].select()
                window[tab_keys[4]].update ( visible=True )
                window[tab_keys[4]].select()
                window[tab_keys[1]].select()

            if button == 'Kayıtlı olanı Sil':
                f = open ( pathname, 'w' )
                #print ( value )
                for i in range(0,3):
                    thedataprint = ''
                    print ( thedataprint, file=f )
                f.close()
                data = [line.strip ( ) for line in open ( pathname )]
                # create single string to display in multiline object.
                for i in range ( 0, 3 ):
                    window[f'_giris{i}_'].update ( data[i] )


            if button == '_save_':
                # create dictionary index _m1_ ... _m4_
                # open file and save
                f = open ( pathname, 'w' )
                #print ( value )
                for dat in range(0,3):
                    print ( logindata[dat], file=f )
                for i in keyrangeforlevelboxes:
                    index = f'_{i}'
                    thedataprint = value[index]
                    print ( thedataprint, file=f )
                f.close ( )
                window.close()

            # some error checking for missing file needed here

            if button == '_display_':
                #print(value)
                # This loads the file line by line into a list called data.
                # the strip() removes whitespaces from beginning and end of each line.
                if os.path.exists ( pathname ):
                    data = [line.strip ( ) for line in open ( pathname )]
                    # create single string to display in multiline object.
                    data=data[3::]      #giris bilgilerini atla
                    if len(data)>=1:
                        if len(data)<=len(keyrangeforlevelboxes):
                            for i in range(len(data)):
                                window[f'_{i}'].update ( data[i] )
                            window['_multiline_'].update ( data )
                        else:
                            for i in keyrangeforlevelboxes:
                                window[f'_{i}'].update ( data[i] )
                            window['_multiline_'].update ( data )
                else:
                    window['_multiline_'].update ( 'Not saved before.' )
        else:
            break



