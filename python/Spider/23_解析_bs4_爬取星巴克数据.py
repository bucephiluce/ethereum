import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.starbucks.com.cn/menu/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

soup = BeautifulSoup(content, 'lxml')

# //ul[@class="grid padded-3 product"]//strong/text()
# //ul[@class="grid padded-3 product"]//div/@style

name_list = soup.select('ul[class="grid padded-3 product"] strong')
img_list = soup.select('ul[class="grid padded-3 product"] div')

for name, img in zip(name_list, img_list):
    src = 'https://www.starbucks.com.cn/'+img.attrs.get('style').split('\"')[1]
    print(name.string, src)
