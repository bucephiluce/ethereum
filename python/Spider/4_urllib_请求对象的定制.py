import urllib.request as ur

url = 'https://www.baidu.com'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

#请求对象的定制
request = ur.Request(url=url , headers=headers)

response = ur.urlopen(request)

content = response.read().decode('utf8')

print(content)

