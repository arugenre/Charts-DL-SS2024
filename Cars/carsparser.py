import pandas as pd
import random
import json

# Load the data from the CSV file
data_path = 'input.csv'
data = pd.read_csv(data_path)

# Function to check for NaN values and return valid labels and values
def get_valid_labels_and_values(data, selected_stat):
    valid_rows = data.dropna(subset=selected_stat)
    labels = valid_rows['Car'].tolist()
    values = valid_rows[selected_stat].values.flatten().tolist()
    return labels, values

# Function to generate a single configuration with axis-specific labels and titles
def generate_chart_config_axis_specific(data, chart_type, labels, values, selected_stats):
    # Map of car statistics for detailed label generation
    stat_narrative = {
        'Mileage': 'Mileage (miles per gallon)',
        'HP': 'Horsepower',
        'Weight': 'Weight (lbs)',
        'Acceleration': 'Acceleration (time to speed)',
        'Price': 'Price (USD)'
    }
    detailed_label = f"Cars' {stat_narrative[selected_stats[0]]}" if len(selected_stats) == 1 else "Cars' performance Metrics"

    # Creating the JSON structure
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
chart_types = ['bar', 'line', 'pie']
stats_columns = ['Mileage', 'HP', 'Weight', 'Acceleration', 'Price']

# Generate the chart configurations
chart_data_axis_specific = []
for chart_type in chart_types:
    for num_data_points in range(3, 16):
        for count in range(3):
            selected_rows = data.sample(n=num_data_points)
            selected_stat = random.sample(stats_columns, 1)
            labels, values = get_valid_labels_and_values(selected_rows, selected_stat)
            if len(labels) == 0 or len(values) == 0:
                continue
            chart_config = generate_chart_config_axis_specific(selected_rows, chart_type, labels, values, selected_stat)
            chart_data_axis_specific.append(chart_config)

# Save the data as JSON
output_json_axis_specific_path = 'output.json'
with open(output_json_axis_specific_path, 'w') as json_file:
    json.dump(chart_data_axis_specific, json_file, indent=4)

print(f"Output JSON path: {output_json_axis_specific_path}")
