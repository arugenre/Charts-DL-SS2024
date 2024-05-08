import json
from csv import DictWriter
import pandas as pd


def main():
    file = pd.read_csv("cancer_data.csv")

    cancer_type = file["cancer_type"]

    with open("cancer_parsed.csv", "w") as f:
        for col in file.columns[1:]:
            curr_data = {
                "chart_type": "line",
                "title": f"Rank of new cases among each cancer type in 2020",
                "data": []
            }
            for i, value in enumerate(file[col]):

                curr_data["title"] = col
                curr_data["data"].append({
                    "name": cancer_type[i],
                    "quantity": value,
                    "color": "rgba(255, 99, 132, 0.2)"
                })
            f.write(f"{json.dumps(curr_data)};")
            f.write("\n")


if __name__ == "__main__":
    main()
