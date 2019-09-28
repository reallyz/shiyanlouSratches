import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

path=''
df=pd.read_csv(path)

# one-hot encoding for catagro data
df_colors=df['Color'].str.get_dummies().add_prefix('color:')
df_type=df['Type'].apply(str).str.get_dummies().add_prefix('type:')# type is numerical data originally,not string
df=pd.concat([df,df_colors,df_type],axis=1)

matrix=df.corr()
f,ax=plt.subplots(figsize=(8,6))
sns.heatmap(matrix,square=True)
plt.title('')

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X=df[['f1','f2','f3']]
y=df['label'].values.reshape(-1,1)
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

# N(0,1)for all ,after normalize the discrete data transform to for regression
X_norm=StandardScaler()
x_train=X_norm.fit_transform(x_train)
x_test=X_norm.transform(x_test)

Y_norm=StandardScaler()
y_train=Y_norm.fit_transform(y_train)
y_test=Y_norm.transform(y_test)

knn=KNeighborsClassifier(n_neighbors=2)
knn.fit(x_train,y_train.ravel())

y_pred=knn.predict(x_test)
y_pred_inv=Y_norm.inverse_transform(y_pred)
y_test_inv=Y_norm.inverse_transform(y_test)

# the raw data
plt.scatter(y_pred_inv,y_test_inv)
plt.xlabel('predict data')
plt.ylabel('the real data')

# add perfect prediction line
diagonal=np.linspace(500,1500,100)
plt.plot(diagonal,diagonal,'-r')
plt.show()

print(y_pred_inv)
knn

