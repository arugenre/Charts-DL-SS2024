import json
from itertools import cycle

from data.common.balancer import charts_statistics, create_summary_label
from data.common.utils import convert_json_to_chart_objects, convert_charts_to_json


def balance():
    with open("Cancer/output.json", "r") as r:
        chart_jsons = json.loads(r.read())
        charts = convert_json_to_chart_objects(chart_jsons=chart_jsons)

        charts_statistics(charts)

        cycled_chart_types = cycle(["bar", "pie"])

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

        with open("Cancer/balanced_output.json", "w") as f:
            json.dump(modified_charts_json, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    balance()
