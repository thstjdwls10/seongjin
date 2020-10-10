# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 00:08:17 2019

@author: 82107
"""



#매크로 실행
se1=se0.split('\n')[0]

#lst=se1.split(', ')[0:10]
lst=se1.split(', ')[10:20]



lst2=[]

for i in lst:
    k=i.strip()
    lst2.append([k[0:4]]+[k[4:8]]+[k[8:12]]+[k.split('-')[1]])
    
time.sleep(3)
for i in lst2:
    for j in i:
        typer(j)
        time.sleep(0.1)
    
    
#g마켓 매크로 실행
#        
#time.sleep(3)
#for i in lst1[20:]:
#    for j in i:
#        typer(j)
#        time.sleep(0.01)
#    
#    