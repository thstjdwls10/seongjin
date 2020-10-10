# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:46:22 2020

@author: computer
"""



# -*- coding: utf-8 -*-

"""

Created on Wed Aug 26 10:55:51 2020


@author: seongjin.son

"""


#히스토그램 그리기

import seaborn as sns

import pandas as pd

import matplotlib.pyplot as plt




se1=pd.Series([int(i) for i in df.split('\n') if i !=""],name='data')



sns.distplot(se1)


plt.show()

#

#

#

#se1.hist(bins=10, grid=False)

#

#plt.show()

#
