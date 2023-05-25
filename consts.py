# The interesting url
cve_url_list = "https://nvd.nist.gov/vuln/full-listing/2023/5"
site_base_url = "https://nvd.nist.gov"
number_of_links_to_scan = 50
# At the moment the url length is 45, but there are months that are also more than one digit, so added 1 to 46
# #(in the future will just check the month with DATE TIME and then will validate)
url_len = 46

# With this rule we will be able to avoid some unwanted urls in the future, and unwanted scripts or urls in our code
regex_rule_for_url = r"^https:\/\/(\w+(?:\.\w+)*\/)+vuln\/full-listing\/\d{4}\/\d{1,2}$"
