from bs4 import BeautifulSoup
import requests
url="proj.html"
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
#print(soup.prettify())
container=soup.findAll("div",{"class":"bhgxx2 col-12-12"})
print(len(container))
print(container)
#print(container[0])



