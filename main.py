from methods import *
from consts import *
import requests
from bs4 import BeautifulSoup
import json
import os

customers_list = read_customers_to_an_array()
# Print the customer names
for customer in customers_list:
    print(customer)


url = 'https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=Microsoft&pubStartDate=2023-03-04T00:00:00.000&pubEndDate=2023-05-05T00:00:00.000&cvssV3Severity=CRITICAL&resultsPerPage=100'
base_url = 'https://services.nvd.nist.gov/rest/json/cves/2.0?'
keyword_customer_name = 'keywordSearch='
customer_name = 'Microsoft'
dates = 'pubStartDate=2023-03-04T00:00:00.000&pubEndDate=2023-05-05T00:00:00.000'
cvss_severity = 'cvssV3Severity=CRITICAL'
max_results_to_return = 'resultsPerPage=100'

full_url = base_url+keyword_customer_name+customer_name+'&'+dates+'&'+cvss_severity+'&'+max_results_to_return

#read_json_from_url_create_customer_json(full_url, customer_name)

# Read the input JSON file
with open(f'{customer_name}.json') as file:
    data = json.load(file)

# Extract required information and create a new JSON object
cve_list = []
for item in data['CVE_Items']:
    cve_item = item['cve']['CVE_data_meta']['ID']
    description = item['cve']['description']['description_data'][0]['value']
    weaknesses = []
    configurations = []

    if 'problemtype' in item['cve']:
        for weakness in item['cve']['problemtype']['problemtype_data']:
            weaknesses.append(weakness['description'][0]['value'])

    if 'configurations' in item['impact']:
        for configuration in item['impact']['configurations']['nodes']:
            if 'cpe_match' in configuration:
                for cpe_match in configuration['cpe_match']:
                    configurations.append(cpe_match['cpe23Uri'])

    cve_dict = {
        'id': cve_item,
        'description': description,
        'weaknesses': weaknesses,
        'configurations': configurations
    }
    cve_list.append(cve_dict)

# Create the output JSON file
output_data = {'Common Vulnerabilities': cve_list}

with open(f'{customer_name}_CVE.json', 'w') as output_file:
    json.dump(output_data, output_file, indent=4)

print(f"{customer_name}_CVE.json file has been created.")

