from datetime import datetime

datetime.now()
dt=datetime(2020,9,5,12,12,00)    #默认时区信息是none
print(dt)
print(dt.timestamp())        #人为统一的时间,1970年1月1日 00:00:00 UTC+00:00
t=10000
print(datetime.fromtimestamp(t))

#str,datetime相互转换
cday=datetime.strptime('2015-7-1 17:17:17','%Y-%m-%d %H:%M:%S')
print(cday)
print(datetime.now().strftime('%a,%b %d %H:%M'))
#datetime加减
from datetime import timedelta
print(dt+timedelta(days=1))
print(dt-timedelta(hours=21))
#时区的转换
from  datetime import  timezone
tz=timezone(timedelta(hours=8))   #utc+8
t=10000
print(datetime.fromtimestamp(t,tz=tz))#带有时区
dtz=datetime(2011,4,1,12,12,12,tzinfo=tz) #默认时区信息是none
print(dtz)
#时区转换 astimezone()
tokyo=dtz.astimezone(timezone(timedelta(hours=1))) #utc的时间加减都是相对于utc=0来的，所以时区转换时把基准放在utc=0比较好
print(tokyo)
#习题
import re
def to_timestamp(dt_str,tz_str):
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    tz=re.match(r'UTC(.)(\d):\d{2}',tz_str)
    hours=int(tz.group(2))
    flag=tz.group(1)
    if flag=='+':
        return (dt-timedelta(hours=hours)).timestamp()
    else:
        return (dt+timedelta(hours=hours)).timestamp()


