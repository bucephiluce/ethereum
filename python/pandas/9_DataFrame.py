import pandas as pd

data = [
    ['张三', 20, '男', 90, 35, 67],
    ['李四', 22, '男', 100, 95, 88],
    ['王五', 23, '女', 80, 76, 67],
    ['陈六', 34, '女', 81, 77, 95],
    ['唐七', 45, '男', 66, 80, 85]
]
columns = ['name', 'age', 'gender', 'chinese', 'english', 'math']
index = pd.Index([1, 2, 3, 4, 5], name='序号')
s = pd.DataFrame(data=data, index=index, columns=columns)
print(s)
print('------------------------------------------')
print(s.sort_index(ascending=False))  # 按照index排序,默认是升序
print(s.sort_index(axis=1, ascending=False))  # 按照列索引排序,默认是降序
print('------------------------------------------')
print(s.sort_values(by='chinese')) #默认是升序
print(s.sort_values(by=['chinese','math'] , ascending=False))
print(s)
print(s.assign(total=s.chinese+s.english+s.math).sort_values(by='total',ascending=False))
print(s)
print('------------------------------------------')
print(s.chinese.nlargest(3))
print(s.chinese.nsmallest(3))
