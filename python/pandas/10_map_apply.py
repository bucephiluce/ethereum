import pandas as pd

lst = [11, 22, 33, 44, 55]


def fun(x):
    if x % 2:
        return x*2
    else:
        return x*3


print(list(map(fun, lst)))  # Python自带的map函数
print('--------------------------------------------------')


def fun1(x):
    if 0 <= x < 60:
        return '不及格'
    elif 60 <= x < 80:
        return '及格'
    elif 80 <= x < 90:
        return '良好'
    elif 90 <= x <= 100:
        return '优'


def fun2(x):
    if x < 40:
        return '正当壮年'
    else:
        return '苦逼中年'


data = [
    ['zhangsan', 20, '男', 90, 35, 67],
    ['lisi', 22, '男', 100, 95, 88],
    ['wangwu', 23, '女', 80, 76, 67],
    ['chenliu', 34, '女', 81, 77, 95],
    ['tangqi', 45, '男', 66, 80, 85]
]
columns = ['name', 'age', 'gender', 'chinese', 'english', 'math']
index = pd.Index([1, 2, 3, 4, 5], name='序号')
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)
print(type(df))  # <class 'pandas.core.frame.DataFrame'>
print(type(df.chinese))  # <class 'pandas.core.series.Series'>
print('--------------------------------------------------')
df['语文等级'] = df.chinese.map(fun1)
print(df)
print('---------------------apply()作用于Series上-----------------------------')
arr = pd.Series(data=[20, 30, 40, 50], index=[
                '张三', '李四', '王五', '陈六'], name='员工信息')
print(arr.apply(fun2))

print('---------------------apply()作用于DataFrame的行或者列上-----------------------------')
# 作用在每个列上 axis=0
print(df.apply(lambda x: x.max(), axis=0))
print(df[['chinese', 'english', 'math']].apply(lambda x: x.min(), axis=1))
df.info()

print('----------applymap()是DataFrame的特有方法,作用于DataFrame的每个元素上--------')
print(df.applymap(lambda x : str(x)).info())
print(df.info())






