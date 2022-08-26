import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['hz.58.com']
    start_urls = ['https://hz.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_E']

    def parse(self, response):
        # self.log(response.text)
        # self.log(response.body)
        self.log(response.xpath('//div[@id="filter"]//a/span'))
        self.log(response.xpath('//div[@id="filter"]//a/span').extract())
        self.log(response.xpath('//div[@id="filter"]//a/span').extract_first())
        
        self.log(response.xpath('//div[@id="filter"]//a/span').getall())
        self.log(response.xpath('//div[@id="filter"]//a/span').get())
