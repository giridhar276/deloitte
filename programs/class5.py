import requests 
from bs4 import BeautifulSoup
class Readweb:
    def __init__(self,link):
        self.link =link
    def readURL(self):
        self.response = requests.get(self.link)
        if self.response.status_code == 200:
            return self.response.text

    def getURLS(self,data):
        self.data = data
        self.soup = BeautifulSoup(self.data, 'html.parser')
        for link in self.soup.find_all('a'):
            print(link.get('href'))
            print("------------------")

if __name__ == "__main__":
    url = "https://www.google.com"
    web = Readweb(url)
    text = web.readURL()
    print(text)
    web.getURLS(text)