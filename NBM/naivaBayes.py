from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np

if __name__=='__main__':
    iris=datasets.load_iris()
    x=iris.data
    y=iris.target
    xtrain,xtest,ytrain,ytest=train_test_split(x,y)
    bayes=GaussianNB()
    model=bayes.fit(xtrain,ytrain)
    pred=model.predict(xtest)
    error=pred-ytest
    print(error)
    print(classification_report(ytest,pred))