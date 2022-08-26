# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDangdang39Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义数据结构

    # 图片地址
    src = scrapy.Field()
    # 图书名字
    name = scrapy.Field()
    # 图书价格
    price = scrapy.Field()
