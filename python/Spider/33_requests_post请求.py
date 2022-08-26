import requests

url = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'eye'
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

response = requests.post(url=url, data=data, headers=headers)

import json

obj = json.loads(response.text)

print(obj)
