from collections import Counter

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

# counter return a counter dictionary
iris =datasets.load_iris()
x=iris.data
y=iris.target
X_Train,X_Test,Y_train,Y_test=train_test_split(x,y,random_state=2003)
'''
clf=KNeighborsClassifier(n_neighbors=3)
clf.fit(X_Train,Y_train)
correct=np.count_nonzero((clf.predict(X_Test)==Y_test)==True)  # number of correct
print('the accuracy of if:{:.2%}'.format(correct/len(X_Test)))
'''
# knn written on my own
def euc_dist(i1,i2):
    zipls=list(zip(i1,i2))
    sum =0
    for i in zipls:
        sum=sum+(i[0]-i[1])**2
    '''
    dist=np.sqrt(sum((i1-i2)**2))
    针对array(向量)数据类型：对应相减
    '''
    return sum


def knn_classify(X,y,testI,k):
    dists={}
    for i,n in enumerate(X):
        dists[i]=euc_dist(n,testI)
    tep=sorted(dists.items(),key=lambda x:x[1])
    output=tep[:k]
    ls=[]
    for i in output:
        ls.append(y[i[0]])
    finalout=Counter(ls)
    if len(finalout)==k:
        return ls[0]
    else:
        f=tuple(finalout.items())
        return f[-1][0]
    '''
    另一种解法
    dists=[euc_dist(x,testI) for x in X]
    kneighbors=np.argsort(dists)[:k]#由小到大排序，输出是下标
    count=Counter(y[kneighbors])
    return count.most_common()[0][0]
    '''
predictions=[knn_classify(X_Train,Y_train,data,3) for data in X_Test]
correct=np.count_nonzero((predictions==Y_test)==True)
print('the accuracy of if:{:.2%}'.format(correct/len(X_Test)))