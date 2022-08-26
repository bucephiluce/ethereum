# urlencode应用场景:多个参数的情景

import urllib.request as ur
import urllib.parse


url = 'https://www.baidu.com/s?'
data = {
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国'
}
params = urllib.parse.urlencode(data)
url = url + params

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
# 请求对象的定制
request = ur.Request(url=url, headers=headers)
response = ur.urlopen(request)

content = response.read().decode('utf-8')

print(content)

