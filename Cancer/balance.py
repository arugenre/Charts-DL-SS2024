import json
import csv
import random
from itertools import cycle
import json
import csv
from collections import defaultdict
from dataclasses import dataclass
from typing import List
from itertools import cycle
from pydantic import BaseModel

from pydantic import BaseModel


class Label(BaseModel):
    label: str
    value: float
    color: str


class Chart(BaseModel):
    chart_type: str
    chart_title: str
    data: List[Label]


def convert_json_to_chart_objects(chart_jsons: List[dict]):
    """
    takes one chart instance json
    and
    converts it to Chart object

    """
    charts = list()

    for chart_json in chart_jsons:
        chart = Chart(
            chart_title=chart_json["chart_title"],
            chart_type=chart_json["chart_type"],
            data=list()
        )

        for chart_label_json in chart_json["data"]:
            chart.data.append(
                Label(
                    label=chart_label_json["label"],
                    value=chart_label_json["value"],
                    color=chart_label_json["color"]
                )
            )

        charts.append(chart)

    return charts


def convert_charts_to_json(charts: List[Chart]):
    charts_list = list()

    for chart in charts:
        charts_list.append(chart.dict())

    return charts_list


def create_summary_label(
    *,
    chart: Chart,
    min_labels_count: int,
    summary_label_title: str
):
    if min_labels_count == len(chart.data):
        return chart

    random.shuffle(chart.data)

    rest_labels = chart.data[min_labels_count-1:]
    summary_label = Label(
        label=summary_label_title,
        value=0,
        color="rgba(255, 99, 132, 0.2)"
    )

    for label in rest_labels:
        summary_label.value += label.value

    chart.data = chart.data[:min_labels_count-1] + [summary_label]

    return chart


def charts_statistics(charts: List[Chart]):
    chart_types_count = defaultdict(int)
    labels_count = defaultdict(int)
    labels_chart_types_dist = defaultdict(lambda: defaultdict(int))

    for chart in charts:
        chart_types_count[chart.chart_type] += 1
        labels_count[len(chart.data)] += 1
        labels_chart_types_dist[chart.chart_type][len(chart.data)] += 1

    print("Chart types: ", chart_types_count)
    print("Chart labels: ", labels_count)
    print("Chart labels types distribution: ", labels_chart_types_dist)


def csv_to_json():
    charts_json = []

    with open("output.csv", "r") as f:
        reader = csv.DictReader(f, delimiter=";")

        for row in reader:
            row = row["json_file"]
            row = json.loads(row)

            chart = {
                "chart_type": row["chart_type"],
                "chart_title": row["title"],
                "data": []
            }

            for label in row["data"]:
                chart["data"].append({
                    "label": label["name"],
                    "value": label["quantity"],
                    "color": label["color"]
                })

            charts_json.append(chart)

    with open("output.json", "w") as f:
        json.dump(charts_json, f, indent=4, ensure_ascii=False)


def main():
    with open("output.json", "r") as r:
        chart_jsons = json.loads(r.read())
        charts = convert_json_to_chart_objects(chart_jsons=chart_jsons)

        charts_statistics(charts)

        cycled_chart_types = cycle(["bar", "line", "pie"])

        modified_charts = []

        for i in range(0, 8, 3):
            for j in range(i, min(8, i+3)):

                chart = charts[j]
                new_chart = create_summary_label(
                    chart=chart,
                    min_labels_count=j + 2,
                    summary_label_title="Others"
                )
                new_chart.chart_type = next(cycled_chart_types)

                modified_charts.append(new_chart)

        charts_statistics(charts=modified_charts)
        modified_charts_json = convert_charts_to_json(charts=modified_charts)

        with open("balanced_output.json", "w") as f:
            json.dump(modified_charts_json, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
