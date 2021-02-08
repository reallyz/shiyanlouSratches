import jieba
import matplotlib.pyplot as plt
import wordcloud

with open('../python_北京理工大学/tep1.txt','r',encoding='utf-8') as f:
    txt=f.read()
c=jieba.lcut(txt)
w=wordcloud.WordCloud(height=1000,width=700,background_color='white',
                      font_path='/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf',max_words=10)

p=w.generate(' '.join(c))
plt.imshow(p)
plt.axis('off')
plt.show()
plt.savefig()