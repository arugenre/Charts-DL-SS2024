import pandas as pd
import random
import json

# Load the data from the CSV file
data_path = 'input.csv'
data = pd.read_csv(data_path)

# Function to generate a single Chart.js configuration with axis-specific labels and titles
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

    # Configuration for Chart.js
    config = {
        'type': chart_type,
        'data': {
            'labels': labels,
            'datasets': [{
                'label': detailed_label,
                'data': values,
                'backgroundColor': [
                    f'rgba({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)}, 0.2)' for _ in values
                ],
                'borderColor': [
                    f'rgba({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)}, 1)' for _ in values
                ],
                'borderWidth': 1
            }]
        },
        'options': {
            'title': {
                'display': True,
                'text': detailed_label
            },
            'scales': {
                'yAxes': [{'ticks': {'beginAtZero': True}}] if chart_type != 'pie' else {}
            }
        }
    }
    return json.dumps(config)

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
            labels = selected_rows['Car'].tolist()
            values = selected_rows[selected_stat].values.flatten().tolist()
            chart_config = generate_chart_config_axis_specific(selected_rows, chart_type, labels, values, selected_stat)
            chart_data_axis_specific.append([chart_type, num_data_points, ', '.join(selected_stat), chart_config])

# Create DataFrame and save to CSV
charts_df_axis_specific = pd.DataFrame(chart_data_axis_specific, columns=['Chart Type', 'Data Points', 'Statistics', 'Chart Configuration'])
output_csv_axis_specific_path = 'output.csv'
charts_df_axis_specific.to_csv(output_csv_axis_specific_path, index=False)

print(f"Output CSV path: {output_csv_axis_specific_path}")
