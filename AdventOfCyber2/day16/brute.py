#!/usr/bin/env python3

import requests 

api_key = 1
html = requests.get(f'http://10.10.205.172:8000/api/{api_key}') 

soup = BeautifulSoup(html.text, "lxml")
