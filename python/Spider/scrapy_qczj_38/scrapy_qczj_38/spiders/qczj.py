import scrapy


class QczjSpider(scrapy.Spider):
    name = 'qczj'
    allowed_domains = ['car.autohome.com.cn']
    # 注意: 以HTML结尾的地址,最后不能加/
    start_urls = ['https://car.autohome.com.cn/price/brand-15-29.html']

    def parse(self, response):
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        price_list = response.xpath('//span[@class="font-arial"]/text()')
        
        for name , price in zip(name_list, price_list):
            print(name.get(),price.get())

        