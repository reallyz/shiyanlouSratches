from sklearn import datasets
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier

iris=datasets.load_iris()
data=iris.data
target=iris.target

ks=[1,3,5,7,9,11,15]

kf=KFold(n_splits=5,random_state=2003,shuffle=True)

best_k=ks[0]
best_score=0
for k in ks:
    curr_score=0
    for train_index,valid_index in kf.split(data):# kfold返回的是切割成K份的索引
        clf=KNeighborsClassifier(n_neighbors=k)
        clf.fit(data[train_index],target[train_index])
        curr_score=curr_score+clf.score(data[valid_index],target[valid_index])
    avg_score=curr_score/5
    if avg_score>best_score:
        best_k=k
        best_score=avg_score
    print('current score is :{:.2%},best k is:{}'.format(best_score,best_k
                                                        ))
print('after cross validation the best k is :{}'.format(best_k))
#搜索最佳参数的函数
'''
模型选择函数GridSearch（网格搜索）不仅能搜索最佳参数，还能搜索最佳优化函数
para={'n_neighbors:[1,3,5,7,9,11]'}
knn=KNeighborsClassifier()
clf=GridSearchCV(knn,para,cv=5)
clf.fit(data,target)
print('best score is:{} and the best k is:{}'.format(clf.best_score_,clf.best_params_))
'''