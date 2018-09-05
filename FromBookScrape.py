from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import HTTPError


url = "https://www.bls.gov/news.release/empsit.t01.htm"

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    try:
        bsObj = BeautifulSoup(html.read(), features="lxml")
        title = (bsObj.title)
    except AttributeError as e:
        return None
    return title


title = getTitle(url)
if title == None:
    print("Title could not be found")
else:
    print(title)
