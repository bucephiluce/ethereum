import pandas as pd

# 创建data
data = [
    [20, '男'],
    [22, '女'],
    [23, '女'],
    [27, '男'],
    [25, '女']
]

columns = ['年龄', '性别']
index = pd.Index(['张三', '李四', '王五', '陈六', '唐七'])
s = pd.DataFrame(data=data, index=index, columns=columns)
print(s)
print('------------------------------------------------')
print(s.info())
print('------------------------------------------------')
print(s.describe())
print(s.head(3))
print(s.tail(3))
print('------------------------------------------------')
print(s.shape)
print(s.shape[0])
print(s.shape[1])
print(s.T) #不会修改原数据
s.to_csv('DF_Students.csv')
s.to_excel('DF_Students.xlsx')









