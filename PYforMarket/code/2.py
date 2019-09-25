import pandas as pd
import echarts_china_provinces_pypkg
from pyecharts import Map
import pandas as pd
data=pd.read_csv('/root/PycharmProjects/shiyanlouSratches/'
                 'PYforMarket/data/tickersrawdata.csv')
province=data['area']
out=province.value_counts()
keys=list(out.index)
values=list(out.values)
ls=list(map(lambda x:x/max(values)*100,values))
maps=Map('Distribution of Listed Company',width=1200,height=600)
maps.add('RI',keys,ls,visual_range=[0,100],maptype='china',
        is_visualmap=True,is_label_show=True,visual_text_color='#000')
maps.render('RI.html')

