"""
name = "小仙女长相甜美并且温柔"
# 切片 [开始:结尾:步长] 取左不取右
print(name[::-1])  # 字符串进行反转

# join函数的使用
a = "我的名字叫王哲瑜"
b = "我的工作是编写程序"
c = "我很高兴来公司工作"
seq = (a, b, c);
s = ","
d = s.join(seq);
print(d)
"""

#小数的表达
s = 3.6567
x = 5.6567

print("今天的橘子{0:.2f}一斤".format(s, x))
print("小数的百分比{:.2%}".format(0.23568))