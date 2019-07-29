import matplotlib.pyplot as plt
import numpy as np
import matplotlib
#matplotlib.rcParams['font.family']='msbm10'全局修改
'''
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

a=np.arange(0.0,5.0,0.02)
plt.subplot(211)
plt.plot(a,f(a))
plt.subplot(212)
plt.plot(a,np.cos(a*2*np.pi),'r--')
#plt.show()
'''
plt.figure(2)
b=np.arange(10)
plt.xlabel('左边',fontproperties='Droid Sans Fallback')
plt.plot(-b,b*2,'bd-',b,b*3,b,b*4)
plt.figure(3)
#饼图
plt.subplot(3,3,1)
labels='frogs','hogs','dogs','logs'
sizes=[15,30,45,10]
explods=0,0.1,0,0
plt.pie(sizes,explode=explods,labels=labels,autopct='%1.1f%%',
        shadow=False,startangle=90)
plt.axis('equal')
plt.title('Pie')
plt.subplot(3,3,2)
np.random.seed(0)
mu,sigma=100,20
a=np.random.normal(mu,sigma,size=100)
plt.hist(a,20,density=1)
plt.title('hist')
ax=plt.subplot(334)
ax.set_title('scatter-object')
ax.plot(10*np.random.randn(100),10*np.random.randn(100),'o')
ax=plt.subplot(338,projection='polar')
n=20
theta=np.linspace(0.0,2*np.pi,n,endpoint=False)
radii=10*np.random.rand(n)
width=np.pi/4*np.random.rand(n)
bars=ax.bar(theta,radii,width=width)
'''
更好看,cm=colormap
for r,bar in zip(radii,bars):
    bar.set_facecolor(plt.cm.viridis(r/10.))
    bar.set_alpha(0.5)
'''
plt.figure(4,figsize=(12,6))
from scipy.io import wavfile
rateh,hstrain=wavfile.read('H1_Strain.wav','rb')
ratel,lstrain=wavfile.read('L1_Strain.wav','rb')
reftime,ref_h1=np.genfromtxt('wf_template.txt').transpose()
htime_interval=1/rateh
ltime_interval=1/ratel
htime_len=hstrain.shape[0]/rateh
ltime_len=lstrain.shape[0]/ratel
htime=np.arange(-htime_len/2,htime_len/2,htime_interval)
ltime=np.arange(-ltime_len/2,ltime_len/2,ltime_interval)
plth=plt.subplot(221)
plth.plot(htime,hstrain,'y')
plth.set_xlabel('Time(seconds)')
plth.set_ylabel('H1 Strain')
plth.set_title('H1 Strain')
pltl=plt.subplot(222)
pltl.plot(ltime,lstrain,'g')
pltl.set_xlabel('Time(seconds)')
pltl.set_ylabel('L1 Strain')
pltl.set_title('L1 Strain')
pltr=plt.subplot(212)
pltr.plot(reftime,ref_h1)
pltr.set_xlabel('Time(seconds)')
pltr.set_ylabel('Template Strain')
pltr.set_title('Template')
plt.show()