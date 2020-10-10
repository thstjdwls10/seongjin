#
###==============================================================================
### 3. 데이터 불러오기
###==============================================================================
##
##
#티몬
number=0
lst0=se0.split("\n")

se1=''.join(lst0[number:number+10])

lst=se1.split(',')
lst2=[]
for i in lst:
    lst2.append(i.replace("_20200701","").strip().split('-'))
    

time.sleep(3)
for i in lst2:
    for j in i:
        typer(j)
        time.sleep(0.35)
    typer('20200701')
    time.sleep(0.2)
    

#
#  
##위메프()

#lst1=se0.split("\n")
##len(lst1)
#
#lst2=[]
#for i in lst1:
#    if ':' in i:
#        lst2.append(i.split(':')[1].strip(" ").split('-'))
#    else:
#        lst2.append(i.split('-'))
#
#len(lst2)
#
#k=0
#
#time.sleep(3)
#for i in lst2[k:k+10]:
#    for j in i:
#        typer(j)
#        time.sleep(0.3)
#    typer('20200101')
#    time.sleep(0.3)
##
##
#
##
###   
###    
###페이코 쿠폰
##import time
##time.sleep(5)
##lst=[i.strip() for i in se1.split(',')]
##for i in lst:
##    typer(i)
##    time.sleep(0.5)
##    press("enter")
##
##len(lst)