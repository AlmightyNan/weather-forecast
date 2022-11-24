# Modules used: requests, os
# Made by AlmightyNan

import requests
import os

os.system(" ") # Making sure colors get printed on command line
city = input('[ ? ]  Enter city name:  ') # Getting the city name as input string

print('[//]  Displaying weather report for: ' + city)

url = 'https://wttr.in/{}'.format(city) # Using https://wttr.in/ to get reports
res = requests.get(url) # Fetching the weather report

print(res.text) # Printing the weather report