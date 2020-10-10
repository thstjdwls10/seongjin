


# -*- coding: utf-8 -*-

"""

Created on Fri Feb 21 15:15:23 2020


@author: seongjin.son

"""


#삼판 2월꺼

#filename1="D:/NPS 최적화작업/0608 지표확인 및 랜덤추출/raw2/(전체)DATA_삼성판매(KMAC)_20200608133356.xls"

#1.삼판

df=pd.read_excel(filename1)



df.columns=list(df.columns)[0:list(df.columns).index("판매")]+list(df.iloc[0])[list(df.columns).index("판매"):df.shape[1]+1]

df=df.iloc[1:,:]





#0. NA 제거


df["서비스 NPS"].isnull().sum()

df=df[~df["서비스 NPS"].isnull()]


print(df.shape)

size1=str(df.shape[0])


#1 품목명 변경


df["변경된품목명"]=df["품목(대)"]

df.변경된품목명.value_counts()



def yesorno(x):

if x=="예":

return True

elif x=="아니오":

return False



df['사원 당사비방']=df['사원 당사비방'].apply(lambda x : yesorno(x))

df['사원 타사추천']=df['사원 타사추천'].apply(lambda x : yesorno(x))

df['사원 잘못된정보']=df['사원 잘못된정보'].apply(lambda x : yesorno(x))


df['사원 당사비방'].value_counts()

df['사원 타사추천'].value_counts()

df['사원 잘못된정보'].value_counts()



df["디펙터여부"]= df['사원 당사비방']|df['사원 타사추천']|df['사원 잘못된정보']


df["디펙터여부"].value_counts()


#단독 확인하기

df['사원 당사비방_단독']=df['사원 당사비방']&((df['사원 타사추천']==False) & (df['사원 잘못된정보']==False))


#에어컨 제외 포함


def Airconditional(x):

if x=="에어컨":

return True

else:

return False



df['에어컨여부']=df['변경된품목명'].apply(lambda x : Airconditional(x))



df1= df[['지사', '지점', '점코드', '점', '사원', '사번', '주문번호', '조사일자', '상담원명', '판매일자',

'고객명', '모델', '변경된품목명', '활동결과', '경험 확인', '구매 확인', '서비스 NPS', '서비스 추천사유',

'서비스 추천상세', '서비스 비추천사유', '사원 NPS', '사원 추천사유', '사원 비추천사유', '재구입의향 NPS','디펙터여부',

'사원 당사비방', '사원 당사비방상세', '사원 타사추천', '사원 타사추천상세', '사원 잘못된정보',

'사원 잘못된정보상세', 'VOC', '성별', '나이', '이벤트동의','사원 당사비방_단독' ]]


df1.index=list(range(1,int(size1)+1))


#전체 NPS




def get_NPS(x):

if x.isnull().sum()>0:

print("NA 존재")

elif x.dtype == 'int64':

return round((x.value_counts()[x.value_counts().index > 8].sum()-(x.value_counts()[x.value_counts().index < 7].sum()))/(x.value_counts().sum())*100,1)

else:

se1=x.astype(int)

return round((se1.value_counts()[se1.value_counts().index > 8].sum()-(se1.value_counts()[se1.value_counts().index < 7].sum()))/(se1.value_counts().sum())*100,1)



#1) 전체 NPS


N=list(df1.shape)[0]


def rounded(s):

return round(s/N,3)


nps1=get_NPS(df1["서비스 NPS"])

nps2=get_NPS(df1["사원 NPS"])

nps3=round((nps1+nps2)/2,1)



NPS_total=pd.DataFrame()

nps_all={"비율":rounded(N),"N수":N,"전체 NPS":nps3,"서비스 NPS":nps1,"사원 NPS":nps2}

NPS_total=pd.DataFrame(pd.Series(nps_all,name='전체 NPS'))


NPS_total=NPS_total.T


NPS_total=NPS_total.append(pd.Series(name="빈칸_1"))


#2) 에어컨 제외포함(로지텍만)

#

#grouped2 = df1[["서비스 NPS","사원 NPS"]].groupby([df1['사원 당사비방_True']])

#

#NPS = grouped.agg(get_NPS)

#

#

#

#grouped2 = df1[["서비스 NPS","사원 NPS"]].groupby([df1['사원 당사비방_True']])

#

#

#NPS = grouped.agg(get_NPS)

#NPS = grouped.transform(get_NPS) #agg 로 나오는값을, 다시 전체 프레임데이터로 확대.



#2) 단독확인


grouped2 = df1[["서비스 NPS","사원 NPS"]].groupby([df1['사원 당사비방_단독']])


NPS = grouped2.agg(get_NPS)


NPS['전체']=(NPS['서비스 NPS']+NPS['사원 NPS'])/2


NPS

(94.9+93.8)/2

(96.7+93.4)/2

sum(df['사원 당사비방_단독']) / 13371





#3) 품목별 NPS

grouped_1 = df1[["서비스 NPS","사원 NPS"]].groupby([df1.변경된품목명])


NPS = grouped_1.agg(get_NPS)

NPS

product=df1["변경된품목명"].value_counts()

product.name='N수'


NPS=NPS.join(product,how='left')


NPS['전체 NPS']=round((NPS['서비스 NPS']+NPS['사원 NPS'])/2,1)


NPS['비율']=NPS['N수'].apply(lambda x : rounded(x))


NPS=NPS[['비율','N수','전체 NPS','서비스 NPS', '사원 NPS']]



list(df1.변경된품목명.value_counts().index)


NPS=NPS.loc[list(df1.변경된품목명.value_counts().index),]



NPS_total=NPS_total.append(NPS,sort=False)


