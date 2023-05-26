# These consts are all building together the API GET request to get details about each customer
base_url = 'https://services.nvd.nist.gov/rest/json/cves/2.0?'
keyword_customer_name = 'keywordSearch='
dates = 'pubStartDate=2023-03-04T00:00:00.000&pubEndDate=2023-05-05T00:00:00.000'
cvss_severity = 'cvssV3Severity=CRITICAL'
max_results_to_return = 'resultsPerPage=100'
