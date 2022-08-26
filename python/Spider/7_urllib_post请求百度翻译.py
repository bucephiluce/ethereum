

#post 请求
import json
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
data={
    'kw':'spider'
}

#post请求的参数 必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

#post请求的参数 必须要进行编码
request = urllib.request.Request(url=url,data=data,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 字符串-->JSON对象
obj = json.loads(content)

print(obj)

