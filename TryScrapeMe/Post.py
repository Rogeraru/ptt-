#https://tryscrapeme.com/web-scraping-practice/beginner/post

import requests
import sys
from lxml import etree

url = 'https://tryscrapeme.com/web-scraping-practice/beginner/post'

response = requests.post(url)