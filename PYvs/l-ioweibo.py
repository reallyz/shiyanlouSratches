from weibopy import WeiboOauth2,WeiboClient
import webbrowser
import json
import re
import time
from collections import defaultdict
from snownlp import SnowNLP
import pandas as pd
import echarts_countries_pypkg,echarts_china_provinces_pypkg
from pyecharts import Map
client_key='3536121960'
client_secret='29a7cb9342f584e7a2fda64124ec01cf'
redirect_url='https://api.weibo.com/oauth2/default.html'
auth=WeiboOauth2(client_key,client_secret,redirect_url)
webbrowser.open(auth.authorize_url)
code=input('the code is\n')
token=auth.auth_access(code)

client=WeiboClient(token['access_token'])
#获取的内容处理：1.删去回复
#2.按地域划分内容
province_list=defaultdict(list)
comment_text_list=[]

for i in range(1,40):
    try:
        result=client.get(suffix='comments/show.json',params={'id':4401542310862649, 'count': 200, 'page': 1})
        comments=result['comments']
        if not len(comments):
            break
        for comment in comments:
            text = re.sub('回复.*?:', '', str(comment['text']))
            province=comment['user']['province']
            province_list[province].append(text)
            comment_text_list.append(text)
            with open('./tep1.txt','a+',encoding='utf-8') as f:
                f.write(text+'\n')
        print('已抓取评论 {} 条'.format(len(comment_text_list)))
        time.sleep(1)
    except:
        print('something went wrong')
provinces={}
results=client.get(suffix='common/get_province.json',params={'country':'001'})
for prov in results:
    for code,name in prov.items():
        provinces[code]=name
propd=pd.Series(provinces)
propd.to_csv('./pron.csv')
positives={}
for province_code,comments in province_list.items():
    sentiment_list=[]
    for text in comments:   #comments is a list
        s=SnowNLP(text)
        sentiment_list.append(s.sentiments)
    #each province's attitude
    positive_number=sum(sentiment_list)
    positive=positive_number/len(sentiment_list)
    #print(positive)
    province_code='0010'+str(province_code)
    if province_code in provinces:
        province_name=provinces[province_code]
        positives[province_name]=positive
ab=pd.Series(positives)
ab.to_csv('./test.csv')
mostp=ab.max()
positives=ab/mostp*100

#print(province_list)
#print(positives)
keys=list(positives.keys())
values=list(positives.values)
map=Map('surpriseme',width=1200,height=600)
map.add('positives',keys,values,visual_range=[0,100],maptype='china'
        ,is_visualmap=True,is_label_show=True,visual_text_color='#000')
map.render('test.html')

'''
with open('./tep.json','a+',encoding='utf-8') as f :
    f.write(json.dumps(result,ensure_ascii=False))
print(result)
'''


