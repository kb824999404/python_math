import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from matplotlib.colors import ListedColormap


def loadData():
    data=load_iris().data
    target=load_iris().target
    X=data[target!=2]
    y=target[target!=2]
    ally=[]
    for i in range(len(y)): # 转正交编码
        if (y[i]==1):
            oneY=[0,1]
        else:
            oneY=[1,0]
        ally.append(oneY)
    Y=np.array(ally)
    return train_test_split(X,Y,test_size=0.2)

if __name__=='__main__':
    trainX,testX,trainY,testY=loadData()
    k=2
    pls=PLSRegression(n_components=k,scale=True)      #PLSR回归
    pls.fit(trainX,trainY)     
    yTrainType=[]  # 训练集样本类别整理
    for item in trainY:
        yTrainType.append(np.argmax(item))
    yTrainType=np.array(yTrainType)
   
    T=pls.x_scores_                 #X在新的主成分空间中的样本新坐标

    #计算测试集样本的得分                            
    xavg=trainX.mean(axis=0)
    xStd=trainX.std(axis=0)
    X_test=(testX-xavg)/xStd #数据预处理
    Tpred=None  # 记录测试集得分
    for i in range(2):
        t=X_test.dot(pls.x_weights_[:,i])
        if Tpred is None:
            Tpred=t
        else:
            Tpred=np.c_[Tpred,t]
        X_test=X_test-np.outer(t,pls.x_loadings_[:,i])
    yTestType=[]  # 整理测试集样本的类别
    for item in testY:
        yTestType.append(np.argmax(item))

    cm_bright = ListedColormap(['#FF0000', '#0000FF'])
    ax = plt.subplot(1, 1, 1)
    # 画训练集点
    ax.scatter(T[:, 0], T[:, 1], c=yTrainType,cmap=cm_bright, s=25)
    # 画测试集点 
    ax.scatter(Tpred[:, 0], Tpred[:, 1], c=yTestType,  edgecolors='black', s=45)

    #堆叠概率等高线图，从二维得分空间转化到原始空间，设残差矩阵为0
    x_min = T[:, 0].min() - .5
    x_max = T[:, 0].max() + .5
    y_min = T[:, 1].min() - .5
    y_max = T[:, 1].max() + .5
    h = .2  

    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),  np.arange(y_min, y_max, h))

    Tmoni = np.c_[xx.ravel(), yy.ravel()]
    Xmoni = Tmoni.dot(pls.x_loadings_.T)  # 转换到原始变量空间，假残差为0
    Xmoni +=xavg
    Xmoni *=xStd
    ymoniPred=pls.predict(Xmoni)  # 预报样本的函数值，每个样本2个值
    exp = np.exp(ymoniPred)
    sumExp = np.sum(exp, axis=1, keepdims=True)
    softmax = exp / sumExp   #  转每类的概率
    Z = softmax [:, 0] # 选择第一类的概率输出
    # 制作概率的等高线图
    Z = Z.reshape(xx.shape)
    CS = ax.contour(xx,yy, Z, 6, colors='k',) # 负值将用虚线显示             
    ax.clabel(CS, fontsize=9, inline=1)
    plt.show()


