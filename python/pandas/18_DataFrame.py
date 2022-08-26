import numpy as np
import pandas as pd
import os

stu = pd.read_excel(os.getcwd()+'/pandas/stu.xlsx')
print(stu)
print(type(stu.姓名)) #<class 'pandas.core.series.Series'>
print(type(stu['姓名'])) #<class 'pandas.core.series.Series'>
print(stu['姓名'].str.find('张三'))
print(stu['姓名'].str.contains('王'))
print(stu['姓名'].str.replace('王','黄'))
print(stu['姓名'].str.len())
print(stu['姓名'].str.count('二'))
print(stu['姓名'].str.split(''))
print(stu['语文'].dtype)
print(stu['语文'].astype(str).str.extractall('(8)'))




