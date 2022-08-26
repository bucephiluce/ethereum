
import random
import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

proxies_pool = [
    {'http':'101.200.127.149:3129'},
    {'http':'101.200.127.149:3128'},
    {'http':'101.200.127.149:3127'},
    {'http':'101.200.127.149:3126'}
]

proxies = random.choice(proxies_pool)

# handler build_opener open

# (1) 获取handler对象
handler = urllib.request.ProxyHandler(proxies=proxies)

# (2) 获取opener对象
opener = urllib.request.build_opener(handler)

# (3) 调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)
