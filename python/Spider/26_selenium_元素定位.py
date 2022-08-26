
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

# 元素定位
# (1)根据id来找到对象
# button = driver.find_element(By.ID, 'su')
# print(button)

# (2)根据标签的属性值来获取对象
# input_name = driver.find_element(By.NAME,'wd')
# print(input_name)

# (3)根据xpath语句来获取对象
# button = driver.find_element(By.XPATH, '//input[@id="su"]')
# print(button)

# (4)根据标签的名称来获取对象
# buttons = driver.find_elements(By.TAG_NAME, 'input')
# print(buttons)

# (5)使用的bs4的语法来获取对象
# button = driver.find_element(By.CSS_SELECTOR, '#su')
# print(button)

# (6)
button = driver.find_element(By.LINK_TEXT, '地图')
print(button)

time.sleep(1)
driver.quit()
