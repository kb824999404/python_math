from sklearn.datasets import load_digits
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

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


def train():    #用minist数据集训练神经网络
    X_train,X_test,Y_train,Y_test=generateData()
    clf=MLPClassifier(activation='logistic',hidden_layer_sizes=(128,64,32,),
    alpha=1e-5,random_state=1,max_iter=1000,verbose=False)
    clf.fit(X_train,Y_train)
    score=clf.score(X_test,Y_test)
    print('score=',score)
    yhat=clf.predict(X_test)
    print(classification_report(Y_test,yhat))



if __name__=='__main__':
    train()
    print("Hello")
    

