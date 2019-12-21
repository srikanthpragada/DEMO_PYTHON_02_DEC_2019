# Displays information about git user

import requests
import sys


def get_top_10_populous_countries(countries):
    return sorted(countries, key=lambda c: c['population'], reverse=True)[:10]


def get_countries_info():
    url = f"https://restcountries.eu/rest/v2/all"
    resp = requests.get(url)
    return resp.json()


def get_country_info(countries, code):
    for c in countries:
        if c['alpha3Code'] == code:
            return c
    else:
        return None


def show_country_info(countries, code):
    country = get_country_info(countries, code)
    if country is None:
        print("Country code not found!")
        return

    print("Name       : ", country['name'])
    print("Capital    : ", country['capital'])
    print("Population : ", country['population'])
    print("Area       : ", country['area'])
    names = []
    for code in country['borders']:
        c = get_country_info(countries, code)
        names.append(c['name'])

    print("Borders    : ", ",".join(names))


countries = get_countries_info()

for c in get_top_10_populous_countries(countries):
    print(f"{c['name']:30} - {c['population']:10d}  - {c['area']:10.0f}")
