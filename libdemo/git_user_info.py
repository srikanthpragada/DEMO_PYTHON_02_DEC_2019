# Displays information about git user

import requests
user = "srikanthpragada"

resp = requests.get(f"https://api.github.com/users/{user}")
print(resp.status_code)
print(resp.text)
details = resp.json()   # Convert JSON to Dict
print(details['name'])
print(details['location'])
print(details['company'])
print(details['public_repos'])
