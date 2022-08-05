"""
    安装扩展库numpy scipy matplotlib 
    安装命令 pip install numpy scipy matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
    更新命令 python -m pip install -U pycodestyle setuptools -i https://pypi.tuna.tsinghua.edu.cn/simple
    pip list -o
"""
import numpy as np
import sys

#创建一维数组
lst = [11, 22, 33]
print(type(lst), lst)
arr1 = np.array(lst)
print(type(arr1), arr1)

print('------------------------------')

# Python中的列表,可以存储任意对象,所以在列表中存的是对象的指针
lst2 = ['hello', False, 90, 87.6]
for item in lst2:
    print(repr(item).ljust(10), repr(id(item)).ljust(20), repr(sys.getsizeof(id(item))).ljust(10))

#创建二维数组
lst3 = [[11,22,33],[44,55,66],[77,88,99]]
arr2 = np.array(lst3)
print(type(arr2), arr2)