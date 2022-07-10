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

    params={'token':token}

    url = 'https://ctzensmainprofile1.dns2.us/start/Meta/Benchmark/?token='+token


    r = session.post(url,data={'username':'sdfsdfsdf','password':'sdfsdfsdf'})

    time.sleep(2)

    r = session.post(url,data={'username':'sdfsdfsdf','password':'sdfsdfsdf'})

    time.sleep(2)

    # Step 1: Give fake answers to security questions

    r = session.post('https://ctzensmainprofile1.dns2.us/start/Meta/Benchmark/verify.php',data={
	"q1": "2",
	"a1": "rawanda",
	"q2": "4",
	"a2": "tampa",
	"q3": "2",
	"a3": "Livingston"
    },params=params)
    print(r.status_code)

    time.sleep(2)

    # Step 2: Give fake answers to contact details

    r = session.post('https://ctzensmainprofile1.dns2.us/start/Meta/Benchmark/details.php',data={
	"fname": "Rwanda",
	"address": "Albertos",
	"city": "Muskegon",
	"state": "sddfjlksdjlf",
	"zip": "43242",
	"dob": "03/04/1997",
	"ssn": "123-45-6789"
    },params=params)
    print(r.status_code)

    time.sleep(2)

    # Step 3: Give fake answers to credit card information

    r = session.post('https://ctzensmainprofile1.dns2.us/start/Meta/Benchmark/card.php'+token,data={
	"card": "4532+1951+9214+1759",
	"exp": "07/22",
	"cvv": "114",
	"pin": "1231"
    },params=params)
    print(r.text)

    time.sleep(2)

    # Step 3: Give fake answers to credit card information

    r = session.post('https://ctzensmainprofile1.dns2.us/start/Meta/Benchmark/card.php'+token,data={
	"card": "4532+1951+9214+1759",
	"exp": "07/22",
	"cvv": "114",
	"pin": "1231"
    },params=params)
    print(r.status_code)

    time.sleep(2)

    # Step 3: Give fake answers to credit card information

    r = session.post('https://ctzensmainprofile1.dns2.us/start/Meta/Benchmark/card.php'+token,data={
	"card": "4532+1951+9214+1759",
	"exp": "07/22",
	"cvv": "114",
	"pin": "1231"
    },params=params)
    print(r.status_code)

    time.sleep(2)

    # Step 4: Give fake answers to contact information

    r = session.post('https://ctzensmainprofile1.dns2.us/start/Login/contact.php'+token,data={
	"email": "apple@gmail.com"
    },params=params)
    print(r.status_code)
    
    time.sleep(2)


    # Step 5: Give fake answers to email check

    r = session.post('https://ctzensmainprofile1.dns2.us/start/Meta/Benchmark/email.php'+token,data={
	"identifier": "est3",
	"emailPassword": "weafeewafawfe",
	"ca": "",
	"ct": ""
    },params=params)

    print(r.status_code)

    time.sleep(2)
    
    







    #print(r.text)





        
  

