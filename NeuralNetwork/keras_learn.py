from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report

from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense,Activation


import numpy as np


def generateData():     # 生成训练集和测试集
    digits=load_digits()
    X=digits.data
    Y=digits.target
    labels_y=LabelBinarizer().fit_transform(Y)
    print("X",X.shape)
    print("Y",labels_y.shape)
    split=train_test_split(X,labels_y,test_size=0.1)
    return split


if __name__ == "__main__":
    X_train,X_test,Y_train,Y_test=generateData()
    model=Sequential()
    model.add(Dense(units=100,activation='relu',input_dim=64))
    model.add(Dense(units=10,activation='softmax'))
    model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])
    model.fit(X_train,Y_train,epochs=20,batch_size=5)
    classes=model.predict(X_test,batch_size=5)
    predict=np.argmax(classes,axis=1)
    ytrue=np.argmax(Y_test,axis=1)
    err=ytrue-predict
    print(err)
    print(classification_report(ytrue,predict))
