# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:23:04 2020

@author: computer
"""

#정규식

import re

phonenumber=re.compile(r'\d\d\d-\d\d\d') #정규식 객체로 만들기

phonenumber.search('asdfsadfsadfsadfasdfsadf 000-000').group()

# group 사용

phonenumber=re.compile(r'(\d\d\d-\d) (\d-\d\d)') #정규식 객체로 만들기

mo=phonenumber.search('asdfsadfsadfsadfasdfsadf 000-0 0-10').groups()

s1, s2= mo

print(s1,s2)

#프린트문 수정하기
'안녕%s하세여' % 100

"안녕{1:>5}하세요".format(100,"200") #1이라서 200이 뜸 오른쪽정렬 5칸뛰기

f"어찌합니까? {s1.upper()} " #중간에 함수까지 넣을수 있음
print(f"어찌합니까? {s1.upper()}")


batRegex= re.compile(r'Bat(man|mobile)') #배트맨 배트모바일 둘다 찾아줘
batRegex.search('Batman is mobile').group()

#?사용법


batRegex= re.compile(r'Bat(wo)?man') #배트맨 배트모바일 둘다 찾아줘
batRegex.search('Batwoman is mobile').group() #배트 맨도 되고 우먼도 됨 wo가 없거나 1번 나타나는 텍스트와 일치 
#*은 0개 이상과 일치, +는 1개 이상과 일치


# (ha){3} 은 ha 3번반복 (ha){3,5}는 3~5번 반복 다 





