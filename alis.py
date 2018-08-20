import requests
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
html2 = "https://www.six-group.com/en/home.html"
soup2 = requests.get(html2)
print(soup2)
soup = BeautifulSoup(html,'lxml')

#print(soup)
soup_b = soup.prettify()
#print(soup_b)
s = soup_b
#print(s)

response = requests.get(html2)
soup = BeautifulSoup(response.content, "html.parser")
#print(response.content)

soupc=soup.prettify()
c = soupc.title
#print(soupc)
#print(soup.a['class'])
chil = soup.head.children
desc = soup.head.descendants
part = soup.a.parent
parts = soup.a.parents
sibs = soup.a.next_siblings
sibs2 = soup.a.previous_siblings
#print(list(enumerate(sibs)))
#print(list(enumerate(sibs2)))
#print(list(enumerate(parts)))
#print(part)
#print(chil)

soup = soup.body
lis = soup.find_all('a')
print(type(lis))
print(type(lis[0]))
print("[*]"*5)
for i in range(3):
    print(i,"\n","[*]"*5,"\n",lis[i].attrs['class'])

#for i, child in enumerate(desc):
#    print(i,child)