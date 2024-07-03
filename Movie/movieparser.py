import pandas as pd
import random
import json

# Load the data from the CSV file
data_path = 'input.csv'  # Adjust the path as necessary
data = pd.read_csv(data_path)

# Function to check for NaN values and return valid labels and values
def get_valid_labels_and_values(data, selected_stat):
    valid_rows = data.dropna(subset=[selected_stat])
    labels = valid_rows['Release'].tolist()
    values = valid_rows[selected_stat].values.flatten().tolist()
    return labels, values

# Function to generate a single Chart.js configuration with axis-specific labels and titles
def generate_chart_config_movies(data, chart_type, labels, values, stat_name):
    detailed_label = f"Movie {stat_name.capitalize()}"
    config = {
        'chart_type': chart_type,
        'chart_title': f'{chart_type.capitalize()} Chart of Movie {stat_name.capitalize()}',
        'data': [
            {
                'label': label,
                'value': value,
                'color': f'rgba({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)}, 0.2)'
            } for label, value in zip(labels, values)
        ]
    }
    return config

# Define variables for chart types and stats columns
chart_types = ['bar', 'pie', 'line']
movie_stats_columns = ['Opening', 'Total Gross', 'Theaters', 'Average']

# Generate the chart configurations for the movie dataset
movie_chart_data = []
for chart_type in chart_types:
    for num_data_points in range(3, 16):
        for count in range(3):
            selected_rows = data.sample(n=num_data_points)
            selected_stat = random.sample(movie_stats_columns, 1)[0]  # Selecting one statistic for simplicity
            labels, values = get_valid_labels_and_values(selected_rows, selected_stat)
            if not labels or not values:
                continue  # Skip if there are no valid labels or values

            # Generate the chart configuration with detailed labels and titles
            chart_config = generate_chart_config_movies(selected_rows, chart_type, labels, values, selected_stat)
            movie_chart_data.append(chart_config)

# Save the data as JSON
output_json_movies_path = 'output.json'
with open(output_json_movies_path, 'w') as json_file:
    json.dump(movie_chart_data, json_file, indent=4)

print(f"Output JSON path: {output_json_movies_path}")
