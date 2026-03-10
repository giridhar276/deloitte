


import requests 
from bs4 import BeautifulSoup

response = requests.get("https://www.google.com")
print(response.status_code)
print("------------")
soup = BeautifulSoup(response.text, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
    print("------------------")
