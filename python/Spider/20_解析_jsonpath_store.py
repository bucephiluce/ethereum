
import json
import jsonpath

with open('python/Spider/20_解析_jsonpath_store.json', 'r', encoding='utf-8') as fp:

    obj = json.load(fp=fp)

    # 获取书店所有书的作者
    # author_list = jsonpath.jsonpath(obj=obj,expr='$.store.book[*].author')
    # print(author_list)

    # 所有作者
    # author_list = jsonpath.jsonpath(obj=obj, expr='$..author')
    # print(author_list)

    # store的所有元素。所有的bookst和bicycle
    # tag_list = jsonpath.jsonpath(obj=obj, expr='$.store.*')
    # print(tag_list)

    # store里面所有东西的price
    # price_list = jsonpath.jsonpath(obj, '$.store..price')
    # print(price_list)

    # 第三个书
    # book = jsonpath.jsonpath(obj, '$..book[2]')
    # print(book)

    # 最后一本书
    # book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]') # ()脚本表达式，使用在脚本引擎下面。
    # print(book)

    # 前面的两本书。
    # book_list = jsonpath.jsonpath(obj, '$..book[0,1]')
    # book_list = jsonpath.jsonpath(obj, '$..book[:2]')
    # print(book_list)

    # 过滤出所有的包含isbn的书。
    # book_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]') # ?() 应用过滤表示式
    # print(book_list)

    # 过滤出价格低于10的书。
    # book_list = jsonpath.jsonpath(obj, '$..book[?(@.price<10)]')
    # print(book_list)

    # 所有元素。
    all_elements = jsonpath.jsonpath(obj, '$..*')
    print(all_elements)
