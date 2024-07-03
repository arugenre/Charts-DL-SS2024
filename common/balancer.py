import json
import csv
from collections import defaultdict
from dataclasses import dataclass
from typing import List
from itertools import cycle
from pydantic import BaseModel


class Label(BaseModel):
    label: str
    value: int
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
