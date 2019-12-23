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
    para = m.find_next("p")
    div = m.find_next("div")
    rating = div.find("span",class_="ipl-rating-star__rating").text
    runtime = para.find("span",class_="runtime").text
    genre = para.find("span", class_="genre").text.strip(' \n')
    print(f"{title:40} - {runtime:10}  - {genre:30}  - {rating}")
