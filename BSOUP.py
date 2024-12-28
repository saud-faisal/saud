import requests
from bs4 import BeautifulSoup
url="""
<html>
<head>	
<title>beautiful soup</title>
</head>
<body>
	<h1 id="h1">
    	Hello, Dcoder
	</h1>
	<p id="p1">this is the normal webpage
	</p>
	<div class="link">
	<a href="#">home</a>
	<a href="#">service</a>
	<a href="#">link</a>
	<a href="#">link</a>
	</div>
	<div class="para">
	<p id="p">this is another paragraph
	</p>
	</div>
	<div class="jj">
     <div class="pp">
       <div class="kk">
         <p class="op">4320this is the paragraph
         </p>
       </div>
     </div>
  </div>
  	<div class="jj">
     <div class="pp">
       <div class="kk">
         <p class="op">3498this is the paragraph
         </p>
       </div>
     </div>
  </div>
  	<div class="jj">
     <div class="pp">
       <div class="kk">
         <p class="op">2400 this is the paragraph
         </p>
       </div>
     </div>
  </div>
  
</body>
</html>
"""
soup=BeautifulSoup(url,"html.parser")
#print(soup)
#print(soup.prettify())
#print(soup.title.name)
#print(soup.title.text)
#print(soup.title.string)
#print(soup.head.name)
#print(soup.find_all("p"))
#print(soup.find_all("a")[1])
#print(soup.find_all("div"))
#print(soup.div.find_all("a"))
#print(soup.p["id"])
#print(soup.get_text())
#print(soup.get_text().strip( ))
container=soup.findAll("div",{"class":"jj"})
#print(container)
#print(container[0])
f=open("text.csv","w")
for cont in container:
	price=cont.find("div",{"class":"kk"})
	f.write(price.p.text)
	print(price.p.text)
"""
for i in range(0,len(container)):
	price=container[i].find("div",{"class":"kk"})
	x=str(price.p.text.strip())
	f.write(x)
	print("\n")
f.close()
"""
f=open("text.csv","r")
print(f.read())
f.close()









