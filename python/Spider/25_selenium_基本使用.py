# (1)导入selenium
from selenium import webdriver

# (2)创建浏览器操作对象
path = 'python/Spider/chromedriver.exe'

browser = webdriver.Chrome(path)

# (3)访问网站
# url = 'https://www.baidu.com'

url = 'https://www.jd.com/'
browser.get(url)

content = browser.page_source

print(content)