NPS_total=NPS_total.append(pd.Series(name="빈칸_2"))


#지사별


grouped_2 = df1[["서비스 NPS","사원 NPS"]].groupby([df1['지사']])

NPS_2 = grouped_2.agg(get_NPS)


location=df1["지사"].value_counts()

location.name='N수'



NPS_2=NPS_2.join(location,how='left')




NPS_2['전체 NPS']=round((NPS_2['서비스 NPS']+NPS_2['사원 NPS'])/2,1)


NPS_2['비율']=NPS_2['N수'].apply(lambda x : rounded(x))


NPS_2=NPS_2[['비율','N수','전체 NPS','서비스 NPS', '사원 NPS']]



NPS_total=NPS_total.append(NPS_2,sort=False)



NPS_total=NPS_total.append(pd.Series(name="빈칸_3"))


#디펙터 별 for문

df1.columns


#k='사원 당사비방'

NPS_k_total=pd.DataFrame()

for s,k in enumerate(['디펙터여부','사원 당사비방','사원 타사추천', '사원 잘못된정보']):


grouped_k = df1[["서비스 NPS","사원 NPS"]].groupby([df1[k]],sort=True)


T=df1[k].value_counts()

T.name='N수'

NPS_k = grouped_k.agg(get_NPS)

NPS_k=NPS_k.join(T,how='left')



NPS_k['전체 NPS']=round((NPS_k['서비스 NPS']+NPS_k['사원 NPS'])/2,1)


NPS_k['비율']=NPS_k['N수'].apply(lambda x : rounded(x))



NPS_k=NPS_k[['비율','N수','전체 NPS','서비스 NPS', '사원 NPS']]


lst=[]

for i in list(NPS_k.index):

lst.append(str(k)+"_"+str(i))


NPS_k.index=lst

NPS_k_total=NPS_k_total.append(NPS_k,sort=False)

NPS_k_total=NPS_k_total.append(pd.Series(name="빈칸__"+str(s)),sort=False)




NPS_total=NPS_total.append(NPS_k_total,sort=False)


NPS_total=NPS_total.append(pd.Series(name="빈칸_4"))

NPS_total



#X 배너

NPS_defect_total=pd.DataFrame()

NPS_defect_total


lstt=['디펙터여부','사원 당사비방','사원 타사추천', '사원 잘못된정보']

df1.columns

for i,k in enumerate(lstt):

grouped_k = df1[["서비스 NPS","사원 NPS"]].groupby([df1[k],df1["변경된품목명"]],sort=True)

grouped_s = df1[["서비스 NPS","사원 NPS"]].groupby([df1[k],df1["지사"]],sort=True)


NPS_k = grouped_k.agg(get_NPS)

NPS_s = grouped_s.agg(get_NPS)


N1=grouped_k.count()["서비스 NPS"]

N1.name="N수"


N2=grouped_s.count()["서비스 NPS"]

N2.name="N수"


NPS_k=NPS_k.join(N1,how='left')

NPS_s=NPS_s.join(N2,how='left')


NPS_k['전체 NPS']=round((NPS_k['서비스 NPS']+NPS_k['사원 NPS'])/2,1)

NPS_k=NPS_k[['N수','전체 NPS','서비스 NPS', '사원 NPS']]


NPS_s['전체 NPS']=round((NPS_s['서비스 NPS']+NPS_s['사원 NPS'])/2,1)

NPS_s=NPS_s[['N수','전체 NPS','서비스 NPS', '사원 NPS']]


if i==0:

defact_data_1=NPS_k

defact_data_1_s=NPS_s

elif i==1:

defact_data_2=NPS_k

defact_data_2_s=NPS_s

elif i==2:

defact_data_3=NPS_k

defact_data_3_s=NPS_s

elif i==3:

defact_data_4=NPS_k

defact_data_4_s=NPS_s


##최종저장

savename="_".join(filename1.split("_")[0:2])+"_NPS_최종_"+size1+".xlsx"

writer = pd.ExcelWriter(savename, engine = 'xlsxwriter')


NPS_total.to_excel(writer, sheet_name = 'NPS 점수')


defact_data_1.to_excel(writer, sheet_name = '디펙터X품목',startrow=0,startcol=0)

defact_data_2.to_excel(writer, sheet_name = '디펙터X품목',startrow=0,startcol=7)

defact_data_3.to_excel(writer, sheet_name = '디펙터X품목',startrow=0,startcol=14)

defact_data_4.to_excel(writer, sheet_name = '디펙터X품목',startrow=0,startcol=21)

defact_data_1_s.to_excel(writer, sheet_name = '디펙터X지사',startrow=0,startcol=0)

defact_data_2_s.to_excel(writer, sheet_name = '디펙터X지사',startrow=0,startcol=7)

defact_data_3_s.to_excel(writer, sheet_name = '디펙터X지사',startrow=0,startcol=14)

defact_data_4_s.to_excel(writer, sheet_name = '디펙터X지사',startrow=0,startcol=21)


df1.to_excel(writer, sheet_name = 'raw_수정본')

# 포맷 만들기

workbook = writer.book

worksheet1 = writer.sheets['NPS 점수']


format1 = workbook.add_format({'num_format': '0.0%'})


worksheet1.set_column('B:B', None, format1)


worksheet2 = writer.sheets['raw_수정본']


header_format = workbook.add_format({

'bold': True,

'text_wrap': True,

'valign': 'top',

'fg_color': '#D7E4BC',

'border': 1})


# Write the column headers with the defined format.

for col_num, value in enumerate(df1.columns.values):

worksheet2.write(0, col_num + 1, value, header_format)



writer.save()

writer.close()



