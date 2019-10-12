import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats,integrate
import pandas as pd
import warnings


warnings.filterwarnings('ignore')
sns.set(color_codes=True)
plt.rcParams['axes.unicode_minus']=False
titanic=sns.load_dataset('titanic')
tips=sns.load_dataset('tips')
iris=sns.load_dataset('iris')
#seaborn相对matplotlib更简单，不用贴图
#强大的绘图工具，seaborn 基于numpy,数据类型最好用numpy
#一维分布，多维相关性，回归，hue是非常好用
#一维数据
x=np.random.normal(size=100)
print(type(titanic['age'].values))
sns.distplot(x,kde=True,rug=True,fit=stats.gamma)
#(kernel density estimation)近似的连续分布,rug:实例
#sns.distplot(titanic['age'].values,kde=True)
plt.figure('核密度')
sns.kdeplot(x)#单独绘制核密度函数，集中趋势
#plt.figure('双变量')#两两相关性
mean,cor=[0,1],[(1,.5),(.5,1)]
data=np.random.multivariate_normal(mean,cor,200)
df=pd.DataFrame(data,columns=['x','y'])
sns.jointplot(x='x',y='y',data=df)
sns.jointplot(x='x',y='y',data=df,kind='kde')#连续化，更好看,还可以对坐标轴对象操作，更好看
sns.pairplot(iris)
#直接对句柄进行操作
g=sns.PairGrid(iris)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.kdeplot)
plt.show()