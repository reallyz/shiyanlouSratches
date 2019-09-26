import os

import pandas as pd
import tushare


#cn
def stockprice(ticker,folder):
    # 1 get data online
    data=tushare.get_hist_data(ticker,ktype='5')
    data.sort_index(inplace=True)
    # 2 if history exists append
    path=folder+ticker+'.csv'
    if os.path.exists(path):
        historyd=pd.read_csv(path,index_col=0)#把哪一列当作index
        data.append(historyd)
    # 3 inverse based on index
    # 4 save
    data.to_csv(path)


tickersRawData=tushare.get_stock_basics()
tickers=tickersRawData.index.tolist()#交易代码
path='../data/tickersrawdata.csv'
if os.path.exists(path):
    history=pd.read_csv(path)
    tickersRawData.append(history)
tickersRawData.to_csv(path)


for i,ticker in enumerate(tickers):
    print(i,'/',len(tickers))
    #time.sleep(2)
    try:
        stockprice(ticker,folder='../data/eachstock/')
    except:
        pass
    '''
    if i>2:
        break
    '''