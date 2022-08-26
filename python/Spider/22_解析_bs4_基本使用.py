

from bs4 import BeautifulSoup

with open('python/Spider/17_解析_xpath的基本使用.html', 'r', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'lxml')

    # 根据标签名查找节点
    # 找到第一个符合条件的数据
    # print(soup.a)
    # 获取标签的属性和属性值
    # print(soup.a.attrs)

    # bs4的一些函数
    # (1) find
    # 返回第一个符合条件的标签
    # print(soup.find('a'))
    # 根据title的值来找到对应的标签
    # print(soup.find('a', title='baidu'))

    # 根据class的值来找到对应的标签,注意的是class需要添加下划线
    # print(soup.find('a',class_='c1'))

    # (2) find_all 返回的是一个列表
    # print(soup.find_all('a'))

    # 如果想获取的是多个标签的数据,那么需要在find_all的参数中添加的是列表的数据
    # print(soup.find_all(['a','span']))

    # limit的作用是查找前几个数据
    # print(soup.find_all('li', limit=2))

    # (3) select(推荐)
    # select返回列表
    # print(soup.select('a'))

    # class类选择器
    # print(soup.select('.c1'))

    # id选择器
    # print(soup.select('#l1'))

    # 属性选择器
    # 查找到li中有id的标签
    # print(soup.select('li[id]'))
    # print(soup.select('li[id="l2"]'))

    # 层级选择器
    # 后代选择器 用""空格"
    # print(soup.select('div li'))

    # 子代选择器
    # print(soup.select('div>ul>li'))

    # 找到a标签和li标签
    # print(soup.select('a,li'))

    # 节点信息
    #    获取节点内容
    # obj = soup.select('#d1')[0]
    # 如果标签对象中 只有内容 那么string和get_text都可以
    # 如果对象中 除了内容还有标签 那么string就获取不到数据, 而get_text是可以获取数据
    # 推荐 get_text
    # print(obj.string)
    # print(obj.get_text())

    #   获取节点的属性
    obj = soup.select('#l1')[0]

    #name是标签的名字
    # print(obj.name)
    # 将属性值作为一个字典返回
    # print(obj.attrs)

    print(obj.attrs.get('class'))
    print(obj.get('class'))
    print(obj['class'])

