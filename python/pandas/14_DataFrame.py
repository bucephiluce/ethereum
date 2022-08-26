import pandas as pd


data1 = [
    ['001', '赵一', 20000],
    ['002', '甄有钱', 30000],
    ['003', '周日', 20000],
    ['004', '明星', 50000],
    ['005', '高静', 10000]
]
columns1 = ['工号', '姓名', '销售业绩']
index1 = pd.Index([1, 2, 3, 4, 5], name='序号')
df1 = pd.DataFrame(data=data1, columns=columns1, index=index1)
print(df1)

data2 = [
    ['004', '明星', '小Lin奶茶店'],
    ['005', '高静', '小Lin奶茶店'],
    ['006', '周六', '小Lin奶茶店'],
    ['007', '张丽', '小Lin奶茶店'],
    ['008', '赵小二', '小Lin奶茶店']
]
columns2 = ['工号', '姓名', '公司名称']
index2 = pd.Index([6, 7, 8, 9, 10])
df2 = pd.DataFrame(data=data2, columns=columns2, index=index2)
print(df2)
print('-----------------------------------------------------')
print(pd.merge(df1,df2 , on='姓名',how='outer',suffixes=('_L','_R'))) #显示两个表中的全部数据
print('==========================================================')
print(pd.merge(df1,df2 , on='姓名',how='inner',suffixes=('_L','_R'))) #显示两个表中的共有数据
print('==========================================================')
print(pd.merge(df1,df2 , on='姓名',how='left',suffixes=('_L','_R'))) 
print('==========================================================')
print(pd.merge(df1,df2 , on='姓名',how='right',suffixes=('_L','_R'))) 

