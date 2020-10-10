# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:42:10 2020

@author: computer
"""


# -*- coding: utf-8 -*-

"""

Created on Mon Jul 27 15:51:04 2020


@author: seongjin.son

"""


#pdf 필요한것만 따기


from PyPDF2 import PdfFileWriter, PdfFileReader



import os

dirr='D:/뉴스클리핑/뉴스클리핑 2020/7월 뉴스클리핑 일별 스크랩'

os.chdir(dirr)

print(os.getcwd())


files = listdir(dirr)



filename="[CMI]뉴스클리핑(W31, 8월10일)_수정전.pdf"

inputpdf = PdfFileReader(open(filename, "rb"))



output = PdfFileWriter()

for i in range(inputpdf.numPages):#[1,0,2,3,4,5,6,7,8,9,10,11]:# #뺄꺼 기입
    if i not in [6,10]: #0부터 시작임... 체크 잘할것.
        output.addPage(inputpdf.getPage(i))


with open( filename.replace('_수정전.pdf','.pdf'), "wb") as outputStream:

    output.write(outputStream)



#

##낮장으로 떼기

#from PyPDF2 import PdfFileWriter, PdfFileReader

#

#inputpdf = PdfFileReader(open("document.pdf", "rb"))

#

#for i in range(inputpdf.numPages):

# output = PdfFileWriter()

# output.addPage(inputpdf.getPage(i))

# with open("document-page%s.pdf" % i, "wb") as outputStream:

# output.write(outputStream)

