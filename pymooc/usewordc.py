import  wordcloud
import  matplotlib.pyplot as plt
import jieba

with open('../新时代.txt','r',encoding='utf-8') as f:
    txt=f.read()
c=jieba.lcut(txt)
w=wordcloud.WordCloud(height=1000,width=700,background_color='white',
                      font_path='/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf',max_words=50)

p=w.generate(' '.join(c))
plt.imshow(p)
plt.axis('off')
plt.show()
plt.savefig()