import json
import csv
import pandas as pd


def main():
    # file = pd.read_csv("bloodtypes_parsed.csv")
    # print(file.info())
    file = pd.read_csv("bloodtypes.csv")
    blood_types = file.columns[2:]
    print(file.info())
    with open("bloodtypes_parsed.csv", "w") as csv_file:
        for item in file.values[:32]:
            print(item)
            data = {
                "chart_type": "bar",
                "title": f"Blood types in {item[0]}",
                "data": [
                    {
                        "name": blood_type,
                        "quantity": round(item[1] / 100 * item[i+2]),
                        "color": "rgba(255, 99, 132, 0.2)"
                    } for i, blood_type in enumerate(blood_types)
                ]
            }
            csv_file.write(f"{json.dumps(data)};")
            csv_file.write("\n")


        for item in file.values[32:64]:
            print(item)
            data = {
                "chart_type": "pie",
                "title": f"Blood types in {item[0]}",
                "data": [
                    {
                        "name": blood_type,
                        "quantity": round(item[1] / 100 * item[i+2]),
                        "color": "rgba(255, 99, 132, 0.2)"
                    } for i, blood_type in enumerate(blood_types)
                ]
            }
            csv_file.write(f"{json.dumps(data)};")
            csv_file.write("\n")

        for item in file.values[64:]:
            print(item)
            data = {
                "chart_type": "line",
                "title": f"Blood types in {item[0]}",
                "data": [
                    {
                        "name": blood_type,
                        "quantity": round(item[1] / 100 * item[i+2]),
                        "color": "rgba(255, 99, 132, 0.2)"
                    } for i, blood_type in enumerate(blood_types)
                ]
            }
            csv_file.write(f"{json.dumps(data)};")
            csv_file.write("\n")


if __name__ == "__main__":
    main()
