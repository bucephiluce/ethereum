# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib.request
from itemadapter import ItemAdapter

# 如果想要使用管道的话 那么就必须在settings中开启管道


class ScrapyDangdang39Pipeline:

    # 在爬虫文件执行完之前  执行的方法
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    # item就是yield后面的book对象
    def process_item(self, item, spider):

        # (1) write方法必须要接受一个字符串 而不能是其他对象
        # (2) w模式 会为每一个对象重新打开一次文件 覆盖之前的内容
        # (3) 这样的模式不推荐 进行了太多的IO操作
        # with open('book.json','a',encoding='utf-8') as fp:
        #     fp.write(str(item))
        self.fp.write(str(item))

        return item

    # 在爬虫文件执行完之后  执行的方法
    def close_spider(self, spider):
        self.fp.close()


# 开启多条管道
# (1) 定义管道类
# (2) 在settings中开启管道


class DangDangDownloadPipeline:
    
    def process_item(self, item, spider):

        url = 'http:'+item.get('src')
        filename = 'books/'+item.get('name')+'.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)

        return item
