import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split

def loadData():
    data=np.loadtxt('data/alldata.txt')
    X=data[:-1]
    X=X.T
    Y=data[-1]
    return train_test_split(X,Y,test_size=0.5)

def findBest():
    trainX,testX,trainY,testY=loadData()
    s=[]
    for i in range(10):
        pls=PLSRegression(n_components=i+1,scale=False)      #PLSR回归
        pls.fit(trainX,trainY)   
        yHat=pls.predict(testX)[:,0]
        err=(testY-yHat)/testY*100
        err=err.round(3)
        s.append(np.abs(err).sum())
    return s.index(min(s))
    

if __name__=='__main__':
    k=findBest()
    print(k)
    trainX,testX,trainY,testY=loadData()


    pls=PLSRegression(n_components=k,scale=False)      #PLSR回归
    pls.fit(trainX,trainY)   
    yHat=pls.predict(testX)[:,0]
    err=(testY-yHat)/testY*100
    err=err.round(3)
    print(err)

    #画图
    plt.rcParams['font.sans-serif'] = ['SimHei'] 
    plt.rcParams['axes.unicode_minus'] = False 
    plt.xlabel('预测值')
    plt.ylabel('真值')
    #画点
    plt.scatter(yHat,testY,color='r')
    #直线y=x
    ymin=xmin=np.min(testY)
    ymax=xmax=np.max(testY)
    plt.plot([xmin,xmax],[ymin,ymax])
    plt.annotate('y=x',xy=(xmax,ymax),xytext=(0,-20),textcoords='offset points',fontsize=18)

    plt.show()

