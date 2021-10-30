import requests
import re

data = "Hello. My email is sheelpatel1801@gmail.com. Please contact me!"
p = re.compile('[A-Za-z0-9_%.-]+@[A-z0-9_%.-]+\.[A-z0-9]{2,}')
print(p.search(data).group())
