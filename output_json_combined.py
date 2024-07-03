import pandas as pd
import random
import json

# Load the data from the CSV files
nba_data_path = 'data/NBA/input.csv'  # Adjust the path as necessary
nba_data = pd.read_csv(nba_data_path)

cars_data_path = 'data/Cars/input.csv'  # Adjust the path as necessary
cars_data = pd.read_csv(cars_data_path)

movies_data_path = 'data/Movie/input.csv'  # Adjust the path as necessary
movies_data = pd.read_csv(movies_data_path)

# Function to check for NaN values and return valid labels and values
def get_valid_labels_and_values(data, label_column, selected_stat):
    valid_rows = data.dropna(subset=[selected_stat])
    labels = valid_rows[label_column].tolist()
    values = valid_rows[selected_stat].values.flatten().tolist()
    return labels, values

# Function to generate a single configuration with axis-specific labels and titles for NBA
def generate_chart_config_nba(data, chart_type, labels, values, selected_stats):
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
    detailed_label = f"NBA Players {stat_narrative[selected_stats[0]]}" if len(selected_stats) == 1 else "NBA Players Performance Metrics"

    chart_data = [
        {
            'label': label,
            'value': value,
            'color': f'rgba({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)}, 0.2)'
        } for label, value in zip(labels, values)
    ]

    return {
        'chart_type': chart_type,
        'chart_title': detailed_label,
        'data': chart_data
    }

# Function to generate a single configuration with axis-specific labels and titles for cars
def generate_chart_config_cars(data, chart_type, labels, values, selected_stats):
    stat_narrative = {
        'Mileage': 'Mileage (miles per gallon)',
        'HP': 'Horsepower',
        'Weight': 'Weight (lbs)',
        'Acceleration': 'Acceleration (time to speed)',
        'Price': 'Price (USD)'
    }
    detailed_label = f"Cars {stat_narrative[selected_stats[0]]}" if len(selected_stats) == 1 else "Cars Performance Metrics"

    chart_data = [
        {
            'label': label,
            'value': value,
            'color': f'rgba({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)}, 0.2)'
        } for label, value in zip(labels, values)
    ]

    return {
        'chart_type': chart_type,
        'chart_title': detailed_label,
        'data': chart_data
    }

# Function to generate a single configuration with axis-specific labels and titles for movies
def generate_chart_config_movies(data, chart_type, labels, values, selected_stats):
    detailed_label = f"Movie {selected_stats.capitalize()}"

    chart_data = [
        {
            'label': label,
            'value': value,
            'color': f'rgba({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)}, 0.2)'
        } for label, value in zip(labels, values)
    ]

    return {
        'chart_type': chart_type,
        'chart_title': f'{chart_type.capitalize()} Chart of Movie {selected_stats.capitalize()}',
        'data': chart_data
    }

# Define variables for chart types and stats columns
chart_types = ['bar', 'pie']
nba_stats_columns = ['pts', 'reb', 'ast', 'net_rating', 'oreb_pct', 'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct']
cars_stats_columns = ['Mileage', 'HP', 'Weight', 'Acceleration', 'Price']
movie_stats_columns = ['Opening', 'Total Gross', 'Theaters', 'Average']

# Generate the chart configurations
chart_data_combined = []

# Process NBA data
for chart_type in chart_types:
    for num_data_points in range(11, 13):
        for count in range(9):
            selected_rows = nba_data.sample(n=num_data_points)
            selected_stat = random.sample(nba_stats_columns, 1)[0]
            labels, values = get_valid_labels_and_values(selected_rows, 'player_name', selected_stat)
            if not labels or not values:
                continue
            chart_config = generate_chart_config_nba(selected_rows, chart_type, labels, values, [selected_stat])
            chart_data_combined.append(chart_config)

# Process cars data
for chart_type in chart_types:
    for num_data_points in range(11, 13):
        for count in range(8):
            selected_rows = cars_data.sample(n=num_data_points)
            selected_stat = random.sample(cars_stats_columns, 1)[0]
            labels, values = get_valid_labels_and_values(selected_rows, 'Car', selected_stat)
            if not labels or not values:
                continue
            chart_config = generate_chart_config_cars(selected_rows, chart_type, labels, values, [selected_stat])
            chart_data_combined.append(chart_config)

# Process movies data
for chart_type in chart_types:
    for num_data_points in range(11, 13):
        for count in range(8):
            selected_rows = movies_data.sample(n=num_data_points)
            selected_stat = random.sample(movie_stats_columns, 1)[0]
            labels, values = get_valid_labels_and_values(selected_rows, 'Release', selected_stat)
            if not labels or not values:
                continue
            chart_config = generate_chart_config_movies(selected_rows, chart_type, labels, values, selected_stat)
            chart_data_combined.append(chart_config)

# Save the combined data as JSON
output_json_path = 'output_combined1.json'
with open(output_json_path, 'w') as json_file:
    json.dump(chart_data_combined, json_file, indent=4)

print(f"Output JSON path: {output_json_path}")
