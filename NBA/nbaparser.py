import pandas as pd
import random
import json

# Load the data from the CSV file
data_path = 'input.csv'  # Make sure to replace this with your actual file path
data = pd.read_csv(data_path)

# Function to generate a single Chart.js configuration with axis-specific labels and titles
def generate_chart_config_axis_specific(data, chart_type, labels, values, selected_stats):
    # Build a detailed label describing the Y-axis based on the specific statistic being charted
    if len(selected_stats) == 1:
        stat_narrative = {
            'pts': 'Points',
            'reb': 'Rebounds',
            'ast': 'Assists',
            'net_rating': 'Net Rating',
            'oreb_pct': 'Offensive Rebound Percentage',
            'dreb_pct': 'Defensive Rebound Percentage',
            'usg_pct': 'Usage Percentage',
            'ts_pct': 'True Shooting Percentage',
            'ast_pct': 'Assist Percentage'
        }
        detailed_label = f"NBA' Players {stat_narrative[selected_stats[0]]}"
    else:
        detailed_label = "NBA' Players Performance Metrics"

    # Creating the JSON structure for Chart.js configuration
    chart_data = []
    for label, value in zip(labels, values):
        color = f'rgba({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)}, 0.2)'
        chart_data.append({
            'label': label,
            'value': value,
            'color': color
        })

    config = {
        'chart_type': chart_type,
        'chart_title': detailed_label,
        'data': chart_data
    }
    return config

# Define variables for chart types and stats columns
chart_types = ['bar', 'pie', 'line']
stats_columns = ['pts', 'reb', 'ast', 'net_rating', 'oreb_pct', 'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct']

# Generate the chart configurations
chart_data_axis_specific = []
for chart_type in chart_types:
    for num_data_points in range(3, 16):
        for count in range(3):
            selected_rows = data.sample(n=num_data_points)
            selected_stat = random.sample(stats_columns, 1)
            labels = selected_rows['player_name'].tolist()
            values = selected_rows[selected_stat].values.flatten().tolist()
            chart_config = generate_chart_config_axis_specific(selected_rows, chart_type, labels, values, selected_stat)
            chart_data_axis_specific.append(chart_config)

# Save the data as JSON
output_json_axis_specific_path = 'output.json'
with open(output_json_axis_specific_path, 'w') as json_file:
    json.dump(chart_data_axis_specific, json_file, indent=4)

print(f"Output JSON path: {output_json_axis_specific_path}")
