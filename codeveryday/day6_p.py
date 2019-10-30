# 跑马灯
'''
content="Julia,I really need you to go to the doctor and get some medicine! "
while True:
    os.system('clear')
    print(content)
    time.sleep(0.2)
    content=content[1:]+content[0]
'''
#获取文件后缀名
def getsuffix(filname,has_dot=False):
    flag=filname.rfind('.')
    if flag!=-1:
        index=flag if has_dot else flag+1
    return filname[index:]
import time
#计算传入的日期是这一年的第几天
def calNoD(year,month,day):
    s=str(year)+str(month)+str(day)
    t=time.mktime(time.strptime(s,"%Y%m%d"))
    result=time.localtime(t).tm_yday
    return result
print(calNoD(2017,5,12))

#随机函数的应用，双色球选号，打印
from  random import randint, sample
def selectballs():
    red_balls=[x for x in range(1,35)]
    select=[]
    n=6
    select=sample(red_balls,n)
    select.append(randint(1,16))
    return select
def printsel(select):
    for i in range(len(select)-1):
        print("%02d"%select[i],end=' ')

    print('| {0}'.format(select[-1]))
    print('\n')

# 格式化输出还有一种
a,b=10,15
print(f'{a}.{b}\n')
print("print 5 group\n")
for _ in range(5):
    s=selectballs()
    printsel(s)
