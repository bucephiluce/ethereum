import copy
import numpy as np

"""
np.random.seed(0);
arr1 = np.random.randint(20, size=4)
arr2 = np.arange(1,5)
print(arr1)
print(arr2)
print(arr1+arr2)
print(arr1/arr2)
print(arr1*arr2)
print(arr1//arr2)
print("---------------------------")
print(arr2**2)


lst = []
num = [2]

lst.append(num)

print(lst)
print(num)

print(id(num))
print(id(lst[0]))

num[0] = 4
print(lst)
print(num)

lst2 = []
lst2.append(copy.deepcopy(num))
print(id(num) == id(lst2[0]))

x = np.array([[1,2],[3,4],[5,6]])
print(x)
y = x[[0,1,2] , [0,1,0]]
print(y)
"""

arr1 = np.random.randint(10 , size=(2,3))
arr2 = np.random.randint(10 , size=(3,2))
print(arr1)
print(arr2)
print(arr1.dot(arr2))
print(np.dot(arr1,arr2))
