import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import KFold


def loadData():
    data=np.loadtxt('data/alldata.txt')
    X=data[:-1]
    X=X.T
    Y=data[-1]
    return X,Y


if __name__=='__main__':
    X,Y=loadData()
    kf=KFold(n_splits=10)
    yTrue=None
    yHat=None

    pls=PLSRegression(n_components=4,scale=False)      #PLSR回归
    for train_index,test_index in kf.split(X):      #交叉验证
        trainX,testX=X[train_index],X[test_index]
        trainY,testY=Y[train_index],Y[test_index]        
        pls.fit(trainX,trainY)   
        c_pred=pls.predict(testX)[:,0]
        if yTrue is None:
            yTrue=testY
            yHat=c_pred
        else:
            yTrue=np.r_[yTrue,testY]
            yHat=np.r_[yHat,c_pred]

    print(np.abs(yTrue-yHat)/yTrue*100)
    print(np.sum(np.abs(yTrue-yHat)/yTrue*100)/X.shape[0]) 

    #画图
    plt.rcParams['font.sans-serif'] = ['SimHei'] 
    plt.rcParams['axes.unicode_minus'] = False 
    plt.xlabel('预测值')
    plt.ylabel('真值')
    #画点
    plt.scatter(yHat,yTrue,color='r')
    #直线y=x
    ymin=xmin=np.min(yTrue)
    ymax=xmax=np.max(yTrue)
    plt.plot([xmin,xmax],[ymin,ymax])
    plt.annotate('y=x',xy=(xmax,ymax),xytext=(0,-20),textcoords='offset points',fontsize=18)

    plt.show()

