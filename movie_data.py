from bs4 import BeautifulSoup
import requests

url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
r=requests.get(url)

soup=BeautifulSoup(r.content,'html5lib')
print(soup.prettify())