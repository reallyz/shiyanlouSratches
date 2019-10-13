
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")
sns.set(color_codes=True)

tips = sns.load_dataset("tips")

#变量间的关系，回归,数值型数据，出现在坐标轴上的都是数值型数据，因变量一定是连续值
#1均连续值
sns.lmplot(x='total_bill',y='tip',data=tips)
#2.1 X离散值，处理方法：加抖动
sns.lmplot(x='size',y='tip',x_jitter=0.08,data=tips)
#2.2 离散值用均值和置信区间代替,还可以其他的方法，np的不容易出错
sns.lmplot(x='size',y='tip',data=tips,x_estimator=np.mean,ci=95)
#3高阶拟合。这种还原已知数据有用，做预测容易overfitting

#变量间的关系，hue
sns.lmplot(x='total_bill',y='tip',hue='smoker',data=tips,markers=['o','x'])
#更多的分类条件
sns.lmplot(x='total_bill',y='tip',hue='smoker',col='day',row='sex',data=tips)
plt.show()