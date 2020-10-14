from bs4 import BeautifulSoup
from sys import path
import re
path.append('/root/PycharmProjects/shiyanlouSratches/Python_北京理工大学')
import lrequests as lre
#信息提取
url='http://python123.io/ws/demo.html'
r=lre.gethtml(url)
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
print(soup.prettify())#对整体
print(soup.a.prettify())#对标签
print(soup.title)
print(soup.a.parent.name)
print(soup.a.parent.parent.name)
print(soup.a.attrs['href'])
print(soup.a.get('class'))
print('this is a type',type(soup.a))
#标签树遍历,有迭代类型
#下行，上行，平行
#信息的标记：html,xml,json,yaml
#信息的提取
for link in soup.find_all('a'):
    print(type(link))
    print(link.get('href'))

for tag in soup.find_all(re.compile('b')):
    print(tag.name)

print(soup.find_all(id=re.compile('link')))
print(soup.find_all(string='Basic Python'))
print('find python',soup.find_all(string=re.compile('(P|p)ython')))#大小写的问题
