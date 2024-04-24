import pandas as pd
import random
import json

# Load the data from the CSV file
data_path = 'areaburntbywildfiresbyweeknew.csv'  # Adjust this to the path where your dataset is located
data = pd.read_csv(data_path)

# Function to generate a single Chart.js configuration with axis-specific labels and titles
def generate_chart_config_axis_specific(data, chart_type, labels, values, selected_year):
    # Build a detailed label describing the Y-axis based on the selected year
    detailed_label = f"Area burnt by wildfires in {selected_year.replace('_', ' ').capitalize()}"

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

# Define variables for chart types
chart_types = ['bar']

# Generate the chart configurations
chart_data_axis_specific = []
for _ in range(100):
    selected_year = random.choice(data.columns[3:])  # Skip first three columns (Entity, Code, Year)
    filtered_data = data[(data[selected_year].notna()) & (data[selected_year] != 0)]  # Filter out rows with NaN values or zeros for the selected year
    num_data_points = random.randint(5, 20)  # Select between 5 and 20 data points
    selected_data = filtered_data.sample(n=min(num_data_points, len(filtered_data)))  # Handle case when less than 20 rows are available
    labels = selected_data['Entity'].tolist()
    values = selected_data[selected_year].tolist()
    chart_type = random.choice(chart_types)
    chart_config = generate_chart_config_axis_specific(selected_data, chart_type, labels, values, selected_year)
    chart_data_axis_specific.append([chart_type, len(labels), selected_year, chart_config])

# Create DataFrame and save to CSV
charts_df_axis_specific = pd.DataFrame(chart_data_axis_specific, columns=['Chart Type', 'Data Points', 'Year', 'Chart Configuration'])
output_csv_axis_specific_path = 'output_wildfire_charts.csv'
charts_df_axis_specific.to_csv(output_csv_axis_specific_path, index=False)

print(f"Output CSV 1path: {output_csv_axis_specific_path}")
