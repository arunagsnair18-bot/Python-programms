"""import math

print(math.pi)
print(math.sqrt(49))
print(math.pow(2,3))

from math import sqrt 
print(sqrt(36))

import random
print(random.randint(1,20))

import string
random_letter=random.choice(string.ascii_letters)
print(random_letter)

small_letter=random.choice(string.ascii_lowercase)
print(small_letter)

cap_letter=random.choice(string.ascii_uppercase)
print(cap_letter)

list1=[1,2,3]
print(random.choice(list1))

#try out multiple random generation
#try out secret module....eg otp

import datetime
print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.date.today()-datetime.timedelta(1))
print(datetime.date.today()-datetime.timedelta(2))"""
'''
#try out random date in btwn specific dates

import sys
print(sys.platform)
print(sys.version)

import os
print(os.getcwd())
print(os.listdir())

#alias temperory  name
import datetime as dt
print(dt.datetime.now())
'''

import requests
url = requests.get('https://jsonplaceholder.typicode.com/users/2')
print(url.json())



















