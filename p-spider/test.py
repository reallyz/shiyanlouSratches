
import  requests_html

def testit(url,selector=''):

    pg=requests_html.HTMLSession().get(url)
    text=pg.html.find(selector,first=True).text
    print(text)
n=44683
try:
    for i in range(100):
        url='http://www.quanshuwang.com/book/44/'+str(n)
        selector='.chapName > strong:nth-child(2)'
        testit(url,selector)
        n+=1
except:
    pass




