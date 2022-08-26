# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6


# 需求 获取周杰伦的网页

import urllib.request as ur
import urllib.parse

url = 'https://www.baidu.com/s?wd='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# 进行Unicode编码
name = urllib.parse.quote('周杰伦')

url = url + name

# 请求对象的定制
request = ur.Request(url=url, headers=headers)
response = ur.urlopen(request)

# content = response.read().decode('utf-8')
content = response.readlines()

print(content)
