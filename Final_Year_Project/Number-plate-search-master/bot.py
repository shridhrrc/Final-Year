from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
import time
#from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
#import pandas as pd
import sys
import os
import ModernStructures
try:
    sys.argv[1] != ""
    q = sys.argv[1]
except:
    q = input("Enter vehicle number: ")
class Bot:
    def __init__(self, number):
        self.number = number
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://rtovehicle.info/index.php')
        time.sleep(2)
        
        search = bot.find_element_by_id('vehiclenum')
        search.send_keys(self.number)
       
        clicker = bot.find_element_by_id('searchB')
        clicker.click()
     
        time.sleep(3)
        bot.execute_script("window.scrollTo(0, 400)")
        bot.save_screenshot("rto.png")
        
    def img_text(self):
        pytesseract.pytesseract.tesseract_cmd = r"tesseract"    
        image = Image.open('rto.png')
        image_to_text = pytesseract.image_to_string(image, lang='eng')
        text = ''
        text=image_to_text
        text1=str(text)
        #print(text)    
        D = ModernStructures.makedf(text1)
        #print(D)
        global s
        s=D
        os.system("pkill -f firefox")

    

quantin = Bot(q)
quantin.login()
key = Keys()
quantin.img_text()





from sqlalchemy import create_engine

import pymysql
import numpy as np
import pandas as pd
tableName   = "RC"

dataFrame   = s           
dataFrame = dataFrame.T
#dataFrame=(dataFrame,columns=['A', 'B', 'C', 'D'])
dataFrame.columns =['Name', 'Vehicle_name', 'Regestration_no', 'Reg_date']
dataFrame.drop(labels=None, axis=0, index=0, columns=None, level=None, inplace=True, errors='raise')
print(dataFrame)

sqlEngine       = create_engine('mysql+pymysql://root:@127.0.0.1/test', pool_recycle=3600)

dbConnection    = sqlEngine.connect()

 

try:

    frame           = dataFrame.to_sql(tableName, dbConnection, if_exists='append');

except ValueError as vx:

    print(vx)

except Exception as ex:   

    print(ex)

else:

    print("Table %s created successfully."%tableName);   

finally:

    dbConnection.close()