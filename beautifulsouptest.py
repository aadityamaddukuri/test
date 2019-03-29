from bs4 import BeautifulSoup
import lxml
with open("test1.html") as fp:
    soup=BeautifulSoup(fp,"html.parser")




print(soup.prettify())
