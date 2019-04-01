from bs4 import BeautifulSoup
import lxml
import urllib.request

def main():
    url=urllib.request.urlopen("https://www.google.com/")
    data=url.read()
    soup=BeautifulSoup(data,"html.parser")
    print(soup.find_all('td'))

main()


