import numpy as np
import pandas as pd
import os

stu1 = pd.read_excel(os.getcwd()+'/pandas/stu.xlsx')
print(stu1)
print('===========================================')
print(stu1[stu1['英语'].isnull()])
print(stu1[stu1.英语.isnull()])
print(type(stu1.英语)) # <class 'pandas.core.series.Series'>
print('===========================================')
print(stu1[stu1['英语'].isnull()|stu1['数学'].isnull()])
print('===========================================')
print(stu1[stu1['数学'].notnull()])
print('===========================================')
print(stu1.dropna(subset=['英语','数学']))
print(stu1.dropna(thresh=6))
print('===========================================')
print(stu1.dropna(axis=0)) # 0表示删除含有NaN的行
print(stu1.dropna(axis=1)) # 1表示删除含有NaN的列
print('===========================================')
stu1.iloc[-1] = np.nan
print(stu1)
print(stu1.dropna(how='all'))
