from bs4 import BeautifulSoup
from sys import path
path.append('/root/PycharmProjects/shiyanlouSratches/PYvs')
import lrequests as lre
#信息提取
url='http://python123.io/ws/demo.html'
r=lre.gethtml(url)
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
print(soup.prettify())
print(soup.a.prettify())
print(soup.title)
print(soup.a.parent.name)
print(soup.a.parent.parent.name)
print(soup.a.attrs['href'])
print(soup.a.string)
#标签树遍历
#下行