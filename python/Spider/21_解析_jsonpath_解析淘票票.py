
import json
import jsonpath
import urllib.request

# url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1661135295841_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
# (1)请求中去掉 &jsoncallback=jsonp109,返回的结果就是纯JSON格式了
# (2)可以用正则表达式来获取JSON数据
url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1661135295841_108&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    # ':authority':'dianying.taobao.com',
    # ':method':'GET',
    # ':path':'/cityAction.json?activityId&_ksTS=1661135295841_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme':'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding':'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'bx-v': '2.2.2',
    'cookie': 'enc=mn%2F4mLmx39joTeOmJ655eDcYDpikwtIAGPx3KuCwAauHNKBTUm95ebYUk7q7H6Erd4SWqBGosDL0lBszV%2FYzdQ%3D%3D; cna=pqKGGMV6Jj4CAdpsIeKGIKUy; t=913e96abb6d025aff23d888f2257fc01; cookie2=13e23d584783c3b3d2866c2ff0af9ddf; v=0; _tb_token_=67855861b19b; xlly_s=1; tfstk=cy-NBbYX2cnw1U8y8MsqhHntEeWOaU9MnkW5SbM9hg1gIbQhasxLM9q8L9WbLSbG.; l=eBSgOoQlLQ7EpahjBO5Zlurza77OCIOb8sPzaNbMiInca6tP1F189NCEgh02Rdtjgt5EUeKPUcfRbdUpoy4g7FsWHpfuKtyuJK96-e1..; isg=BGJi3yv3db-hmGge5OiToJeOs-jEs2bN8wopeKz641WAfwP5lUS13vGxr7uD795l',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('python/Spider/21_解析_jsonpath_解析淘票票.json','w', encoding='utf-8') as fp :
    fp.write(content)


with open('python/Spider/21_解析_jsonpath_解析淘票票.json','r', encoding='utf-8') as fp :

    obj = json.load(fp=fp)
    region_name_list = jsonpath.jsonpath(obj, '$..regionName')

    print(region_name_list)


