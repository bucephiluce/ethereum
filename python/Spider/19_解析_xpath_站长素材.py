
# https://sc.chinaz.com/tag_tupian/omeimeinu.html 1
# https://sc.chinaz.com/tag_tupian/omeimeinu_2.html

# GET请求 获取站长素材前10页的欧美美女图片
# 1. 定制请求对象
# 2. 获取响应内容
# 3. 下载图片保存到本地
from lxml import etree
import urllib.request


def create_request(page):
    if page == 1 :
        url = 'https://sc.chinaz.com/tag_tupian/omeimeinu.html'
    else: 
        url = 'https://sc.chinaz.com/tag_tupian/omeimeinu_'+str(page)+'.html'

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    # 定制请求头
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_content(content):
    # 下载图片
    tree = etree.HTML(content)

    name_list = tree.xpath('//img[@class="lazy"]/@alt')

    # 一般涉及图片的网站都是对图片进行懒加载的,所以直接拿src的一般拿到的都是不是真正要拿的图片
    src_list = tree.xpath('//img[@class="lazy"]/@data-original')

    for src , name in zip(src_list, name_list):
        url = 'https:' + src
        filename = 'python/img/'+name + '.jpg'
        urllib.request.urlretrieve(url=url , filename=filename)


if __name__ == '__main__':
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    for page in range(start_page, end_page+1):
        request = create_request(page)
        content = get_content(request)
        down_content(content)


