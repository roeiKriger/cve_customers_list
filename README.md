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







![image](https://github.com/roeiKriger/cve_customers_list/assets/66572300/fd943aaa-cd56-4b45-87ba-0e955eeb408a)
![image](https://github.com/roeiKriger/cve_customers_list/assets/66572300/c000a029-b111-4c89-aca0-747807ca9658)





