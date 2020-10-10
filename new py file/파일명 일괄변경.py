

# -*- coding: utf-8 -*-

"""

Created on Mon Jul 27 15:42:51 2020


@author: seongjin.son

"""


#파일명 일괄변경


# -*- coding: utf-8 -*-

import sys

from os import rename, listdir

import os


# current working directory

print(os.getcwd())

# change directory

dirr='D:/뉴스클리핑/뉴스클리핑 2020/7월 뉴스클리핑 일별 스크랩'

os.chdir(dirr)

# current working directory

print(os.getcwd())


# 파일 목록

files = listdir(dirr)


# 파일명에 일괄로 확장자 바꾸기

count = 0

for name in files:

new_name = name.replace( ".xlsx",".pdf")

#print(new_name)

rename(name,new_name)

count += 1



#파일명에 숫자붙이기

files = sorted_alphanumeric(listdir(dirr))

count = 0

for name in files:

new_name = name.strip('1234567890.')

#print(new_name)

rename(name,str(count+1)+'.'+new_name)

count += 1




#파일명에 숫자 없애기

files = sorted_alphanumeric(listdir(dirr))

for name in files:

new_name = name.strip('1234567890.')

rename(name,new_name)



import re

def sorted_alphanumeric(data):

convert = lambda text: int(text) if text.isdigit() else text.lower()

alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]

return sorted(data, key=alphanum_key)