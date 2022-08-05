import pandas as pd
import numpy as np
# 创建data
data = [
    [20, '男'],
    [22, '女'],
    [23, '女'],
    [27, '男'],
    [25, '女']
]

columns = ['年龄', '性别']
index = pd.Index(['张三', '李四', '王五', '陈六', '唐七'], name='姓名')
s = pd.DataFrame(data=data, index=index, columns=columns)
print(s)
print('------------------------------------------------')
print(s.年龄.cumsum())
print(s.性别.cumsum())
print('------------------------------------------------')
s['语文']= np.random.randint(low=50,high=100,size=5)
s['数学']= np.random.randint(low=50,high=100,size=5)
s['英语']= np.random.randint(low=50,high=100,size=5)
print(s)
print('------------------------------------------------')
print(s.describe())
print('-----------------------查看非数值列的统计指标-------------------------')
print(s.describe(include='object'))
print(s.info())
print(s.性别.value_counts())
print(s.年龄.idxmax()) #显示索引
print(s.年龄.idxmin()) #显示索引
print('------------------------------------------------')
s['语文离散化'] = pd.cut(s.语文,4,labels=['差','一般','良好','好'])
s['语文离散化'] = pd.cut(s.语文,[0,60,80,90,100],labels=['不及格','及格','良好','优秀'])
print(s)
print('------------------------------------------------')
print(pd.cut(s.年龄,[10,20,30,40,50]))



