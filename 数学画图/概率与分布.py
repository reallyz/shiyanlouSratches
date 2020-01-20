from scipy.stats import binom,expon
import matplotlib.pyplot as plt
import numpy as np


# 离散型的，二项分布
plt.subplot(311)
n=100
p=0.5
mean,var,skew,kurt=binom.stats(n,p,moments='mvsk')
# ppf:累积分布函数的反函数。q=0.01时，ppf就是p(X<x)=0.01时的x值
x=np.arange(binom.ppf(0.01,n,p),binom.ppf(0.99,n,p))# 离散的
# 分布律
plt.plot(x,binom.pmf(x,n,p),'o')

# 连续型的，指数分布
plt.subplot(312)
plt.title('概率密度')
lambdax=1/5
loc=0
scale=1/lambdax
means,vars,skews,kurts=expon.stats(loc,scale,moments='mvsk')
xx=np.linspace(expon.ppf(0.01,loc,scale),expon.ppf(0.99,loc,scale),100)
#概率密度
plt.plot(xx,expon.pdf(xx,loc,scale),label='expon')
plt.subplot(313)
plt.title('分布函数')
plt.plot(xx,1-np.exp(-lambdax*xx),'*')
plt.show()
print(xx[-1],1-np.exp(-lambdax*x[-1]))



