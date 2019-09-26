from sklearn import datasets,linear_model
import numpy as np
import  matplotlib.pyplot as plt

data=np.array([[152,51],[156,53],[160,54],[164,55],
               [168,57],[172,60],[176,62],[180,65],
               [184,69],[188,72]])
print(data.shape)
x=data[:,0].reshape(-1,1)
y=data[:,1]
plt.plot(x,y)

lmodel=linear_model
l=lmodel.LinearRegression()
regr=l.fit(x,y)
y_pred=regr.predict(x)
plt.plot(x,y_pred)
print(l.coef_)
plt.show()