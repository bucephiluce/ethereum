

# 通过登录 进入到主页

# https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx

# 通过登录接口, 我们来确定需要带的参数
# __VIEWSTATE: 54ttRSZzaQw06Hj3wXBaVW4xLxDD6V68VziXhyDtBdLv/lCG0tVlicOJjIiSZYG3hV8G7dKO4iRESaQidplOAtZLLEN/Vv3ssX59ZBOmjPAdJTlEqDREq9ORmYrC/SUF3VIX5ql+uDPyT7HrWEpcw8VcczU=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 906187954@qq.com
# pwd: wzy1988456
# code: 9648
# denglu: 登录

# __VIEWSTATE __VIEWSTATEGENERATOR  code 三个变量

# 难点:(1)  __VIEWSTATE __VIEWSTATEGENERATOR 一般情况看不到的数据, 都是在页面源码中
#      (2) 验证码

# 获取登录页面的源码
from bs4 import BeautifulSoup
import requests


url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

response = requests.get(url=url, headers=headers)

content = response.text

# 解析页面源码 , 获取 __VIEWSTATE __VIEWSTATEGENERATOR

# //input[@id="__VIEWSTATE"]/@value | //input[@id="__VIEWSTATEGENERATOR"]/@value
soup = BeautifulSoup(content, 'lxml')

viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# 获取验证码图片
img_code = soup.select('#imgCode')[0].attrs.get('src')
imgcode_url = 'https://so.gushiwen.cn' + img_code

# 有坑
# 如果使用urlretrieve就会从新发起一个请求对象,这和原来的请求对象不一致
# import urllib.request
# urllib.request.urlretrieve(url=imgcode_url, filename='code.jpg')

# 解决方式就是使用session来保持同一个请求对象

session = requests.session()
response_code = session.get(imgcode_url)
# 注意图片需要用二进制进行保存
content_code = response_code.content
# 将图片保存到本地
# wb的模式就是将二进制数据写入到文件
with open('python/Spider/code.jpg', 'wb') as fp:
    fp.write(content_code)

code = input('请输入验证码:')

# 点击登陆
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '906187954@qq.com',
    'pwd': 'wzy1988',
    'code': code,
    'denglu': '登录'
}

response_post = session.post(url=url_post, data=data_post)

content_post = response_post.text

with open('python/Spider/gushiwen.html','w',encoding='utf-8') as fp:
    fp.write(content_post)
