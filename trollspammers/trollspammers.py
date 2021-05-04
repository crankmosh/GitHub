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


# loop forever, or till we get a bad response
while True:

    # generate some fake info, faker has built in "Factories"
    goodname = fake.name()
    goodcard = fake.credit_card_number()
    gooddate = fake.credit_card_expire()
    goodcvv = fake.credit_card_security_code()
    goodagent = fake.chrome()
    
    # put the URL yer going to attack here
    url = 'https://quickmove247.co.uk/dhl/index.php'
    # modify as needed for fields
    obj = {'captcha' : '', 'step' : 'cc', 'name' : goodname, 'one' : goodcard, 'two' : gooddate, 'three' : goodcvv}
    # basically a debug output
    print(obj)
    # headers (depending how stupid the phishing script is, which usually isn't very intelligent
    headers = {'authority' : 'yourmom.com', 'method' : 'POST', 'path' : '', 'scheme' : 'https', 'accept' : '*/*', 'user-agent' : goodagent, 'x-requested-with' : 'XMLHttpRequest'} #if needed

    # POST that badboy
    r = requests.post(url, data=obj, headers=headers)

    print("POST Request made.")
    print(r.status_code, r.reason)
    print("\n")
    randsleep = random.uniform(1.0, 7.5)
    print("Sleep for " + str(randsleep) + "\n")
    time.sleep(randsleep)
