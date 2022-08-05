import pandas as pd

# 创建data
data = [
    [20, '男'],
    [22, '女'],
    [23, '女'],
    [27, '男'],
    [25, '女']
]

columns = ['年龄', '性别']
index = pd.Index(['张三', '李四', '王五', '陈六', '唐七'])
s = pd.DataFrame(data=data, index=index, columns=columns)
print(s)
print('-----------------------------')
print(s.iloc[2])
print(s.iloc[0:3]) # 含头不含尾
print(s.iloc[::2]) #步长
print(s.iloc[3,1]) #获取索引为3的行中,索引为1的列
print(s.iloc[3,0]) #获取索引为3的行中,索引为0的列
print('======================================')
print(s.loc['李四'])
print(s.loc['张三':'陈六'])#含头含尾
print(s.loc['张三'].年龄)

