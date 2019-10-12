import pandas as pd
import numpy as np
#more about pandas
# groupby,agg,concat,merge,
salaries = pd.DataFrame({
    'Name':['BOSS', 'HanMeimei', 'HanMeimei', 'Han', "BOSS", "BOSS", "HanMeimei", "BOSS"],
    "Year":[2017,2017,2017,2017,2018,2018,2018,2018],
    "Salary":[40000, 5000, 4000, 3000, 38000, 42000, 6000, 39000],
    'Bonus':[12000, 3000, 3500, 1200, 16000, 18000, 7000, 21000]
})
groupby_name=salaries.groupby('Name')#返回一个groupby对象
for item in groupby_name:
    print(type(item))  #tuple
    print(item[0])      #name
    print(type(item[1])) #datafram

#对groupby后的数据可以做聚合操作
print(groupby_name.sum(),groupby_name.mean()
      ,groupby_name.median())
print(groupby_name.size())#求index的频次
print(salaries.groupby('Name')[['Bonus','Salary']].mean())#筛选操作

#多重分组,只有通过聚合操作，才能打印，不然返回的就是一个对象
#groupby里面的就是index
print(salaries.groupby(['Name','Year'],sort=False).median())#index完全相同才相加
#用聚合函数（agg)做统计运算
print(salaries.groupby('Name')[['Bonus','Salary']].agg(['sum','mean','std','median']))#直接写
print(salaries.groupby('Name')[['Bonus','Salary']].agg([np.sum,np.mean,np.std,np.median]))#传入numpy的统计函数
#高级特性，广播和apply,对某一列变换得到另外一列，如果是简单操作，直接用广播特性；如果是复杂变换，记得用apply
print(salaries)
#广播,向量特性，可以多个向量表示一个向量，线性表出
salaries.loc[:,'my_salary']=salaries['Salary']*2-1000
print(salaries)
#apply也可
salaries.loc[:,'my_salary_apply']=salaries['Salary'].apply(lambda x:x*2-1000)
print(salaries)
#取数据可以用逻辑表达式
print(salaries.loc[(salaries['Salary']>4000)&(salaries['Bonus']>5000),['Name','Salary','Bonus']])
salaries.drop(['my_salary','my_salary_apply'],axis=1,inplace=True)
salaries.loc[:,'Name']=salaries['Name'].apply(lambda x:x if x!='Han' else 'HY')#匿名函数式直接返回值
print(salaries)
#高级函数的综合应用，如果式boss返回工资加奖金，如果是员工，返回工资
def mount(name,salary,bouns):
    if name=='BOSS':
        return salary+bouns
    else:
        return salary
salaries['Welfare']=list(map(mount,salaries['Name'],salaries['Salary'],salaries['Bonus']))
print(salaries)
#s数据的拼接和合并
#拼接，按行，按列
df1 = pd.DataFrame({
    'apts':[55000, 60000],
    'cars':[200000, 300000],
}, index = ['Beijing', 'Shanghai']
)
df2 = pd.DataFrame({
    'apts':[35000, 45000],
    'cars':[150000, 180000],
}, index = ['Hangzhou', 'Guangzhou']
)
df3 = pd.DataFrame({
    'apts':[30000, 40000],
    'cars':[120000, 100000],
}, index = ['Nanjing', 'Guangzhou']
)
dfrow=pd.concat([df1,df2,df3],axis=0)
dfcol=pd.concat([df1,df2,df3],axis=1)
print(dfrow,'\n',dfcol)
#合并，按某列做关联,how类似与SQL
dfmer=pd.merge(df1,df2,left_index=True,right_index=True,how='outer')
print(dfmer)
#join，基于index做关联,q其实merge也可以做到
print(dfmer.info())

