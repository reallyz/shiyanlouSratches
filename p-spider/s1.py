
#use requests_html
from requests_html import HTMLSession
import csv
sess=HTMLSession()
r=sess.get('https://movie.douban.com/subject/1292052/')
#content > h1 > span:nth-child(1)
#content > h1 > span:nth-child(1)
#content > h1:nth-child(3) > span:nth-child(1)
title=r.html.find('#content > h1 > span:nth-child(1)',first=True)
print(title.text)
url='https://movie.douban.com/subject/'
link1=[url+'1292052/',url+'1291546/',url+'1295644']
with open('./douban.csv','w') as f:
    cw=csv.writer(f)
    cw.writerow(['片名','年份'])
    for link in link1:
        rs = sess.get(link)#针对top250有效
        t=rs.html.find('#content > h1:nth-child(3) > span:nth-child(1)', first=True)
        y=rs.html.find('.year', first=True)
        cw.writerow([t.text,y.text])
r.close()
#html,css,javascript重新渲染
r = sess.get('https://sou.zhaopin.com/?jl=530&kw=python&kt=3')
r.html.render()
nextButton = r.html.find('#pagination_content > div > button:nth-child(7)',first=True)
print(nextButton.text)
r.close()