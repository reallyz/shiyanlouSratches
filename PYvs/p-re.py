import  re
'''
with open('p-re.txt','r+') as f:
    for line in f:
        #print(line,'ok',type(line))
        m=re.match(r'(https|ftp|file)(://)[-A-Za-z0-9+&@#/%?=~_|!:,.;]z+[-A-Za-z0-9+&@#/%=~_|]',line)
        if m:
            print(m)
'''

s='<div class="imgview" id="imgView"><a href="https://xinwen.eastday.com/a/n181211075002407.html?qid=news.baidu.com" target="_blank"><img src="https://imgsa.baidu.com/news/q%3D100/sign=cdae0fb78a94a4c20c23e32b3ef51bac/cefc1e178a82b90151b62d8b7e8da9773912ef6b.jpg"></a></div><ul><li class="hdline0">'
mm=re.match(r'<("[^"]*"|\'[^\']*\'|[^\'">])*>',s)
m3=re.match(r'https',s)
mc=re.match(r'010','https01012345')
print(mc)
print(m3)
print(mm)