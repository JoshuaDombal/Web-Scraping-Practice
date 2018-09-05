from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://www.glassdoor.com/Salaries/seattle-software-engineer-salary-SRCH_IL.0,7_IM781_KO8,25.htm")
bsObj = BeautifulSoup(html, features="lxml")

nameList = bsObj.findAll("span", {"class":"OccMedianBasePayStyle__payNumber"}, {"data-test":"AveragePay"})
for name in nameList:
    print(name.get_text())



    #class ="OccMedianBasePayStyle__payNumber" data-test="AveragePay" > $126, 913 < / span >