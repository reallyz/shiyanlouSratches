import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#一般来说，X轴式分类数据，Y轴是数值型数据
path=r"E:\baidudownloads\FORAI\Python-7\(贪心学院）Python基础+机器学习\机器学习集训营资料\第三周\自行车数据实例"
daydf=pd.read_csv(path+r'\day.csv',parse_dates=[1],engine='python')
hourdf=pd.read_csv(path+r'\hour.csv',parse_dates=[1],engine='python')
droplist=['instant', 'season', 'yr', 'mnth', 'holiday', 'workingday', 'weathersit', 'atemp', 'hum']
daydf.drop(labels=droplist,axis=1,inplace=True)
print(daydf.head())
#print(daydf.info(),'\n',hourdf.info())
# TODO 画图参数配置
import  matplotlib
matplotlib.rc('figure',figsize=(14,7))
matplotlib.rc('font',size=14)
matplotlib.rc('axes.spines',top=False,right=False)
matplotlib.rc('axes',grid=False)
matplotlib.rc('axes',facecolor='white')
plt.hist(daydf['windspeed'].values,bins=40)#单维度分析
# TODO 多维度分析，散点图，离散值与离散值之间
from matplotlib import font_manager
fonp=font_manager.FontProperties()
fonp.set_family('SimHei')
fonp.set_size(14)
# TODO 画图变量的细节设置
def scatterplot(x_data,y_data,x_label,y_label,title):
    fig,ax=plt.subplots()
    ax.scatter(x_data,y_data,s=10,color='#539caf',alpha=0.75)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
scatterplot(x_data = daydf['temp'].values
            , y_data = daydf['cnt'].values
            , x_label = 'Normalized temperature (C)'
            , y_label = 'Check outs'
            , title = 'Number of Check Outs vs Temperature')
# TODO 拟合线性回归
import  statsmodels.api as sm
from  statsmodels.stats.outliers_influence import summary_table#获得信息汇总
x=sm.add_constant(daydf['temp'])#temp作为自变量，并添加常数项
y=daydf['cnt']
regr=sm.OLS(y,x)#ordinary least square model
res=regr.fit()# fit之后获得一个对象，用summary_table去调用这个对象
st, data, ss2 = summary_table(res, alpha=0.05) # 置信水平alpha=5%，st数据汇总，data数据详情，ss2数据列名
fitted_values = data[:,2]
# TODO 画出拟合后的曲线


def lmlineplot(x_data,y_data,x_label,y_label,title):
    fig,ax=plt.subplots()
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.plot(x_data,y_data,lw=2,alpha=1)#lw=linewidth，alpha=transparancy


lmlineplot(daydf['temp'],fitted_values,
           x_label='Normalized temperature (C)'
           , y_label='Check outs'
           , title='Number of Check Outs vs Temperature(lm)'
           )

# TODO 带置信区间的拟合结果
# 获得5%置信区间的上下界，得预先知道，fit后data里的结构
predict_mean_ci_low, predict_mean_ci_upp = data[:,4:6].T

# 创建置信区间DataFrame，上下界
CI_df = pd.DataFrame(columns = ['x_data', 'low_CI', 'upper_CI'])
CI_df['x_data'] = daydf['temp']
CI_df['low_CI'] = predict_mean_ci_low
CI_df['upper_CI'] = predict_mean_ci_upp
CI_df.sort_values('x_data', inplace = True) # 根据x_data进行排序,因为回归的时候是排过序的，要保持一致
# 绘制
def lineplotCI(x_data, y_data, sorted_x, low_CI, upper_CI, x_label, y_label, title):
    # 创建绘图对象
    fig, ax = plt.subplots()
    # 绘制预测曲线
    ax.plot(x_data, y_data, lw = 1, color = '#539caf', alpha = 1, label = 'Fit')
    ax.fill_between(sorted_x,low_CI,upper_CI,color = '#539caf', alpha = 0.5, label = '95%CI')
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend(loc='best')
lineplotCI(daydf['temp'],fitted_values,CI_df['x_data'],CI_df['low_CI'],CI_df['upper_CI'],
           x_label='Normalized temperature (C)'
           , y_label='Check outs'
           , title='Number of Check Outs vs Temperature(lm with CI)')

# TODO 双坐标曲线
#•曲线拟合不满足置信阈值时，考虑增加独立变量
#•分析不同尺度多变量的关系
#share x axis
def lineplot2y(x_data, x_label, y1_data, y1_color, y1_label, y2_data, y2_color, y2_label, title):
    fig,ax=plt.subplots()
    ax.plot(x_data,y1_data,color=y1_color,label=y1_label)
    ax.set_ylabel(y1_label,color=y1_color)
    ax.set_title(title)
    ax.legend(loc='upper left')
    ax1=ax.twinx()
    ax1.plot(x_data,y2_data,color=y2_color,label=y2_label)
    ax1.set_ylabel(y2_label,color=y2_color)
    ax1.spines['right'].set_visible(True)
    ax1.legend(loc='upper right')

