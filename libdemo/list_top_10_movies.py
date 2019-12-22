# List top 10 movies of 2019 from imdb.com

import requests
from bs4 import BeautifulSoup
import sys

resp = requests.get("https://www.imdb.com/list/ls043344514/")
if resp.status_code != 200:
    print("Sorry! Could not retrieve details!")
    sys.exit(1)

bs = BeautifulSoup(resp.text, "html.parser")
movies = bs.find_all("h3", class_ = 'lister-item-header')
if movies is None or len(movies) == 0:
    print("Sorry! Could not get information about movies!")
    sys.exit(1)

for m in movies:
    title = m.find("a").text
    # print(type(m))
    # p = m.next_element    # Para that followed h3
    # p = p.next_element
    # print(type(p), p)
    # runtime = p.find_all("span",class_="runtime")
    # print(type(runtime))
    print(f"{title:40}")

