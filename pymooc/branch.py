#圆周率的计算，利用蒙特卡洛方法
from  random import random
from time import  perf_counter
darts=10000*10000
hits=0.0
start=perf_counter()
for i in range(1,darts+1):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits+=1
pi=4*(hits/darts)
end=perf_counter()
print('the pi is:{},and runtime is:{}'.format(pi,end-start))


#formation
pi1=0
n=100
start1=perf_counter()
for k in range(n):
    pi1+=1/pow(16,k)*(\
        4/(8*k+1)-2/(8*k+4)\
        -1/(8*k+5)-1/(8*k+6))
end1=perf_counter()
print('the format pi is:{},and runtime is:{}'.format(pi1,end1-start1))