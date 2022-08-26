from lxml import etree


# xpath解析
# (1) 本地文件           etree.parse
# (2) 服务器响应的数据    etree.HTML

# xpath来解析本地文件
tree = etree.parse('python/Spider/17_解析_xpath的基本使用.html')

# tree.xpath('xpath路径')

#查找ul下面的li
# li_list = tree.xpath('//body/ul/li')

#查找所有有id属性的li标签
#text() 获取标签中的内容
# li_list = tree.xpath('//ul/li[@id]/text()')
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')

# 查找到id为l1的li标签的class的属性值
# li_list = tree.xpath('//ul/li[@id="l1"]/@class')

# 查询id中包含l的li标签
# li_list = tree.xpath('//ul/li[contains(@id, "l")]/text()')

# 查询id中以l开头的li标签
# li_list = tree.xpath('//ul/li[starts-with(@id, "l")]/text()')

# 查询id和class的and操作
# li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')

# | 这个操作不能对属性进行,需要对元素进行操作,需要注意
# li_list = tree.xpath('//ul/li[@id="l1" | @id="l2"]/text()') # 报错
li_list = tree.xpath('//ul/li[@id="l1" or @id="l2"]/text()') # 这样是可以的
# li_list = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()') # 这样也是可以的

print(li_list)
print(len(li_list))