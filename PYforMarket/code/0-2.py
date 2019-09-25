import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import mpl_finance

def stockpriceplot(ticker):
    # 1 load data
    path='/root/PycharmProjects/shiyanlouSratches/PYforMarket/data/eachstock/'+ticker+'.csv'
    data=pd.read_csv(path,parse_dates=True,index_col=0)
    # 2 transform data
    # 2.1 close price per 5m
    close=data['close']
    close=close.reset_index()
    close['date']=close['date'].map(matplotlib.dates.date2num)
    subplot1=plt.subplot2grid((2,1),(0,0))
    subplot1.xaxis_date()
    plt.plot(close['date'],close['close'],'b.')
    # 2.2 ohlc price per 1h
    ohlc=data[['open','close','high','low']].resample('1H').ohlc()
    ohlc=ohlc.reset_index()
    ohlc['date']=ohlc['date'].map(matplotlib.dates.date2num)
    subplot2=plt.subplot2grid((2,1),(1,0),sharex=subplot1)
    subplot2.xaxis_date()
    mpl_finance.candlestick_ohlc(ax=subplot2,quotes=ohlc.values,
                                 width=0.01,colorup='r',colordown='g')

    plt.show()

stockpriceplot('000725')