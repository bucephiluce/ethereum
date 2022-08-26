import pandas as pd


data = [
    ['zhangsan', 20, '男', 90, 35, 67],
    ['lisi', 22, '男', 100, 95, 88],
    ['wangwu', 23, '女', 80, 76, 67],
    ['chenliu', 34, '女', 81, 77, 95],
    ['tangqi', 45, '男', 66, 80, 85]
]
columns = ['name', 'age', 'gender', 'chinese', 'english', 'math']
index = pd.Index([1, 2, 3, 4, 5], name='序号')
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)
df2 = df.copy()
print(df2)
print(df.append(df2))
print('---------------------------------------------------------------')
print(pd.concat([df,df2]))
df.pop('chinese')
print(df)
print(df.append(df2))
print('===============================================================')
print(pd.concat([df,df2], join='inner')) #inner这种拼接方式,显示的两个表中共有列,默认方式为outer
print('-----------------------横向合并--------------------------')
print(pd.merge(df,df2 ,on='name' , how='outer',suffixes=('_L','_R')))
df=df.rename(columns={'name':'姓名'})
print(df) #两个DataFrame中列名不相同,但是内容相同时,使用left_on,和right_on
print(pd.merge(df,df2 ,left_on='姓名',right_on='name' , how='outer',suffixes=('_L','_R')))








