import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
path='/root/baidunetdiskdownload/公司财务数据挖掘/FDDC_financial_data/FDDC_financial_data/Macro&Industry.xlsx'
df=pd.read_excel(path,sheet_name='数据信息')
dfid=pd.read_excel(path,sheet_name='指标信息',usecols='A:B')
for i in range(len(dfid)):
    tep=dfid.iloc[i,:].values
    id=tep[0]
    name=tep[1]
    plt.figure(name)
    sns.lineplot(x='PERIOD_DATE',y='DATA_VALUE',data=df[df['indic_id']==id])
    plt.savefig(name+'.jpg')
    plt.close()
