#匿名函数
import math


def get_circle(r):        # r为形式参数
    area = math.pi*r*r    # 函数体
    return area           # 返回值
result = get_circle(2)    # 2为实际参数
print(result)
print('---------------------------------------------------')

r=2
result = lambda r:math.pi*r*r
print(result(r))
