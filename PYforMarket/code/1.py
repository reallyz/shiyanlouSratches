
import pandas as pd
import datetime
#usa get data online on my own
datetoday=datetime.datetime.today().strftime('%Y%m%d')
'''对于规范的结构以下代码适用
url='http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download'
dataString=requests.get(url).content
tickersrawdata=pd.read_csv(io.StringIO(dataString.decode('utf-8')),sep=None)#解码
path=

tickersrawdata.to_csv(path,index=False)
'''
import pandas_datareader as pdrusa
rawdata=pdrusa.get_nasdaq_symbols(timeout=10)
path='../data/'
rawdata.to_csv(path+datetoday+'usa.csv')

