import os
import requests

ENDPOINTURL = os.environ['APIENDPOINTURL']
REQUESTTIMEOUT = os.environ.get('REQUESTTIMEOUT', 10)
try:
    REQUESTTIMEOUT = int(REQUESTTIMEOUT)
except:
    REQUESTTIMEOUT = 10

if ENDPOINTURL[:1] != '/':
    ENDPOINTURL += '/'

if '://' not in ENDPOINTURL:
    ENDPOINTURL = 'http://' + ENDPOINTURL

print("Endpoint url:", ENDPOINTURL)

def is_prime_number(x):
    url = ENDPOINTURL + str(x)
    print("Call endpoint: " + url)
    r = requests.get(url, timeout=REQUESTTIMEOUT)
    r.raise_for_status()
    if r.status_code == 200 and r.text:
        result = r.text.strip().lower()
        print (result)
        return result == 'true'

def prime_text(x):
    if is_prime_number(x):
            return '{} is prime.'.format(x)
    return '{} is not prime.'.format(x)

def prime_list(start,end):
    return "Not yet implemented!"

if __name__ == '__main__':
    print(prime_text(1))
    print(prime_text(2))
    print(prime_text(3))
    print(prime_text(4))
