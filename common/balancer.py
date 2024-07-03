import random
from collections import defaultdict
from typing import List, Union

from common.schemas import Chart, Label


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
