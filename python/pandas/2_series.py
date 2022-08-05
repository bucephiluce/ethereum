import pandas as pd
import numpy as np
# 如果没有显示索引的时候,会采用默认索引,0到n-1
arr = pd.Series(data=np.random.randint(low=20, high=30, size=5))
print(arr)
arr.index = ['张三', '李四', '王五', '陈六', '唐七']
arr.name = '学生信息'
arr.index.name = '姓名'
print(arr)


print('-------------------关键字参数创建--------------------')
data = np.random.randint(low=20, high=30, size=5)
index = pd.Index(['张三', '李四', '王五', '陈六', '唐七'])
name = '学生信息'
print(type(data))
arr2 = pd.Series(data=data, index=index, name=name)
print(arr2)
