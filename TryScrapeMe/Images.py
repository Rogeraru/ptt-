#https://tryscrapeme.com/web-scraping-practice/beginner/images
import hashlib
import requests
import sys
from lxml import etree

url = 'https://tryscrapeme.com/web-scraping-practice/beginner/images'
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}
response = requests.get(url, headers = headers)

if response.status_code != 200:
    print(f'error, status code: {response.status_code}')
    exit()

html = response.text
root = etree.HTML(html)
srcs = root.xpath('//img/@src')

for src in srcs:
    if 'gzybck.jpg' in src:
        #download img
        result = requests.get(src, headers = headers)
        if result.status_code != 200:
            print(f'error, status code: {result.status_code}')
            exit()
        md5_hash = (hashlib.md5(result.content).hexdigest()).lower()
        break

print(md5_hash)
