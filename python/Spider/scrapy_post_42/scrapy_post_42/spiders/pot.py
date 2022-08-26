import scrapy
import json

class PotSpider(scrapy.Spider):
    name = 'pot'
    allowed_domains = ['fanyi.baidu.com']
    # post请求 如果没有参数 那么这个请求将没有任何意义
    # 所以start_urls 也没有用了
    # parse 方法也没有用了
    # start_urls = ['http://fanyi.baidu.com/']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw': 'final'
        }

        yield scrapy.FormRequest(url=url, formdata=data,callback=self.after_post)

    def after_post(self, response):
        content = response.text
        obj = json.loads(content)
        print(obj)