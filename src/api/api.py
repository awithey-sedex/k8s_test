import os
import requests

ENDPOINTURL = os.environ['APIENDPOINTURL']

if ENDPOINTURL[:1] != '/':
    ENDPOINTURL += '/'

if '://' not in ENDPOINTURL:
    ENDPOINTURL = 'http://' + ENDPOINTURL

print("Endpoint url:", ENDPOINTURL)

def is_prime_number(x):
    url = ENDPOINTURL + str(x)
    print("Call endpoint: " + url)
    r = requests.get(url)
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
    l = []
    for i in range(start,end,1):
        l.append(prime_text(i))
    return l

if __name__ == '__main__':
    for p in prime_list():
        print(p)
