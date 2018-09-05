from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://books.toscrape.com/"
html = urlopen(url)
bsObj = BeautifulSoup(html, features="lxml")

#print(bsObj.title)

list = bsObj.findAll("a", {"href":"catalogue/a-light-in-the-attic_1000/index.html"})

for title in list:
    print(title.get_text())

    #< ahref = "catalogue/a-light-in-the-attic_1000/index.html"title = "A Light in the Attic" > ALight in the... < / a >