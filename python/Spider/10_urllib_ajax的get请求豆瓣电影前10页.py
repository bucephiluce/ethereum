# https://movie.douban.com/j/chart/top_list?type=1&interval_id=100:90&action=&
# start=0&limit=20

# https://movie.douban.com/j/chart/top_list?type=1&interval_id=100:90&action=&
# start=20&limit=20

# page 1 2 3 4
# start 0 20 40 60
# start = (page - 1) * 20

# get请求 获取豆瓣电影 前5页数据
# 1. 定制请求对象
# 2. 获取响应内容
# 3. 下载内容保存到本地
import urllib.parse
import urllib.request


def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=1&interval_id=100:90&action=&'
    data = {
        'start': (page - 1)*20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data)
    url = base_url+data
    headers = {
        'Accept': '*/*',
        # 'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'douban-fav-remind=1; gr_user_id=d8812056-2b0d-47fe-adde-5f1d079e6938; viewed="27620886_2239755"; bid=iU-hf_CPFxA; ll="118172"; _vwo_uuid_v2=DBB3D129CDB37C4427B4A8DA597504E72|1c4993990991984b6ed43db43c09ac06; ap_v=0,6.0; __utma=30149280.792025846.1524716210.1658988628.1660717809.29; __utmb=30149280.0.10.1660717809; __utmc=30149280; __utmz=30149280.1660717809.29.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.550568118.1534922283.1658988628.1660717809.10; __utmb=223695111.0.10.1660717809; __utmc=223695111; __utmz=223695111.1660717809.10.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1660717809%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dc7WJ0fNNDKHEyMoXoxhVZUAKOO82dyzN7Z-F9hXDm3wqqrfsjcTiDLNgH0VTKhjQ%26wd%3D%26eqid%3Dde53f175000840580000000362fc8aee%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=bcf3bee3d78b8547.1534922283.10.1660718962.1658988628.',
        'Host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com/typerank?type_name=%E7%BA%AA%E5%BD%95%E7%89%87&type=1&interval_id=100:90&action=',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    # 定制请求头
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_content(page, content):
    with open(f'douban_{page}.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始页:'))
    end_page = int(input('请输入终止页:'))
    for page in range(start_page, end_page+1):
        request = create_request(page)
        content = get_content(request)
        down_content(page, content)
