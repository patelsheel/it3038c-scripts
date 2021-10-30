import re
import requests
from bs4 import BeautifulSoup

r = requests.get(
    "http://webscraper.io/test-sites/e-commerce/allinone/phones").content
soup = BeautifulSoup(r, "lxml")
tags = soup.findAll('div', {'class': re.compile('(ratings)')})
for div in tags:
    a = (div.findAll("p", {"class": "pull-right"}))
    print((a[0].string))

#tags = soup.find_all("a", {"href": re.compile('(phones)')})
# for a in tags:
#    print(a.get('href'))
