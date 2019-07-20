
weekday='一二三四五六七'
weekid=eval(input('please enter number betwwn1-7\n'))
print('星期'+weekday[weekid-1])

#十二星座
for i in range(12):
    print(chr(9800+i),end='')
print('\n')
#format详解
print('{0:=^10},{1:,.2f}'.format(23,123476.897))#%百分号不是加而是计算

#time repository,文本进度条
import  time
scale=10
print('执行开始'.center(scale*2,'-'),end='\n')
start=time.perf_counter()
for i in range(scale+1):
    a='*'*i
    b='-'*(scale-i)
    c=(i/scale)*100
    print('\r{:^3.0f}%[{}-->{}]'.format(c,a,b),end='')
    time.sleep(0.5)
end=time.perf_counter()
dur=end-start
print('执行结束'.center(scale*2,'-'),end='\n')
print('the duration time is:{}'.format(dur))