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

    mlp=MLPRegressor(hidden_layer_sizes=(20,), activation='logistic', solver='sgd', alpha=0.0001, 
    learning_rate='adaptive', learning_rate_init=0.1, power_t=0.5, 
    max_iter=5000,  random_state=1, tol=0.0001, verbose=False, warm_start=False, momentum=0.9)

    mlp.fit(X_train,Y_train)
    YPred=mlp.predict(X_test)
    err=(Y_test-YPred)/Y_test*100
    err=err.round(3)
    print(err)