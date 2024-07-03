import json
from csv import DictWriter
import pandas as pd


def main():
    file = pd.read_csv("male_female_usa.csv")

    with open("male_female_usa_parsed.csv", "w") as f:
        for i in range(0, 936, 6):
            v = file.values[i]
            data = {
                "chart_type": "pie",
                "title": f"{v[4]} {v[2].lower()} in {v[1]} in USA",
                "data": []
            }
            for j in range(i, i + 6):
                data["data"].append({
                    "name": file.values[j][3],
                    "quantity": file.values[j][6],
                    "color": "rgba(255, 99, 132, 0.2)"
                })

            f.write(f"{json.dumps(data)};")
            f.write(f"\n")


if __name__ == "__main__":
    main()
