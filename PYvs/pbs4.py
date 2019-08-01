from bs4 import BeautifulSoup
import bs4
from sys import path
path.append('/root/PycharmProjects/shiyanlouSratches/PYvs')
import lrequests as lre


def fillUnivlist(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')#寻找tr中的td标签,返回列表
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])


def PrintUnivlist(ulist,num):
    #中英文混排输出
    tplt='{0:^10}\t{1:{4}^12}\t{2:^8}\t{3:^6}'
    print(tplt.format('排名','学校','位置','总分',chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],chr(12288)))


def main():
    unifo=[]
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
    html=lre.gethtml(url).text
    fillUnivlist(unifo,html)
    PrintUnivlist(unifo,20)


if __name__ == '__main__':
    main()
