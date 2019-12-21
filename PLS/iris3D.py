import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

def loadData():
    data=load_iris().data
    target=load_iris().target
    X=data[target!=2]
    Y=target[target!=2]
    Y[Y==0]=-1
    return train_test_split(X,Y,test_size=0.2)

if __name__=='__main__':
    trainX,testX,trainY,testY=loadData()
    k=2
    pls=PLSRegression(n_components=k,scale=False)      #PLSR回归
    pls.fit(trainX,trainY)        
    T=pls.x_scores_                 #X在新的主成分空间中的样本新坐标

    cls1=trainY==1.0                 #分两类
    cls2=trainY!=1.0

    plt.title("PLS")
    plt.plot(T[cls1,0],T[cls1,1],'ro')      #取T的前2列制图
    plt.plot(T[cls2,0],T[cls2,1],'b^')


    xavg=trainX.mean(axis=0) 
    testX=testX-xavg
    Tpred=None

    for i in range(k):
        t= testX.dot(pls.x_weights_[:,i])
        if Tpred is None:
            Tpred=t 
        else:
            Tpred=np.c_[Tpred,t]
        testX-=np.outer(t,pls.x_loadings_[:,i])

    plt.scatter(Tpred[:, 0], Tpred[:, 1], c=testY,  edgecolors='black', s=25)
    plt.show()
