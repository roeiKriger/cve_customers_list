import os
import json
import re
from urllib.parse import urljoin
import requests
from consts import *


# The method check the length of the url and validates it
def check_url_length(the_url, url_expected_len):
    if (url_expected_len - len(the_url)) > 1:
        print("url length is too short")
        return False
    if (url_expected_len - len(the_url)) < 0:
        print("url length is too long")
        return False
    return True


# The method check the structure of the url and validates it
def check_url_regex(the_url, regex_pattern):
    matches = re.match(regex_pattern, the_url)
    if not matches:
        print("No regex match found!")
        return False
    return True


# The method calls length check and regex check for the url, if valid returns True
def check_url_integrity(the_url, url_expected_len, regex_pattern):
    if check_url_length(the_url, url_expected_len) and check_url_regex(the_url, regex_pattern):
        print("Url is secure and valid")
        return True
    return False


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


def get_cve_monthly_links():
    # Send a GET request to the URL and fetch the page content
    response = requests.get(cve_url_list)
    page_content = response.text

    # Use regex to extract relative links starting with "CVE"
    relative_links = re.findall(r'href="/vuln/detail/(CVE-\d+-\d+)"', page_content)

    # Construct absolute URLs for the CVE links
    links = [urljoin(site_base_url, "vuln/detail/" + link) for link in relative_links]
    return links
