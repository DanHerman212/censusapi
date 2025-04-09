import requests
import csv

def fetch_census_data(year, dataset, variables, geo, api_key):
    """
    Sends an API request to the Census.gov API and retrieves the response in JSON format.

    Args:
        baseurl (str): Base URL for the Census API.
        year (str): Year of the dataset (e.g., "2018").
        dataset (str): Dataset to query (e.g., "acs/acs5").
        variables (list): List of variables to fetch (e.g., ["NAME", "B19013_001E", "B19013_001M"]).
        geo (str): Geographic query (e.g., "&for=state:*").
        api_key (str): Your Census API key.

    Returns:
        list: JSON response as a list of lists, or None if an error occurs.
    """
    # Construct the API URL
    # set condition if "group" is in the variables
    get = "?get="+",".join(variables)
    key = "&key="+api_key
    
    # set condition for product for URL construction

    url = f"https://api.census.gov/data/{year}/{dataset}{get}{geo}{key}"

    print(f"Sending request to: {url}")  # Debugging: Print the URL being requested

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

def transform_json_to_csv(data, output_file):
    """
    Transforms JSON data into a CSV file.

    Args:
        data (list): JSON response as a list of lists.
        output_file (str): Path to save the output CSV file.

    Returns:
        None
    """
    if not data:
        print("No data to transform.")
        return

    try:
        # Save data to CSV
        with open(output_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print(f"Data successfully saved to {output_file}")
    except Exception as e:
        print(f"Error writing to CSV: {e}")
