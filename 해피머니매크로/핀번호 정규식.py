# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:35:43 2020

@author: 82107
"""

import re

lst1=[]

p = re.compile(r'교환권번호:\d+-\d+-\d+-\d+')
len(p.findall(se1))

for i in p.findall(se1):
    print(i.strip("교환권번호:").replace('-',''))


#컬쳐랜드 지마켓

p = re.compile(r'\) \d+-\d+-\d+-\d+')
len(p.findall(se0))

lst1=[i.strip(') ').replace('-','') for i in p.findall(se0)]
    
    


import re
import copy
lst1=[]

p = re.compile('티켓번호 : \d+')
len(p.findall(se1))



for i in p.findall(se1):
    lst1.append(i.strip("티켓번호 : "))
    print(i.strip("티켓번호 : "))

for i in lst2:
    print(i)
lst2=copy.deepcopy(lst1)

len(lst1)
lst1

for i in lst1:
    print(i)




import re
lst1=[]
p = re.compile(r'상품권번호 : \d+-\d+-\d+')
len(p.findall(se1))


len(lst1)

lst1=[]

for i in p.findall(se1):
    lst1.append(i.replace('상품권번호 : ',"").replace('-',""))

import re
lst1=[]
p = re.compile(r'핀번호: \d+-\d+-\d+-\d+')
len(p.findall(se1))


len(lst1)

lst1=[]

for i in p.findall(se1):
    lst1.append(i.replace('핀번호: ',""))



import re
p = re.compile(r'쿠폰번호 : \d+')
len(p.findall(se0))


lst1=[]

for i in p.findall(se0):
    lst1.append(i.replace('쿠폰번호 : ' ,""))

ke1="""999816179758
999906209901
999223358608
999314707089
999835978269"""

ke2=ke1.split('\n')

lst1=lst1+ke2
