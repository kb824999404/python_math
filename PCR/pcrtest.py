from module.PCR import PCR
import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':
    data=np.loadtxt('data/alldata.txt')
    X=data[:-1]
    X=X.T
    Y=data[-1]
    testX=X[::10]               #测试样本，间隔10取一个
    testY=Y[::10]
    trainX=np.delete(X,np.arange(X.shape[0])[::10],axis=0)         #去掉测试样本得到训练样本
    trainY=np.delete(Y,np.arange(Y.shape[0])[::10],axis=0)
    pcr=PCR(trainX,trainY)                  
    compare = pcr.confirmPCs()              #分解降维，得到特征值比值
    print(compare)
    k=int(input("确定主成分数："))
    pcr.fit(k)
    yHat=pcr.predict(testX)
    print('预测值：',yHat)
    err=(testY-yHat)/testY*100              #计算误差
    print('误差(%)：',err)

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