import scrapy

from scrapy_movie_40.items import ScrapyMovie40Item


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    def parse(self, response):

        a_list = response.xpath('//div[@class="co_content8"]//tr[2]/td[2]//a[2]')
        for a in a_list:
            name = a.xpath('./text()').get()
            href = a.xpath('./@href').get()

            url = 'https://www.ygdy8.net'+href
            
            # 对第二页地址发起访问  并且通过meta将数据传递到第二个页面
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name':name})

    def parse_second(self, response):
        # 如果拿不到数据,请检查你的xpath语法是否正确
        src = response.xpath('//div[@id="Zoom"]//img/@src').get()
        # 接受meta参数的值
        name = response.meta['name']
        movie = ScrapyMovie40Item(src=src, name=name)

        yield movie

