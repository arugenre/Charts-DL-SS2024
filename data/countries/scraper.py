import requests
from bs4 import BeautifulSoup
import json


URL = "https://www.worldometers.info/world-population/population-by-country/"


def scrape():

    response = requests.get(url=URL)
    response_content = response.content.decode(encoding="utf-8")
    bs = BeautifulSoup(markup=response_content, features="html.parser")

    trs = bs.find_all(name="tr")

    countries = []

    for tr in trs:
        tds = tr.find_all(name="td")
        if tds:
            country_name = tds[1].text
            country_population = tds[2].text
            countries.append({
                "country_name": country_name,
                "country_population": int(country_population.replace(",", ""))
            })

    with open("Countries/countries.json", "w") as f:
        json.dump(countries, f, indent=4, ensure_ascii=False)

