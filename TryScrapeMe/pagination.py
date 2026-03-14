#https://tryscrapeme.com/web-scraping-practice/beginner/pagination
import time

import requests
import sys
from lxml import etree

base_url = 'https://tryscrapeme.com/web-scraping-practice/beginner/pagination'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}
lst = []

for i in range(5):
    url = base_url + '?pageno=' + str(i+1)
    response = requests.get(url, headers=headers)
    html = response.text
    root = etree.HTML(html)
    trs = root.xpath('//tr')

    for tr in trs:
        tds = tr.xpath('td')
        if len(tds) >= 4:
            price = tds[3].text
            if price != '':
                lst.append(float(price))

total = sum(lst)
print(total)

########################################

# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}
#
# def fetch_page(page_no: int) -> str:
#     url = 'https://tryscrapeme.com/web-scraping-practice/beginner/pagination'
#     page_url = f'{url}?pageno={page_no}'
#     response = requests.get(page_url, headers=headers)
#     if response.status_code != 200:
#         print('error')
#         return ''
#     return response.text
#
# if __name__ == '__main__':
#     lst = []
#     for i in range(1, 6):
#         print(i)
#         html = fetch_page(i)
#         root = etree.HTML(html)
#         trs = root.xpath('//tr')
#
#         for tr in trs:
#             tds = tr.xpath('./td')
#             if len(tds) >= 4:
#                 s = tds[3].text
#                 if s != '':
#                     price = float(s)
#                     lst.append(price)
#         time.sleep(1)
#     total = sum(lst)
#     print(total)