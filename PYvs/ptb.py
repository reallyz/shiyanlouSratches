import requests
import re
from lrequests import gethtml
from bs4 import BeautifulSoup

#目标：提取名称和价格
#掌握：接口的应用(没有接口），翻页的处理(淘宝反爬虫，需要登录）

#requests,re


def paserpage(ilt,html):
    pass

def printGoodlist(ilt):
    pass
def main():
    pass

if __name__ == '__main__':
    main()
    url='https://list.tmall.com/search_product.htm?q=七夕&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton'
    html=gethtml(url)
    soup=BeautifulSoup(html.text,'html.parser')
    soup.find()


