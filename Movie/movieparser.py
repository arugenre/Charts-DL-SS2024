import pandas as pd
import random
import json

# Load the data from the CSV file
data_path = 'input.csv'  # Adjust the path as necessary
data = pd.read_csv(data_path)

# Function to generate a single Chart.js configuration with axis-specific labels and titles
def generate_chart_config_movies(data, chart_type, labels, values, stat_name):
    detailed_label = f'Movie {stat_name.capitalize()}'
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
                'text': f'{chart_type.capitalize()} Chart of Movie {stat_name.capitalize()}'
            },
            'scales': {
                'yAxes': [{'ticks': {'beginAtZero': True}}] if chart_type != 'pie' else {}
            }
        }
    }
    return json.dumps(config)

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
            labels = selected_rows['Release'].tolist()
            values = selected_rows[selected_stat].tolist()
    
            # Generate the chart configuration with detailed labels and titles
            chart_config = generate_chart_config_movies(selected_rows, chart_type, labels, values, selected_stat)
            movie_chart_data.append([chart_type, num_data_points, selected_stat, chart_config])

# Create DataFrame and save to CSV for the new dataset charts
movies_charts_df = pd.DataFrame(movie_chart_data, columns=['Chart Type', 'Data Points', 'Statistics', 'Chart Configuration'])
output_csv_movies_path = 'output.csv'
movies_charts_df.to_csv(output_csv_movies_path, index=False)

print(f"Output CSV path: {output_csv_movies_path}")
