from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier

def generateData():
    from module.ImageDigit import ImageDigit
    img=Image.open('data/digit/digit (1).jpg')
    imageDigit=ImageDigit(img)
    imageDigit.histShow()
    thresold=int(input("请输入闸值："))
    imageDigit.convert_to_bw(threshold=thresold)
    digits=imageDigit.split()
    imageDigit.to_32_32('digits_32')
    X,Y=imageDigit.featureExtract()
    return X,Y

def getDigits():
    from sklearn.datasets import load_digits
    from sklearn.metrics import confusion_matrix,classification_report
    from sklearn.preprocessing import LabelBinarizer
    digits = load_digits()
    X = digits.data
    y = digits.target
    labels = LabelBinarizer().fit_transform(y)
    return x,labels

def preprocessData(X,Y):
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    X=StandardScaler().fit_transform(X)
    return train_test_split(X,Y,test_size=0.1)

def predict(clf,X_test,y_test,is_test):
    score=clf.score(X_test,y_test)
    print("Score:",score)
    yhat=clf.predict(X_test)
    if is_test:
        print("Predit:",yhat)
        print("Real:",y_test)
    print('-'*20)


if __name__=='__main__':
    X,Y=generateData()
    # X,Y=getDigits()
    X_train, X_test, y_train, y_test=preprocessData(X,Y)
    clf=MLPClassifier(solver='lbfgs',hidden_layer_sizes=(64),alpha=1e-5,random_state=1,max_iter=8000)
    clf.fit(X_train,y_train)
    print('-'*20)
    print('Train Data:')
    predict(clf,X_train,y_train,False)
    print('Test Data:')
    predict(clf,X_test,y_test,True)

