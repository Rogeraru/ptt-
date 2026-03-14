import requests
from lxml import etree

url = 'https://image-download.vsplay.com/activity01/M00/1F/1B/CgEPemU2UZyARQ1qAAv_stCmqi4946.jpg'

response = requests.get(url)

with open(f'./img/arkana.jpg', 'wb') as f:
    f.write(response.content)
