from typing import List
import random

from data.common.schemas import Chart, Label


def convert_json_to_chart_objects(chart_jsons: List[dict]) -> List[Chart]:
    """
    takes list with dict objects
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
                    # color=chart_label_json["color"]
                    color="test"
                )
            )

        charts.append(chart)

    return charts


def convert_charts_to_json(charts: List[Chart]) -> List[dict]:
    charts_list = list()

    for chart in charts:
        charts_list.append(chart.dict())

    return charts_list


def shuffle_data(labels_length: int, full_data: list):
    """
    takes a list of objects (full_data)
    and
    returns a restricted list of size labels_length with random items from full_data
    """

    data = []

    while len(data) < labels_length:
        label = full_data[random.randint(0, len(full_data)-1)]
        if label not in data:
            data.append(label)

    return data
