import requests

url = 'http://www.baidu.com'
response = requests.get(url=url)

# 一个类型和6个属性
# <class 'requests.models.Response'>
# print(type(response)) 

# 设置响应的编码格式
# response.encoding = 'utf-8'

# 返回网页源码
# print(response.text)

# 返回请求URL
# print(response.url)

# 返回的是二进制的数据  b' 开头
# print(response.content)

# 返回响应的状态码
# print(response.status_code)

# 返回响应头
print(response.headers)


