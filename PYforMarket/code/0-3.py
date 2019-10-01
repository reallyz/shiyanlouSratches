import matplotlib.pyplot as plt
import numpy
import pandas as pd
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential

# goal is use one hour data to predict 5 hours trend
CONST_TRAINING_SEQUENCE_LENGTH=12
CONST_TESTING_CLASS=2
def dataNormalization(data):
    # 为什么要做数据正规化？因为数据的尺度会造成影响，所以要正规化
    return [(datum-data[0])/data[0] for datum in data]#得到closeprice的变化率
def dataDenormalization(data,base):
    return [(datum+1)*base for datum in data]
def getDeeplearingdata(ticker):
    # 1.load data
    path='/root/PycharmProjects/shiyanlouSratches/PYforMarket/data/eachstock/'+ticker+'.csv'
    data=pd.read_csv(path)['close'].tolist()
    # 2.building training data
    dataTraining=[]
    for i in range(len(data)-CONST_TESTING_CLASS*CONST_TRAINING_SEQUENCE_LENGTH):
        dataSegment=data[i:i+CONST_TRAINING_SEQUENCE_LENGTH+1]#以一个区间长度截取数据
        dataTraining.append(dataNormalization(dataSegment))
    dataTraining=numpy.array(dataTraining)
    # np.random.shuffle(dataTraining)
    X_Training=dataTraining[:, :-1]
    Y_Training=dataTraining[:, -1]
    # 3.building testing data
    X_Testting=[]
    Y_Testing_Base=[]
    for i in range(CONST_TESTING_CLASS,0,-1):
        dataSegment=data[-(i+1)*CONST_TRAINING_SEQUENCE_LENGTH:-i*CONST_TRAINING_SEQUENCE_LENGTH]
        Y_Testing_Base.append(dataSegment[0])
        X_Testting.append(dataNormalization(dataSegment))

    Y_Testing=data[-CONST_TRAINING_SEQUENCE_LENGTH*CONST_TESTING_CLASS:]
    X_Testting=numpy.array(X_Testting)
    Y_Testing=numpy.array(Y_Testing)# Y_testing数据不用normalize，因为最后的预测数据要denormalize
    # 4.reshape for deep learning
    X_Training=numpy.reshape(X_Training,(X_Training.shape[0],X_Training.shape[1],1),order='C')
    X_Testing=numpy.reshape(X_Testting,(X_Testting.shape[0],X_Testting.shape[1],1),order='C')
    return X_Training,Y_Training,X_Testing,Y_Testing,Y_Testing_Base

def predict(model,X):
    predictionNormalized=[]
    for i in range(len(X)):
        data=X[i]
        result=[]
        for j in range(CONST_TRAINING_SEQUENCE_LENGTH):
            predicted=model.predict(data[numpy.newaxis,:,:])[0,0]
            result.append(predicted)
            data=data[1:]
            data=numpy.insert(data,[CONST_TRAINING_SEQUENCE_LENGTH-1],predicted,axis=0)
        predictionNormalized.append(result)
    return predictionNormalized
def plotResults(Y_hat,Y):
    plt.plot(Y)
    for i in range(len(Y_hat)):
        padding=[None for _ in range(i*CONST_TRAINING_SEQUENCE_LENGTH)]
        plt.plot(padding+Y_hat[i])
    plt.show()

def predictLSTM(ticker):

    # 1.load data
    X_Training, Y_Training, X_Testing, Y_Testing, Y_Testing_Base=getDeeplearingdata(ticker)
    # 2.build model
    model=Sequential()
    model.add(LSTM(
        input_dim=1,
        output_dim=50,
        return_sequences=True
    ))
    model.add(Dropout(0.2))
    model.add(LSTM(
        200,
        return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(output_dim=1))
    model.add(Activation('linear'))
    model.compile(loss='mse',optimizer='rmsprop')
    # 3.train model
    model.fit(X_Training,Y_Training,
              batch_size=512,
              nb_epoch=5,
              validation_split=0.05)
    # 4.predict
    predictionNormalized=predict(model,X_Testing)

    # 5.de-nomalize
    predictions=[]
    for i,row in enumerate(predictionNormalized):
        predictions.append(dataDenormalization(row,Y_Testing_Base[i]))
    # 6.plot
    plotResults(predictions,Y_Testing)


def main():
    predictLSTM('000498')


if __name__ == '__main__':
    main()