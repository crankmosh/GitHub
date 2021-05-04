# this will fill a form with fake information, used to attack phishing URLs
# requires request and faker libs in Python 3
import requests
import random
import string
import os
import time
from faker import Faker

fake = Faker()
Faker.seed(random.randint(0,100))


# create a user agent list most blockers accept
UAlist = ['Mozilla/5.0 (Windows NT 10.0; ber-MA; rv:1.9.2.20) Gecko/2020-02-03 10:13:19 Firefox/14.0',
'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/536.1 (KHTML, like Gecko) CriOS/26.0.852.0 Mobile/64T196 Safari/536.1',
'Mozilla/5.0 (Linux; Android 3.2.2) AppleWebKit/535.0 (KHTML, like Gecko) Chrome/20.0.866.0 Safari/535.0',
'Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/532.28.7 (KHTML, like Gecko) Version/5.0.2 Safari/532.28.7',
'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/534.1 (KHTML, like Gecko) FxiOS/11.8w7752.0 Mobile/31Z815 Safari/534.1',
'Mozilla/5.0 (Windows NT 5.1; oc-FR; rv:1.9.1.20) Gecko/2020-07-28 13:55:27 Firefox/3.8']

failc = 0

# loop forever, or till we get a bad response
while True:

    # generate some fake info, faker has built in "Factories"
    goodname = fake.name()
    goodcard = fake.credit_card_number()
    gooddate = fake.credit_card_expire()
    goodcvv = fake.credit_card_security_code()
    goodagent = random.choice(UAlist)
    
    # put the URL yer going to attack here
    url = 'https://quickmove247.co.uk/dhl/index.php'
    # modify as needed for fields
    obj = {'captcha' : '', 'step' : 'cc', 'name' : goodname, 'one' : goodcard, 'two' : gooddate, 'three' : goodcvv}
    # basically a debug output
    print(obj)
    print("\nUser-Agent: " + goodagent + "\n")
    # headers (depending how stupid the phishing script is, which usually isn't very intelligent
    headers = {'authority' : 'yourmom.com', 'method' : 'POST', 'path' : '', 'scheme' : 'https', 'accept' : '*/*', 'user-agent' : goodagent, 'x-requested-with' : 'XMLHttpRequest'} #if needed

    # POST that badboy
    try:
       r = requests.post(url, data=obj, headers=headers)
    except:
       pass
       failc += 1
       
    print("POST Request made.")
    print(r.status_code, r.reason)
    print("\nFails: " + failc + "\n")
    randsleep = random.uniform(0.3, 3.5)
    print("Sleep for " + str(randsleep) + "\n")
    time.sleep(randsleep)
