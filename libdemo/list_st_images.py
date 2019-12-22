import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com")
# print(resp.text)

bs = BeautifulSoup(resp.text, "html.parser")
for t in bs.find_all("img"):
    print(t['src'])

print("Anchor Tags")
for t in bs.find_all("a"):
    print(t['href'])
