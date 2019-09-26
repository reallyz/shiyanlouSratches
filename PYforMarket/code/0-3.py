import numpy as np
import pandas as pd

# goal is use one hour data to predict 5 hours trend
CONST_TRAINING_SEQUENCE_LENGTH=60
CONST_TESTING_CLASS=5
def dataNormalization(data):
    #为什么要做数据正规化？
    return [(datum-data[0])/data[0] for datum in data]#得到closeprice的变化率
def dataDenormalization(data,base):
    return [(datum+1)*base for datum in data]
def getDeeplearingdata(ticker):
    # 1.load data
    path='/root/PycharmProjects/shiyanlouSratches/PYforMarket/data/eachstock/'+ticker+'.csv'
    data=pd.read_csv(path)['close'].to_numpy()
    # 2.building training data
    dataTraining=[]
    for i in range(len(data)-CONST_TRAINING_SEQUENCE_LENGTH):
        dataSegment=data[i:i+CONST_TRAINING_SEQUENCE_LENGTH+1]#以一个区间长度截取数据
        dataTraining.append(dataNormalization(dataSegment))
    dataTraining=np.array(dataTraining)
    np.random.shuffle(dataTraining)
    X_Training=dataTraining[:,:-1]
    Y_Training=dataTraining[:,-1]
    # 3.building testing data

    # 4.reshape for deep learning
    return
    pass
def predictLSTM(ticker):
    pass
    # 1.load data
    # 2.build model
    # 3.train model
    # 4.predict
    # 5.de-nomalize
    # 6.plot