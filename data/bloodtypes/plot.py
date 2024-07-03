import json
import pandas as pd


def main():
    json_data = []

    with open("balanced_output.json", "r") as f:
        json_data = json.loads(f.read())

    df = pd.json_normalize(
        json_data,
        record_path='Bloodtypes',
        meta=['chart_type', 'chart_title']
    )


if __name__ == "__main__":
    main()
