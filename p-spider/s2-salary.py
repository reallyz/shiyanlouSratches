import requests_html
import re
import matplotlib.pyplot as plt


salre=re.compile(r'(\d+)K-(\d+)K')
finalp=re.compile(r'<button.* disabled="disabled">下一页</button>')
disb=None
p=1
salary=[]
tep=[]
while not disb:
    print('正在爬取第'+str(p)+'页')
    url = 'https://sou.zhaopin.com/?p=' + str(p)\
          + '&jl=530&kw=爬虫工程师&kt=3'
    s = requests_html.HTMLSession()
    pg = s.get(url)
    pg.html.render(sleep=3)
    salary+=re.findall(salre,pg.html.html)
    print(salary)
    '''
    with open('./salary.txt','w+') as f:
        f.writelines(tp)
    disb=re.findall(finalp,pg.html.html)
    '''
    p+=1
    tp=[]
    s.close()
salary=[(int(s[0])+int(s[1]))/2 for s in salary]

l,m,h=[0,0,0]
for s in salary:
    if s<=15:
        l+=1
    if s>15 and s<=30:
        m+=1
    if s>30:
        h+=1
plt.figure(figsize=(6,9))
labels=[u'<15k',u'15k-30k',u'>30k']
data=[l,m,h]
plt.pie(data,labels=labels)
plt.axis('equal')
plt.legend('salary dist')
plt.show()


