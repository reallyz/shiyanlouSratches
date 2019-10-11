import  numpy as np
import  pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',1024)
plt.rcParams['axes.unicode_minus']=False

path=r"E:\baidudownloads\FORAI\Python-7\(贪心学院）Python基础+机器学习\机器学习集训营资料\第二周\data"
df=pd.read_csv(path+r"\NVDA.csv",index_col=0,parse_dates=[0],engine='python')
dfgg=pd.read_csv(path+r'\GOOG.csv',index_col=0,parse_dates=[0],engine='python')
dfap=pd.read_csv(path+r'\AAPL.csv',index_col=0,parse_dates=[0],engine='python')
dfms=pd.read_csv(path+r'\MSFT.csv',index_col=0,parse_dates=[0],engine='python')

#print(df.head(3))
#print(df.info())
#print(df.describe())

#TODO log_return
adj_close=df['Adj Close']
adj_closeg=dfgg['Adj Close']
adj_closea=dfap['Adj Close']
adj_closem=dfms['Adj Close']

log_return=[]
#print(adj_close,type(adj_close),adj_close.iloc[0])
for i in range(len(adj_close)-1):
    rate=np.log2(adj_close.iloc[i+1]/adj_close.iloc[i])
    log_return.append(rate)
log_return.insert(0,0)
#print(log_return[0:5])
log_rate=pd.Series(log_return,index=adj_close.index,name='log_rate')
#TODO find the first ten
ls=list(log_rate.sort_values(ascending=False)[0:10].index)
#date被解析成了Timestamp
print(df.loc[ls])
#TODO use each month's last day price to plot
#df['Adj Close'].plot()
# log_rate.plot.scatter(x=log_rate.index,y=log_rate.values)# df才有scatter,线形的设置

dfadj_close=pd.DataFrame({'adj_closen':adj_close,'adj_closeg':adj_closeg,'adj_closea':adj_closea,
                          'adj_closem':adj_closem},index=dfgg.index)
dfadj_close.plot()
plt.show()

