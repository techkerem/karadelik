from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import ctypes
import os
import random

from gtts import gTTS
from playsound import playsound
import selenium
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

number = 1
mem = 0

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://countik.com/video/7140651034711510273"
driver.get(URL)
time.sleep(10)


ln=1
while ln<10:


    time.sleep(1)
    #hata verirse chrome da kaynagi incele tusuna basip takipci sayiniza tiklayin ve copy full path diyip assagiya ekleyin
    izlenme = driver.find_element("xpath", '/html/body/div/div/section/section/section[1]/div[2]/div/div[1]/div/span/h5').text

    view=izlenme.replace(",","")

    artis = int(view)-int(mem)

    while artis > 0:
            img = Image.open("output.jpg", 'r')

            x = random.randrange(1,3440)
            y= random.randrange(1,1440)

            img.putpixel((x,y), (0,0,0))
            time.sleep(1)
            img.save("output.jpg")

            print(number)
            number = number + 1
            # ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\Dell\\Desktop\\tt2\\tt\\output.jpg" , 0)

            artis=artis-1


    mem = view
