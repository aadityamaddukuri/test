from bs4 import BeautifulSoup
import lxml
import urllib.request



def main():
    url=urllib.request.urlopen("http://www.ms2soft.com/tcds/?loc=Minneapolis&mod=tcds&local_id=84")
    data=url.read()
    soup=BeautifulSoup(data,"html.parser")
    print(soup.find_all('tbody'))
   

main()


