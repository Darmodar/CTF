import requests
import urllib
import urllib3
import time
import json
 
 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

URl = 'https://0ab100f303199c45c0fd68f1005d0085.web-security-academy.net/login'

# username_file = open("username.txt", "r")
# password_file = open("password.txt", "r")

# Python program to convert text
# file to JSON
# the file to be converted to
# json format
filename = 'password.txt'
 
# dictionary where the lines from
# text will be stored
dict1 = {}
element = []
# creating dictionary
with open(filename) as fh:
 
    for line in fh:
 
        # reads each line and trims of extra the spaces
        # and gives only the valid words
        description = line.strip('\n')
 
        element.append(description)
    dict1.update({"password" : element})   

file1 = open('password.txt', 'r') 
Lines = file1.readlines() 
for line in Lines: 
    print(' "{}", '.format(line.strip()))
# creating json file
# the JSON file is named as test1
# out_file = open("test1.json", "w")
# json.dump(dict1, out_file, indent = 4, sort_keys = False)
# out_file.close()