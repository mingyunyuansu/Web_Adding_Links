import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.qtfy7.com/content-24167.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}

r = requests.get(url, headers=headers)

html_text = r.text

soup = BeautifulSoup(html_text, features='lxml')

collection = []

valid = re.compile(r"D挺好.*")
for each in soup.find_all(title=valid):
    collection.append(each['href'])
