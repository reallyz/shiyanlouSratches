
#use requests_html
from requests_html import HTMLSession
sess=HTMLSession()
r=sess.get('https://movie.douban.com/subject/1292052/')
title=r.html.find('#content > h1:nth-child(3) > span:nth-child(1)',first=True)
print(title.text)
url='https://movie.douban.com/subject/'
link1=[url+'1292052/',url+'1291546/',url+'1295644']

for link in link1:
    rs = sess.get(link)#针对top250有效
    t=rs.html.find('#content > h1:nth-child(3) > span:nth-child(1)', first=True)
    y=rs.html.find('.year', first=True)
    print(t.text,y.text)


r = sess.get('https://sou.zhaopin.com/?jl=530&kw=python&kt=3')
r.html.render()
nextButton = r.html.find('#pagination_content > div > button:nth-child(7)',first=True)
print(nextButton.text)
