import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['simhei']
plt.rcParams['axes.unicode_minus']=False
pd.set_option('display.max_columns',1024)

#  pd.plot，pandas里简单封装的plot
'''
path="E://baidudownloads//FORAI//Python-7//(贪心学院）Python基础+机器学习//机器学习集训营资料//第二周//GOOG.csv"
df=pd.read_csv(path,index_col=0,parse_dates=[0],engine='python')
plt.plot(df['Adj Close'])
plt.figure('random')
ts=pd.Series(np.random.randn(1000)*1000,index=pd.date_range('1/1/2018',periods=1000))
ts=ts.cumsum()
plt.plot(ts)
plt.figure('dfrandom')
df=pd.DataFrame(np.random.randn(1000,4),index=ts.index,columns=['OP','AS','WZ','TI'])
df=df.cumsum()
print(type(df.columns))
plt.plot(df,label=list(df.columns))
plt.show()
'''
# 构建三个Series，分别是一系列商品的单价，计量单位，和数量
s1=pd.Series(np.arange(1,6),name='price')
s2=pd.Series(np.arange(11,16),name='unit')
s3=pd.Series(np.arange(21,26),name='quantity')
print(s1,s2,s3)
df=pd.DataFrame([s1,s2,s3])
print(df.T)
#io,dataframe
path="E://baidudownloads//FORAI//Python-7//(贪心学院）Python基础+机器学习//机器学习集训营资料//第二周//data//titanic.csv"
dft=pd.read_csv(path,engine='python')
print(dft.head())
#注意df的哪些操作不是inplace
#数据操作，重点在用什么操作来选数据 df['col'>90] bool 表达式
#female=0,male=1
dft['Sex'][dft['Sex']=='male']=1           # dft['Sex'].apply(lambda x:1 if x=='male' else 0)
dft['Sex'][dft['Sex']=='female']=0
#Cabin 填充为0
dft['Cabin']=dft['Cabin'].fillna(0)         #df['Cabin'].fillna(0,inplace=True)
gender=dft['Sex'].value_counts()
#把年龄分类，空值用平均值填充
dft['Age'].fillna(dft['Age'].mean(),inplace=True)
#pd.cut分箱操作，还有打标功能
dfc=dft.copy()
print(dfc.head())
bins=[0,11,22,33,44,55,66,200]
labels=[0,1,2,3,4,5,6]
dfc['Age']=pd.cut(dfc['Age'],bins=bins,labels=labels)
print(dfc.head())
