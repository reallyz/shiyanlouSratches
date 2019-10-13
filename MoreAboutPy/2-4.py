import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#对数据类型有要求,离散值(catalog类型），连续值
tips=sns.load_dataset('tips')
#分类子图，直接指定kind是什么
sns.factorplot(x="day", y="total_bill", hue="smoker", col="time", data=tips, kind="swarm")
#多分类子图，建立对象，然后用map贴上去
g = sns.PairGrid(tips,
                 x_vars=["smoker", "time", "sex"],
                 y_vars=["total_bill", "tip"],
                 aspect=.75, size=3.5)
g.map(sns.violinplot, palette="bright")