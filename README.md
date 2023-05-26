# Python program to collect CVE's based on keywords important to you

### How it works:

The program is using https://nvd.nist.gov/vuln/full-listing as a source of information about CVE's.

An API call with different varaiables (Date, Keyword to search, Severity) is being made.
The data is being saved a 'Keyword.json'.


Then the program extract important info such as description and weaknesses and then it saves it to a cleaner jsin file: 'Keyword_CVE.json'

* customers_list.json - each customer in the array is a keywrod search that will be used in an API call, can change it based on your interests.
* consts.py - has the varaiables for the API call, can change there things like severity, dates, and more.
* main.py - the main page of the code to execute.
* methods - contain all the methods of the program. 

Keep in mind that there is a rate limit on the API call, so you should use with thought the amount of calls for different keywords (customers), recommended to make an account to have more calls per minute.

Basic Visualization of the program:







![part 1 of the visualization](https://github.com/roeiKriger/cve_customers_list/blob/main/images_visual/part1py.png?raw=true)


![part 2 of the visualization](https://github.com/roeiKriger/cve_customers_list/blob/main/images_visual/part2py.png?raw=true)





