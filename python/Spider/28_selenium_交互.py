
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

time.sleep(1)

# 文本框中输入'周杰伦'
input = driver.find_element(By.ID, 'kw')
input.send_keys('周杰伦')

time.sleep(1)

# 点击百度一下
button = driver.find_element(By.ID, 'su')
button.click()

time.sleep(2)

# 滑动到底部
to_bottom = 'document.documentElement.scrollTop=100000'
driver.execute_script(to_bottom)

time.sleep(2)

# 点击""下一页"
next = driver.find_element(By.XPATH, '//a[@class="n"]')
next.click()

time.sleep(2)

# 回到上一页
driver.back()

time.sleep(2)

#回到前一页
driver.forward()

time.sleep(1)
driver.quit()
