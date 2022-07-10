import requests
import random
import time
import re



with requests.Session() as session:


    session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    response = session.get('https://ctzensmainprofile1.dns2.us/start/')
    cookies= response.cookies.get_dict()

    time.sleep(2)

    token = re.search('token=[\w]*',response.text).group(0)
    token=token.replace('token=','')

    PARAMS = {'username':'sdfsdfsdf','password':'sdfsdfsdf'}


    url = 'https://ctzensmainprofile1.dns2.us/start/Meta/Benchmark/?token='+token


    r = session.post(url,data=PARAMS)

    time.sleep(2)

    r = session.post(url,data=PARAMS)





    #print(r.text)





        
  

