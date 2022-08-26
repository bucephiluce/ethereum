from urllib.request import urlopen

url = 'http://www.baidu.com'

response = urlopen(url)

# 一个类型和六个方法
# <class 'http.client.HTTPResponse'>
# print(type(response)) 

# 按照一个字节一个字节的去读
# content = response.read()

# 返回多少字节
# content = response.read(300)
# print(content)

#读取一行
# content = response.readline()

#读取所有内容
# content = response.readlines()
# print(content)

# 返回状态码
# print(response.getcode())

#返回URL地址
print(response.geturl())

# 获取状态信息
print(response.getheaders())



