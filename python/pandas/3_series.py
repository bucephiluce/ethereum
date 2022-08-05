import pandas as pd
import numpy as np

index = pd.Index(['张三','李四','王五','陈六','唐七'] , name='姓名')
arr1=pd.Series(data=[23,24,25,22,27] , name='学生信息')
print(arr1)
print(arr1[0]) #根据索引获取元素
#添加显示索引
arr1.index = index
print(arr1)
print(arr1['张三']) #有点类似Python基础语法中的字典key=>value
print(arr1.张三)
print(arr1.get('张三'))
print(arr1.get('Tom','查无此人')) # 不会报错
print('-------------------切片操作----------------------')
print(arr1[0:3]) #含头不含尾
print(arr1[0:3:2])
print(arr1['张三':'王五']) #显示索引,切片,含头含尾
print(arr1[['张三','王五']]) #数据提取
print('------提取数据时进行判断[提取符合要求的数据]-----')
print(arr1[arr1 < 25])

print('------广播方式计算-----')
print(arr1+1)
print('统计计算')
print('平均值:',arr1.mean())
print('平均值:',np.mean(arr1))
print('最大值:',np.max(arr1))

