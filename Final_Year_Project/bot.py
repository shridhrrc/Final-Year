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
def vehicle_enum(req):    
    q = req
        #image = Image.open('download.jpeg', mode='r')     
        #image_to_text = pytesseract.image_to_string(image, lang='eng')
        #text = ''
        #text=image_to_text
        #text1=str(text)
        #q=text1
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
    dataFrame.columns =['Name', 'Vehicle_name', 'Regestration_no', 'Date','Time']
    dataFrame.drop(labels=None, axis=0, index=0, columns=None, level=None, inplace=True, errors='raise')
    dataFrame.reset_index(drop=True, inplace=True)
    dataFrame.to_string(index=False)
    print(dataFrame)

    sqlEngine       = create_engine('mysql+pymysql://root:toor@34.121.72.154/final_year', pool_recycle=3600)

    dbConnection    = sqlEngine.connect()

    

    try:

        frame           = dataFrame.to_sql(tableName, dbConnection,index=False, if_exists='append');

    except ValueError as vx:

        print(vx)

    except Exception as ex:   

        print(ex)

    else:

        print("Inserted data to %s Successfully."%tableName);   

    finally:

        dbConnection.close()
