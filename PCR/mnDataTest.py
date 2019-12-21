from module.PCR import PCR
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def loadData():
    data=np.loadtxt('data/monidata.txt')
    X=data[:,:-1]
    Y=data[:,-1]
    return train_test_split(X,Y,test_size=0.2)

def showResult(testY,yHat):
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

if __name__=='__main__':
    trainX,testX,trainY,testY=loadData()
    pcr=PCR(trainX,trainY)                  
    compare = pcr.confirmPCs()              #分解降维，得到特征值比值
    print(compare)
    k=int(input("确定主成分数："))
    pcr.fit(k)
    yHat=pcr.predict(testX)
    print('预测值：',yHat)
    err=(testY-yHat)/testY*100              #计算误差
    print('误差(%)：',err)
    showResult(testY,yHat)
