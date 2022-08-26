

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver


service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

url = 'https://www.jd.com/'
driver.get(url)

driver.quit()

