import numpy as np
import matplotlib.pyplot as plt
import  seaborn as sns
plt.rcParams['axes.unicode_minus']=False

x=np.linspace(0,50,200)
y=np.cos(x)-x
plt.figure(1)
plt.plot(x,y)
plt.figure(2)
plt.plot(x,np.cos(x))
plt.plot(x,x)
plt.show()