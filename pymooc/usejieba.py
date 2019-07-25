import matplotlib.pyplot as plt
from wordcloud import WordCloud
def getText():
    txt=open('hamlet.txt','r',encoding='utf-8').read()
    txt=txt.lower()
    for ch in "[\\]|,.<>?/:;!\"@#$%^&*()_+-=~`\'":
        txt=txt.replace(ch,' ')
    return txt


hamlet=getText()
worldc=WordCloud().generate(hamlet)
plt.imshow(worldc)
plt.axis('off')
plt.show()
words=hamlet.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))


import jieba
txt1=open('threekingdoms.txt','r',encoding='utf-8').read()
words1=jieba.lcut(txt1)
counts1={}
for word in words1:
    if len(word)==1:
        continue
    else:
        counts1[word]=counts1.get(word,0)+1
items1=list(counts1.items())
items1.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items1[i]
    print('{0:<10}{1:>5}'.format(word,count))