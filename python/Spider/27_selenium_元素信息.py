
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

# 设置options
options = webdriver.ChromeOptions()
# 防止打印一些无用的日志
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
options.add_experimental_option("useAutomationExtension", False)

# 设置service
path = 'python/Spider/chromedriver.exe'
service = ChromeService(executable_path=path)

# 加载浏览器
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.baidu.com'
driver.get(url)

# 元素信息
button = driver.find_element(By.ID, 'su')
# 获取标签属性
print(button.get_attribute('class'))
# 获取标签名字
print(button.tag_name)
# 获取标签之间的内容
print(button.text) 

a = driver.find_element(By.LINK_TEXT, '新闻')
print(a.text)

time.sleep(1)
driver.quit()
