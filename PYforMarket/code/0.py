import tushare
import pandas as pd
import datetime
#cn
tickersRawData=tushare.get_stock_basics()
path='../data/'
datetody=datetime.datetime.today().strftime('%Y%m%d')
tickersRawData.to_csv(path+datetody+'.csv')
