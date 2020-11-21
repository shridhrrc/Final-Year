#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:50:34 2020

@author: root
"""

from PIL import Image 
from pytesseract import image_to_string 
import pytesseract
image = Image.open('download.jpeg', mode='r')     
image_to_text = pytesseract.image_to_string(image, lang='eng')
text = ''
text=image_to_text
text1=str(text)
print(text1)