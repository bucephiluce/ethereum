
# 使用urllib来获取百度首页的源码
from urllib.request import urlopen

# 定义一个url 就是你要访问的地址
url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urlopen(url)

# 获取响应中的页面源码
content = response.read().decode('utf-8')

print(content)