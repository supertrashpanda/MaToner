#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 21:35:26 2021

@author: lingyunfan
"""


import pypinyin 
from pypinyin import pinyin, lazy_pinyin
import re
import pygame
def make_voice(song):
    pygame.mixer.init()
    for index,i in enumerate(song):
        if index<len(song)-1:
            if i=='3' and song[index+1]=='3':#第三声连读变调
                pygame.mixer.music.load("MA2.ogg")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    pass
                continue                                                     
        if i==" ":
            pygame.time.wait(400) #a 0.4s pause
        else:
            pygame.mixer.music.load("MA" + i + ".ogg")
            pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            pass
    return None

def pronounce(speech):
    pys=pinyin(speech,style=pypinyin.TONE2)
    dic={'1':55,'2':35,'3':214,'4':51}
    tones=str()
    for i in pys:
        if any(c.isalpha() for c in i[0])==False:
            tones+=' '#pause for punctuations and spaces
        elif re.findall(r'\d+',i[0])==[]:
            tones+='0'#the zero tone
        else: tones+=re.findall(r'\d+',i[0])[0]
    print(tones)  
    make_voice(tones)
    return None
    

with open('the text.txt') as f:
    contents = f.read()
    pronounce(contents)

