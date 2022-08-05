import pandas as pd
arr = pd.Series(data=[90,100,87,98,67],
                index=['张三','李四','王五','陈六','唐七'],
                name='成绩表',
                dtype='int32')
print(arr)
print('1.数据',arr.values)
print('2.索引',arr.index)
print('3.数据类型',arr.dtype)
print(type(arr)) #<class 'pandas.core.series.Series'>
print('4.Series的name',arr.name)
print('5.索引的名称',arr.index.name)
#设置索引的名称
arr.index.name = '姓名'
print(arr)