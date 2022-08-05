import pandas as pd

#创建data
data=[
    [20,'男'],
    [22,'女'],
    [23,'女'],
    [27,'男'],
    [25,'女']
]
print(type(data))
columns=['年龄','性别']
index = pd.Index(['张三','李四','王五','陈六','唐七'])
s = pd.DataFrame(data=data,index=index,columns=columns)
print(s)
print(type(s))
print('------------------------------------')
print(s.values)
print(s.index)
print(s.columns)
#print(s[0].dtype) #这样写是会报错的,需要写成下面这样
print(s['年龄'].dtype)
print(s['性别'].dtype)
print(s.index.name)


