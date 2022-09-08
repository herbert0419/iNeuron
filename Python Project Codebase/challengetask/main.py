import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://www.youtube.com/user/krishnaik06/videos'
driver.get('{}'.format(url))
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content, 'lxml')
results = soup.find("a",class_='video-title')
for title in results[:]:
    print('\n{}\t{}\t{}\thttps://www.youtube.com{}'.format(title.text))

