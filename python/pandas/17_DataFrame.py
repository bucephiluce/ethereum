import numpy as np
import pandas as pd
import os

stu1 = pd.read_excel(os.getcwd()+'/pandas/stu.xlsx')
print(stu1)
print('--------------1.填充固定值----------------')
print(stu1['英语'].fillna(0))
print('--------------2.根据前一个值进行填充----------------')
print(stu1['英语'].fillna(method='pad'))
print(stu1['英语'].fillna(method='ffill'))
print('--------------3.根据后一个值进行填充----------------')
print(stu1['英语'].fillna(method='bfill'))
print(stu1['英语'].fillna(method='backfill'))
print('---------------------------------------------')
print(stu1.replace('不知道', '男'))
print(stu1)
