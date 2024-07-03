import json
from itertools import cycle

from data.common.balancer import create_summary_label, charts_statistics
from data.common.utils import convert_charts_to_json, \
    convert_json_to_chart_objects


def balance():
    with open("Bloodtypes/output.json", "r") as r:
        chart_jsons = json.loads(r.read())
        charts = convert_json_to_chart_objects(chart_jsons=chart_jsons)

        cycled_chart_types = cycle(["bar", "pie"])

        modified_charts = []

        for i in range(2, 9):
            k = 17 * (i-2)
            m = 17 * (i - 1)
            for j in range(k, m):
                chart = charts[j]
                new_chart = create_summary_label(
                    chart=chart,
                    min_labels_count=i,
                    summary_label_title="Others"
                )
                new_chart.chart_type = next(cycled_chart_types)

                modified_charts.append(new_chart)

        charts_statistics(charts=modified_charts)
        modified_charts_json = convert_charts_to_json(charts=modified_charts)

        with open("Bloodtypes/balanced_output.json", "w") as f:
            json.dump(modified_charts_json, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    balance()
