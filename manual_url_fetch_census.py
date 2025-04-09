import requests
import csv
import os

# Function to fetch data from a URL and return JSON
def manual_url_fetch_census(url):
    
    try:
        # Submit the API request with a timeout
        response = requests.get(url, timeout=10)  # Timeout set to 10 seconds
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
        print("Request successful!")
        print()  # Debugging: Confirm the request was successful
        return response.json()
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please check your network or try again later.")
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while fetching data: {e}")
    return None

# Function to convert JSON data to CSV
def json_to_csv(json_data, output_file):
    # Assuming the first row of JSON data contains headers
    headers = json_data[0]
    rows = json_data[1:]
    
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write headers
        writer.writerows(rows)   # Write data rows

    print(f"Data successfully written to {output_file}")
