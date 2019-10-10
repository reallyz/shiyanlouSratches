import numpy as np
import pandas as pd

#series datafram index io

#index is key!
#key-value,难怪和dict联系非常大了
# pd.Series
pds1=pd.Series(5,index=[1,2,3,4],name='scaler')
pds2=pd.Series(['a','b',1])
pds3=pd.Series({'a':9,'b':10})
pds4=pd.Series(np.random.randn(5))

#选择数据更灵活，相比于列表
pds1[[0,1,2]]
pds3[['a','b']]
pds4.get('who',0) #更安全，找不到值会返回 0
print('a' in pds3)
pds3['c']=12
#pds3.append 这里Series or list/tuple of Series，index_ingored
#真的类似于字典，
# 过滤器 bool索引
#print(pds3[pds3>9])

# dataframe
#把多个serise连起来
df=pd.DataFrame(pds1)
print(df)
#dict
data = {'city': ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Hangzhou', 'Chongqing'],
       'year': [2016,2017,2016,2017,2016,2016],
       'population': [2100, 2300, 1000, 700, 500, 500]}
df1=pd.DataFrame(data,index=['a','b','c','d','e','f'],columns=['population',
                                                               'year','city'])

print(df1)
# serise
df2=pd.DataFrame({'pds1':pds1,'pds2':pds2})
print(df2) #index对齐
# list of dict
data2=[{'july':100,'may':200},{'july':200,'may':300},{'july':300,'may':200,'dec':100}]
df3=pd.DataFrame(data2,index=['one','two','three'])
print(df3)

#取数据,取了之后就能赋值
print(df3['july'])#列
print(df3.loc['one']) #行
print(df3.loc['one','july'])#只有出现逗号，前面为行，后面为列
print(df3.iloc[0,0])#iloc默认是选列
#添加列
df3['diff']=df3['july']-df3['may']
print(df3)
#dataframe.append,     DataFrame or Series/dict-like object, or list of these
df4=df3.T
df4.columns.name='num'
df4.index.name='type'
print(df3.T)
#index,是一个单独的对象
#reindex,重排
df4=df4.reindex(['may','july','dec','diff'],columns=['three','two','one'])
print(df4)
#reindex的同时，可以重排columns
#drop 数据。注意drop的效果不是in place的，也就是说他会返回一个object，原来的Obejct并没有被改变
#默认axis=0,即drop行，axis=1,drop列,


#io,
'''
pd.read_csv(params,)#决定谁作index,时间解析等
df.to_csv()
'''
