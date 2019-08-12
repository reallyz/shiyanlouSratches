import requests
from bs4 import BeautifulSoup
import traceback #convenient for test
import re
from lrequests import gethtml


def getstocklist(lst,stockurl):
    html=gethtml(stockurl).text
    soup=BeautifulSoup(html,'html.parser')
    a=soup.find_all('a')
    for i in a :
        try:
            href=i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}',href)[0])
        except:
            continue

def getstockinfo(lst,stockurl,fpath):
    count=0
    for stock in lst:
        url=stockurl+stock+'.html'
        html=gethtml(url).text
        try:
            if html=='':
                continue
            infodict={}
            soup=BeautifulSoup(html,'html.parser')
            stockinfo=soup.find('div',attrs={'class':'stock-bets'})
            name=stockinfo.find_all(attrs={'class':'bets-name'})[0]
            infodict.update({'股票名称':name.text.split()[0]})
            keylist=stockinfo.find_all('dt')
            valuelist=stockinfo.find_all('dd')
            for i in range(len(keylist)):
                key=keylist[i].text
                val=valuelist[i].text
                infodict[key]=val
            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infodict)+'\n')
                count+=1
                print('\r当期进度：{:.2f}%'.format(count*100/len(lst)),end='')
        except:
            count+=1
            print('\r当期进度：{:.2f}%'.format(count*100/len(lst)),end='')


def main():
    stock_list_url='https://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = './BaiduStockInfo.txt'
    slist=[]
    getstocklist(slist,stock_list_url)
    getstockinfo(slist,stock_info_url,output_file)
    for i in slist:
        print(i)
main()
