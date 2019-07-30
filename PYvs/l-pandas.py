import pandas as pd
import numpy as np
#两种数据类型，serise,dataframe
#serise
id=['a','b','c']
s=pd.Series(25,index=id)
dt={'one':[1,2,3],'two':[4,5,6]}
d=pd.Series(dt)
print(d)
nd=pd.Series(np.arange(4),index=id+['d'])
ls=pd.Series([1,2,3],index=id)
#基本操作类似于ndarray,dict
d.get('f',10)
print('one' in d)#只判断自定义索引
print(ls[ls>1],'\n',ls[['a','b']],'\n',ls[[0,1]],'\n',ls[:2],'\n') #选择
print(nd+s)#补齐原则，相同索引元素相加,不同索引置nan
d.name='so'
d.index.name='ind'#name属性
print(d)
#dataframe,基于serise
dfdt=pd.DataFrame(dt)
print(dfdt)
dfnd=pd.DataFrame(np.arange(12).reshape(3,4),index=id,columns=id+['d'])
print(dfnd)
print(dfdt.loc[0,'one'],',',dfdt.iloc[0,0])#获取元素，loc,可以是label,iloc必须是整数
#对索引进行重排
dfnd.reindex(index=['c','a','b'],columns=['d','a','c','b'])
print(dfdt.drop(labels='one',axis=1))
#累加函数，相关分析函数
