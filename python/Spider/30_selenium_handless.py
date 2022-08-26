
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

# 设置options
options = webdriver.ChromeOptions()
# 防止打印一些无用的日志
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
options.add_experimental_option("useAutomationExtension", False)
# 设置无头的选项
# options.headless = True
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

# 设置service
path = 'python/Spider/chromedriver.exe'
service = ChromeService(executable_path=path)

# 加载浏览器
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.baidu.com'
driver.get(url)
driver.save_screenshot('python/baidu.png')

time.sleep(1)
driver.quit()
