import pandas as pd

# python里一切都是对象(引用），所以用对可变的数据类型一定要慎重
# 比如列表，dataframe，这种类型，一个对象变化，所有引用该对象都改变
df=pd.read_excel(r"E:\temp\test.xlsx")
stop=len(df)
itemlist=['产品A','产品B','产品C']
refund=['未发货退款','退货退款']
df.iloc[0,2]='未发货退款'
ind=[]
deal=[]
for i in itemlist:
    ind.append(df[df['货号']==i].index.tolist()[0])
for j in refund:
    deal.append(df[df['退款类型']==j].index.tolist())
money=[]
for item in ind:
    money.append(df.iloc[item,1])
ind.append(stop)
#对数据结构要有了解
for i in range(3):#fill 产品和售卖总数
    df.iloc[ind[i]:ind[i+1],0].fillna(itemlist[i],inplace=True)
    df.iloc[ind[i]:ind[i+1],1].fillna(money[i],inplace=True)
for j,k in zip(deal[0],deal[1]):#fill 未发货退款
    df.iloc[j:k].fillna(refund[0],inplace=True)
#骚气的python引用开始出现了！！！
temp=deal[0]
temp.pop(0)
temp.append(stop)
for j,k in zip(deal[1],deal[0]):#fill 未发货退款
    df.iloc[j:k].fillna(refund[1],inplace=True)

df.to_excel('temp.xls')