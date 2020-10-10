# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:18:40 2018

@author: user
"""

#셀레니엄으로 인스타 스크립핑하기

    
from selenium import webdriver

path="C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(path)


driver.get('https://www.instagram.com/accounts/login/')

driver.find_element_by_name("username").send_keys('thstjdwls10@naver.com')

driver.find_element_by_name("password").send_keys('152godwjd1!')

driver.find_element_by_name("password").submit()

def insta_input(text):
    elem=driver.find_element_by_tag_name('input')
    
    
    elem.clear() #값을지움
    elem.send_keys(text) #검색어 입력
    elem.click() #검색실행
    time.sleep(3)
    html = driver.page_source #소스전부가져오기
    return html

insta_input('#하나은행')

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')




import nltk
from nltk.corpus import stopwords
from collections import Counter
import networkx as nx
import itertools
import pickle
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import time
import re


import csv    
f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(['카테고리','대표단어','유사어','인스타 게시물 수'])

s1=dict([(i.split('게시물')[0].strip(),i.split('게시물')[1]) for i in soup.find('div',class_="_dv59m").text.split('#') if (i!="" and int(i.split('게시물')[1].replace(',',''))>9)])
i=soup.find('div',class_="_dv59m").text.split('#')[1]

for k in s1.items():
    wr.writerow(['anniversary',list(s1.keys())[0], k[0], int(k[1].replace(',',''))])

f.close()

