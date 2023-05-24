import os
import json


def read_customers_to_an_array():
    # Get the directory path of the current Python file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path to the JSON file
    json_file_path = os.path.join(current_dir, 'customers_list.json')

    # Read the JSON file
    with open(json_file_path) as customers_file:
        data = json.load(customers_file)

    # Extract the customer names from the JSON data
    customers = data['customers']
    return customers
