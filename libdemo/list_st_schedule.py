import requests
from bs4 import BeautifulSoup
import sys

resp = requests.get("http://www.srikanthtechnologies.com")
if resp.status_code != 200:
    print("Sorry! Could not retrieve details!")
    sys.exit(1)

bs = BeautifulSoup(resp.text, "html.parser")
table = bs.find("table", {'id': 'ctl00_ContentPlaceHolder1_GridView2'})

if table is None:
    print("Sorry! Could not parse document correctly!")
    sys.exit(2)

try:
    for row in table.find_all('tr')[1:]:
        course = row.find_all('td')
        print(f"{course[0].text:30} {course[2].text:10}  {course[1].text}")
except:
    print("Sorry! Error during parsing document!")