lineplot2y(x_data = daydf['dteday']
           , x_label = 'Day'
           , y1_data = daydf['cnt']
           , y1_color = '#539caf'
           , y1_label = 'Check outs'
           , y2_data = daydf['windspeed']
           , y2_color = '#7663b0'
           , y2_label = 'Normalized windspeed'
           , title = 'Check Outs and Windspeed Over Time')
#TODO 组间分析，定量比较，分组粒度，组间聚类
#groupby,很多函数都有，看自己怎么组合在一起了
cnt_day=daydf[['weekday','cnt']].groupby('weekday').agg(['mean','std'])#必须droplevel，不然取不到值
cnt_day.columns=cnt_day.columns.droplevel()
def barplot(x_data, y_data, error_data, x_label, y_label, title):
    fig,ax=plt.subplots()
    ax.bar(x_data,y_data,color='#539caf',align='center')
    ax.errorbar(x_data, y_data, yerr=error_data, color='#297083',ls='None',lw=5)# ls='none'去掉bar之间的连线
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)

barplot(x_data = cnt_day.index.values
        , y_data = cnt_day['mean']
        , error_data = cnt_day['std']
        , x_label = 'Day of week'
        , y_label = 'Check outs'
        , title = 'Total Check Outs By Day of Week (0 = Sunday)')
#TODO 堆积柱状图，分类少的话，比饼图好看
mean_by_reg_co_day=daydf[['weekday','registered','casual']].groupby('weekday').mean()
# 分天统计注册和偶然使用的占比,这里归一化处理
mean_by_reg_co_day['total'] = mean_by_reg_co_day['registered'] + mean_by_reg_co_day['casual']
mean_by_reg_co_day['reg_prop'] = mean_by_reg_co_day['registered'] / mean_by_reg_co_day['total']
mean_by_reg_co_day['casual_prop'] = mean_by_reg_co_day['casual'] / mean_by_reg_co_day['total']


def stackedbarplot(x_data, y_data_list, y_data_names, colors, x_label, y_label, title):
    _, ax = plt.subplots()
    # 循环绘制堆积柱状图
    for i in range(0, len(y_data_list)):
        if i == 0:
            ax.bar(x_data, y_data_list[i], color = colors[i]
            ,align = 'center', label = y_data_names[i])
        else:
            # 采用堆积的方式，除了第一个分类，后面的分类都从前一个分类的柱状图接着画
            # 用归一化保证最终累积结果为1
            ax.bar(x_data, y_data_list[i], color = colors[i],
                   bottom = y_data_list[i - 1], align = 'center', label = y_data_names[i])
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc = 'upper right') # 设定图例位置
stackedbarplot(x_data = mean_by_reg_co_day.index.values
               , y_data_list = [mean_by_reg_co_day['reg_prop'], mean_by_reg_co_day['casual_prop']]
               , y_data_names = ['Registered', 'Casual']
               , colors = ['#539caf', '#7663b0']
               , x_label = 'Day of week'
               , y_label = 'Proportion of check outs'
               , title = 'Check Outs By Registration Status and Day of Week (0 = Sunday)')
#TODO 分组柱状图
#•多级类间绝对数值比较
def groupedbarplot(x_data, y_data_list, y_data_names, colors, x_label, y_label, title):
    _, ax = plt.subplots()
    # 设置每一组柱状图的宽度
    total_width = 0.8
    # 设置每一个柱状图的宽度
    ind_width = total_width / len(y_data_list)
    # 计算每一个柱状图的中心偏移
    alteration = np.arange(-total_width/2+ind_width/2, total_width/2+ind_width/2, ind_width)

    # 分别绘制每一个柱状图
    for i in range(0, len(y_data_list)):
        # 横向散开绘制
        ax.bar(x_data + alteration[i], y_data_list[i], color = colors[i], label = y_data_names[i], width = ind_width)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc = 'upper right')

# 调用绘图函数
groupedbarplot(x_data = mean_by_reg_co_day.index.values
               , y_data_list = [mean_by_reg_co_day['registered'], mean_by_reg_co_day['casual']]
               , y_data_names = ['Registered', 'Casual']
               , colors = ['#539caf', '#7663b0']
               , x_label = 'Day of week'
               , y_label = 'Check outs'
               , title = 'Check Outs By Registration Status and Day of Week (0 = Sunday)')


plt.show()