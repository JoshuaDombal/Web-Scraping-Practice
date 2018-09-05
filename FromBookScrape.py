from urllib.request import urlopen
from bs4 import BeautifulSoup


try:
    html = urlopen("https://www.bls.gov/news.release/empsit.t01.htm")
    bsObj = BeautifulSoup(html.read(), features="lxml")
    print(bsObj.body)

except HTTPError as e:
    print(e)
else:
    # Program continues