# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:49:28 2020

@author: computer
"""



pdf로 변환

# -*- coding: utf-8 -*-

"""

Created on Fri Sep 25 10:25:18 2020


@author: seongjin.son

"""


#이미지 변환



import sys

from os import rename, listdir

import os


## current working directory

#print(os.getcwd())

## change directory

dirr='D:/뉴스클리핑/뉴스클리핑 2020/Insight Pick/인픽 모음'

os.chdir(dirr)

# current working directory

print(os.getcwd())


# 파일 목록

files = listdir(dirr)


from PIL import Image

for file in files:
    image1 = Image.open(file)
    im1 = image1.convert('RGB')
    im1.save(file[:-4]+'.pdf')



