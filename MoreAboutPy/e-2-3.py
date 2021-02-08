
import pandas as pd

#lianjia

path=r"E:\baidudownloads\FORAI\Python-7\(贪心学院）Python基础+机器学习\机器学习集训营资料\第二周\线下\LJdata.csv"
df=pd.read_csv(path,engine='python',header=0,encoding='utf-8')
ls=['district', 'address', 'title', 'house_type', 'area', 'price', 'floor', 'build_time', 'direction', 'update_time', 'view_num', 'extra_info', 'link']

#print(df.sort_values(by='更新时间',ascending=False).head(20))
print(df.describe())
print(df.head(10))
