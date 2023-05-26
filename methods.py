import os
import json
import requests
from consts import *


# The method gets the customer name, and then it concat all the parts of the API call
# (which can be changed, severity, dates and more...) then it creates the url for the GET Request
def create_url_for_api_call(customer_name):
    full_url = base_url+keyword_customer_name+customer_name+'&'+dates+'&'+cvss_severity+'&'+max_results_to_return
    return full_url


# The method read the customers JSON to an array
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


# The GET request returns a JSON, so need to read it and I save it to the project: the customer name.json
# That way if I will want to use it again I will not need to do another API call.
def read_json_from_url_create_customer_json(full_url, customer_name):
    response = requests.get(full_url)
    page_content = response.text

    # Convert page_content to a JSON object
    try:
        json_data = json.loads(page_content)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON content: {e}")
        exit(1)

    # Save the JSON object to a new JSON file
    output_filename = f"{customer_name}.json"
    output_path = os.path.join(os.path.dirname(__file__), output_filename)

    with open(output_path, "w") as file:
        json.dump(json_data, file, indent=4)

    print(f"Content saved to {output_filename}")


# Here I read and save the data I have in the JSON I created before in a variable for future use
def read_json_from_the_project_code(customer_name):
    # Define the relative file path, each time we will get the data for another customer and create json files for them
    file_path = f'cve_customers_list/{customer_name}.json'

    # Get the absolute file path of the folders
    absolute_path = os.path.join(os.getcwd(), file_path)

    with open(absolute_path, 'r') as file:
        data = json.load(file)
    return data, file_path


# From the data I have about a customer, I want to get specific information and see what the description and the
# weakness for each CVE, that way I can know how to exploit them or to patch them
def create_cve_list_for_customer(information_for_json):
    cve_list = []
    for item in information_for_json['vulnerabilities']:
        cve_item = item['cve']['id']
        description = item['cve']['descriptions'][0]['value']
        weaknesses = [weakness['description'][0]['value'] for weakness in item['cve']['weaknesses']]

        cve_dict = {
            'id': cve_item,
            'description': description,
            'weaknesses': weaknesses
        }
        cve_list.append(cve_dict)

    return cve_list


# After I collected the important information in the method above I save it to another json
def create_cve_list_json(file_path, cve_list):
    # Extract the customer name from the file path
    customer_name = os.path.splitext(os.path.basename(file_path))[0]

    # Create the output JSON file path
    output_file_path = os.path.join(os.path.dirname(file_path), f'{customer_name}_CVE.json')

    # Create the output JSON file
    output_data = {'Common Vulnerabilities': cve_list}

    with open(output_file_path, 'w') as output_file:
        json.dump(output_data, output_file, indent=4)

    print(f"{output_file_path} file has been created.")

