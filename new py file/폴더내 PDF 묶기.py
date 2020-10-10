# -*- coding: utf-8 -*-

"""

Created on Mon Jul 27 15:42:51 2020


@author: seongjin.son

"""


# 폴더 내 pdf 1개로 다 합치기

#

## -*- coding: utf-8 -*-

import sys

from os import rename, listdir

import os


import re

def sorted_alphanumeric(data):

    convert = lambda text: int(text) if text.isdigit() else text.lower()
    
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]

    return sorted(data, key=alphanum_key)


## current working directory

#print(os.getcwd())

## change directory

dirr='C:/Users/seongjin.son/Desktop/해외 MD 조사/0924 3차 사이클 초안'

os.chdir(dirr)

# current working directory

print(os.getcwd())


# 파일 목록

files = sorted_alphanumeric(listdir(dirr))

#

## 파일명에 번호 추가하기

#count = 0

#for name in files:

# new_name = name.replace( ".xlsx",'.pdf')

# #print(new_name)

# rename(name,new_name)

# count += 1




#하나로 묶기


from PyPDF2 import PdfFileWriter, PdfFileReader



import os


files = sorted_alphanumeric(listdir(dirr))


# 파일명에 번호 추가하기

output = PdfFileWriter()


for file in files:
    if '.pdf' in file:
        filename=dirr+'/'+file

        inputpdf = PdfFileReader(open(filename, "rb"))

        for i in range(inputpdf.numPages):# #뺄꺼 기입
            output.addPage(inputpdf.getPage(i))


with open( "최종.pdf", "wb") as outputStream:
    output.write(outputStream)

