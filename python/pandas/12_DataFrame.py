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
print('---------------------------------------------------------------')
print(df.rename(columns={'name':'姓名','age':'年龄'}))
print(df)
print(df.rename(index={1:'one',2:'two'}))
print('---------------------------------------------------------------')
print(df.age.astype('object'))
df.info()
series = df.age.astype('object')
print(series)
print(series.dtype)
