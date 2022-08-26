import scrapy

from scrapy_dangdang_39.items import ScrapyDangdang39Item


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']

# http://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
# http://category.dangdang.com/pg3-cp01.01.02.00.00.00.html
# http://category.dangdang.com/pg4-cp01.01.02.00.00.00.html
    base_url = 'http://category.dangdang.com/pg'
    page = 1


    def parse(self, response):

        # pipelines 下载数据
        # items     定义数据结构的
        # src = //ul[@id="component_59"]/li//img/@src
        # alt = //ul[@id="component_59"]/li//img/@alt
        # price = //ul[@id="component_59"]/li/p[@class="price"]/span[1]/text()
        # 所有的selector的对象 都可以再次调用xpath方法
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            src = li.xpath('.//img/@data-original').get() # 图片处理需要进行懒加载处理
            # 第一张图片的属性和其他的不一样,所以需要判断
            # if src:
            #     pass
            # else:
            #     src = li.xpath('.//img/@src').get() 
            # 第二种写法
            if not src:
                src = li.xpath('.//img/@src').get() 

            name = li.xpath('.//img/@alt').get()
            price = li.xpath('./p[@class="price"]/span[1]/text()').get()

            book = ScrapyDangdang39Item(src=src, name=name, price=price)

            # 获取一个book就将book交给pipelines
            yield book
        
        if self.page < 3:
            self.page +=1
            url = self.base_url+str(self.page)+'-cp01.01.02.00.00.00.html'

            # 怎么去调用parse方法
            # scrapy.Request就是scrapy的get请求
            # url就是请求地址
            # callback就是你要执行的那个函数, 注意函数不能加()
            yield scrapy.Request(url=url, callback=self.parse)

