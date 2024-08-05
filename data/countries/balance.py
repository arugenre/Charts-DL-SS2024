import json
import random
from itertools import cycle

from data.common.utils import shuffle_data

COMPLEXITY_MIN = 14
COMPLEXITY_MAX = 15
QUANTITY_PER_COMPLEXITY = 50

TITLE_SAMPLES = [
    "Population across nations",
    "Population in different countries",
    "Population distributed over countries",
    "Population spanning nations",
    "Population in various countries",
    "Population throughout countries",
    "Population among nations",
    "Population over multiple countries",
    "Population in worldwide countries",
    "Population across global nations",
    "Population across various countries",
    "Population in multiple nations",
    "Population distributed among countries",
    "Population over different nations",
    "Population spanning multiple countries",
    "Population across international borders",
    "Population in diverse countries",
    "Population among global nations",
    "Population throughout various countries",
    "Population over the world's countries",
    "Population in numerous nations",
    "Population across all countries",
    "Population among different countries",
    "Population over global countries",
    "Population spanning worldwide nations",
    "Population in countries worldwide",
    "Population among worldwide countries",
    "Population over international nations",
    "Population distributed across nations",
    "Population spanning diverse countries",
    "Population across many countries",
    "Population among numerous nations",
    "Population throughout different countries",
    "Population in a variety of countries",
    "Population across multiple nations",
    "Population over numerous countries",
    "Population spanning global nations",
    "Population distributed in countries",
    "Population across the globe's countries",
    "Population among international countries",
    "Population over a variety of nations",
    "Population throughout global countries",
    "Population in all nations",
    "Population among many countries",
    "Population distributed worldwide",
    "Population over various nations",
    "Population spanning all countries",
    "Population across different nations",
    "Population throughout numerous countries",
    "Population in global countries",
]


def balance():
    output_data = []

    with open("Countries/balanced_output.json", "r") as f:
        output_data = json.loads(f.read())

    cycled_chart_types = cycle(["bar", "pie"])

    countries = []
    with open("Countries/countries.json", "r") as f:
        countries = json.loads(f.read())

    for i in range(COMPLEXITY_MIN, COMPLEXITY_MAX + 1):
        for j in range(QUANTITY_PER_COMPLEXITY):
            shuffled_countries = shuffle_data(
                labels_length=i,
                full_data=countries
            )

            output_data.append({
                "chart_type": next(cycled_chart_types),
                "chart_title": TITLE_SAMPLES[random.randint(0, len(TITLE_SAMPLES)-1)],
                "data": [
                    {
                        "label": country["country_name"],
                        "value": country["country_population"],
                        "color": "rgba(255, 99, 132, 0.2)"
                    } for country in shuffled_countries
                ]
            })

    with open("Countries/balanced_output.json", "w") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
