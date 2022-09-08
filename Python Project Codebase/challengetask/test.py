import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.youtube.com/user/krishnaik06/videos'
driver = webdriver.Chrome()
driver.get('{}'.format(url))
content = driver.page_source.encode('utf-8').strip()
page = requests.get(url)
soup = BeautifulSoup(content, 'lxml')
results = soup.find("a", id='video-title')
print(results)