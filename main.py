from methods import *
from consts import *

customers_list = read_customers_to_an_array()
# Print the customer names
for customer in customers_list:
    print(customer)
check_url_integrity(cve_url_list, url_len, regex_rule_for_url)


import re
import requests
from urllib.parse import urljoin


# Send a GET request to the URL and fetch the page content
response = requests.get(cve_url_list)
page_content = response.text

# Use regex to extract relative links starting with "CVE"
relative_links = re.findall(r'href="/vuln/detail/(CVE-\d+-\d+)"', page_content)

# Construct absolute URLs for the CVE links
base_url = "https://nvd.nist.gov"
links = [urljoin(base_url, "vuln/detail/" + link) for link in relative_links]

# Fetch the content of the first link
check = links[0]
response = requests.get(check)
page_content = response.text
print(page_content)