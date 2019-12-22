import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(resp.text, "lxml-xml")
for item in bs.find_all("item"):
    print(item.find('title').text.strip())
    print(item.find('pubDate').text[5:17])
    print('-' * 80)
