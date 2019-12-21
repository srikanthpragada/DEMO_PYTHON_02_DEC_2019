# Displays information about git user

import requests
url = "https://restcountries.eu/rest/v2/all"

resp = requests.get(url)
countries = resp.json()

for c in countries: # list of dict
    print(f"{c['name']:50}  {c['capital']:20} {c['population']:10}  ")
