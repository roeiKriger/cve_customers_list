from methods import *
from consts import *
import requests
from bs4 import BeautifulSoup

customers_list = read_customers_to_an_array()
# Print the customer names
for customer in customers_list:
    print(customer)

check_url_integrity(cve_url_list, url_len, regex_rule_for_url)
links_of_the_month = get_cve_monthly_links()


# Extract the text inside the <p> tag from each link
data = []
for link in links_of_the_month:
    response = requests.get(link)
    page_content = response.text
    soup = BeautifulSoup(page_content, "html.parser")
    paragraph = soup.find("p", attrs={"data-testid": "vuln-description"})
    if paragraph:
        data.append(paragraph.text)
    break

# Print the extracted text
for item in data:
    print(item)
    break

