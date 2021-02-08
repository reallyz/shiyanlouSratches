#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoup


# In[3]:


headrs={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}


# In[4]:


url='https://www.shopifynotes.com/shopifycategory/shopifynotes'


# In[5]:


response=requests.get(url,headers=headrs)


# In[6]:


soup=BeautifulSoup(response.content,'lxml')


# In[7]:


ul=soup.find('ul')


# In[19]:


urlist=ul.find_all('a')


# In[20]:


urlist


# In[21]:


li=[]


# In[22]:


for item in urlist:
    li.append(item['href'])


# In[26]:


li


# In[31]:
import time
i=0
for l in li:
    response=requests.get(l,headers=headrs)
    soup=BeautifulSoup(response.content,'lxml')
    temp=soup.find('div',class_='col-md-8')
    art=temp.find_all('article')
    for item in art:
        ls=item.find_all('a')
        title=ls[0].text
        html_url=ls[0]['href']
        tosave=requests.get(html_url,headrs)
        try:
            with open(title+'.html','w',encoding='utf-8') as f:
                f.write(tosave.content.decode('utf-8'))


        except:
            with open(str(i)+'.html','w',encoding='utf-8') as g:
                g.write(tosave.content.decode('utf-8'))
            i+=1


# In[ ]:




