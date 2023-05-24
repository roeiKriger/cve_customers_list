# The interesting url
cve_url_list = "https://nvd.nist.gov/vuln/full-listing/2023/5"

# At the moment the url length is 45, but there are months that are also more than one digit
url_len = 46

# With this rule we will be able to avoid some unwanted urls in the future, and unwanted scripts or urls in our code
regex_rule_for_url = r"^https:\/\/(\w+(?:\.\w+)*\/)+vuln\/full-listing\/\d{4}\/\d{1,2}$"
