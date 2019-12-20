from sklearn.neural_network import MLPRegressor
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.cross_decomposition import PLSRegression

import numpy as np

def generateData():
    digits=load_diabetes()
    X=digits.data
    Y=digits.target
    split=train_test_split(X,Y,test_size=0.05)
    return split

if __name__=='__main__':
    X_train,X_test,Y_train,Y_test=generateData()

    clf=MLPRegressor(hidden_layer_sizes=(128,64,32,16),alpha=1e-5,random_state=1)
    clf.fit(X_train,Y_train)
    YPred=clf.predict(X_test)
    err=(Y_test-YPred)/Y_test*100
    err=err.round(3)
    print(err)