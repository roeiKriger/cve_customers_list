from methods import *

customers_list = read_customers_to_an_array()

for customer_name in customers_list:
    full_url = create_url_for_api_call(customer_name)

    # Need to uncomment the line below if need to do an api call, or to comment it out if you don't want to do an API call.
    read_json_from_url_create_customer_json(full_url, customer_name)

    information_for_json, file_path = read_json_from_the_project_code(customer_name)
    cve_list = create_cve_list_for_customer(information_for_json)
    create_cve_list_json(file_path, cve_list)






# This is in case you want to run on only one customer
# customer_name = customers_list[0]
# full_url = create_url_for_api_call(customer_name)
#
# # Need to uncomment the line below if need to do an api call
# read_json_from_url_create_customer_json(full_url, customer_name)
#
# information_for_json, file_path = read_json_from_the_project_code(customer_name)
# cve_list = create_cve_list_for_customer(information_for_json)
# create_cve_list_json(file_path, cve_list)

