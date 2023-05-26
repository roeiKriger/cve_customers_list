from methods import *
from consts import *
import requests
from bs4 import BeautifulSoup

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

response = requests.get(full_url)
page_content = response.text
print(page_content)







# check_url_integrity(cve_url_list, url_len, regex_rule_for_url)
# links_of_the_month = get_cve_monthly_links()
#
#
# # Extract the text inside the <p> tag from each link
# data = []
# for link in links_of_the_month:
#     response = requests.get(link)
#     page_content = response.text
#     soup = BeautifulSoup(page_content, "html.parser")
#     paragraph = soup.find("p", attrs={"data-testid": "vuln-description"})
#     if paragraph:
#         data.append(paragraph.text)
#     break
#
# # Print the extracted text
# for item in data:
#     print(item)
#     break

