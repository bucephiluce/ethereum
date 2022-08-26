# 1 获取百度首页
# 2 解析获取百度一下

from lxml import etree
import urllib.request

url = 'https://www.baidu.com'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

#定制请求头
request = urllib.request.Request(url=url , headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 解析网页源码
# 解析服务器的响应文件,需要etree.HTML
tree = etree.HTML(content)

#获取想要的数据
result = tree.xpath('//input[@id="su"]/@value')

print(result)
