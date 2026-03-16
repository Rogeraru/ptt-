#https://tryscrapeme.com/web-scraping-practice/beginner/iframe

import requests
import sys
from lxml import etree

url = 'https://tryscrapeme.com/web-scraping-practice/beginner/iframe-data'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print('Error code:', response.status_code)
    sys.exit()

html = response.text
root = etree.HTML(html)
trs = root.xpath('//tr')
lst = []

for tr in trs:
    tds = tr.xpath('td')
    if len(tds) >= 4:
        s = tds[3].text
        if s != '':
            price = float(s)
            lst.append(price)
total = sum(lst)
avg = total / len(lst)
print(avg)
