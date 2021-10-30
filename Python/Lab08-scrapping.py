import requests
import re
from bs4 import BeautifulSoup

data = requests.get(
    "https://www.radioshack.com/collections/headphones/products/decibel-b68-bluetooth-headphones-club-studio").content
soup = BeautifulSoup(data, "html.parser")
span = soup.find("h1")
title = span.text
# print(title)
span = soup.find("p", {"class": "price_range"})
price = span.text
# print(price)
span = soup.find("span", {"class": "vendor_wrapper"})
vendor = span.text
# print(vendor)
print("Product %s is with %s with a price of %s." % (title, vendor, price))
