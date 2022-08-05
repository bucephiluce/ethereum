import numpy as np

# 自动转化: 字符串> 浮点类型> 整数
arr1 = np.array([11,22,33,44,'hello',55.55])
print(arr1) # ['11' '22' '33' '44' 'hello' '55.55'] 列表中有str类型的,就自动转化为str类型
arr2 = np.array([11,22,33,44,55.55])
print(arr2) # [11.   22.   33.   44.   55.55] 列表中没有str类型,就自动转化为float类型

