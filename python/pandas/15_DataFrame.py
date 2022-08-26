import pandas as pd
import os


print(os.getcwd()) 
print(os.curdir)
print(os.path.abspath(os.curdir))
stu = pd.read_csv(os.getcwd()+'/pandas/15_stu.txt')
print(stu)
print('----------------------------------------------')
stu1=pd.read_csv(os.getcwd()+'/pandas/15_stu.csv')
print(stu1)
print(type(stu))
print(type(stu1))
print('-------------------------------------------------')
stu2=pd.read_excel(os.getcwd()+'/pandas/stu.xlsx')
print(stu2)

