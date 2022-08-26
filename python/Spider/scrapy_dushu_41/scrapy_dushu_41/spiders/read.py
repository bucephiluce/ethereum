import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_dushu_41.items import ScrapyDushu41Item


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    # 使用CrawlSpider有一个大坑,就是第一页的数据会因为首页地址往往被忽略掉
    start_urls = ['https://www.dushu.com/book/1188_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1188_\d+\.html'), 
                           callback='parse_item', 
                           follow=True), # follow = True 表示按照这个规则直接跟进
    )

    def parse_item(self, response):
        img_list = response.xpath('//div[@class="bookslist"]//img')
        for img in img_list:
            name = img.xpath('./@alt').get()
            src = img.xpath('./@data-original').get()

            book = ScrapyDushu41Item(name=name, src=src)
            yield book
