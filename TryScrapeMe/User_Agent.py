#https://tryscrapeme.com/web-scraping-practice/beginner/user-agent

import requests
import sys
from lxml import etree

url = 'https://tryscrapeme.com/web-scraping-practice/beginner/user-agent'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print('Error code:', response.status_code)
    sys.exit(1)

html = response.text
root = etree.HTML(html)
lst = []

trs = root.xpath('//tr')
for tr in trs:
    tds = tr.xpath('./td')
    if len(tds) >= 4:
        price = float(tds[3].text)
        print(price)
        lst.append(price)
avg = sum(lst) / len(lst)
print('total:', avg)

