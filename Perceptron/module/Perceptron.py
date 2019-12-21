import matplotlib.pyplot as plt
import numpy as np



class Perceptron():         #感知器算法
    def __init__(self,X,Y):
        one=np.ones(X.shape[0])
        print(one)
        self.X=np.c_[one,X]
        self.Y=Y
        

    def lossF(self):        #损失函数
        temp=[]
        temp=self.X.dot(self.a)
        temp=np.sum(temp,axis=1)        # 每个样本的 a1x1+a2x2+b的取值
        temploss=temp*self.Y                 # 每个样本函数值与真值的乘积
        loss=0                          # 计算损失函数，每项取负值，即误判样本
        for i in range(temploss.shape[0]):
            loss+=max(0,-temploss[i])  
        self.temp=temploss  # temploss返用于找误判，调节系数
        self.loss=loss      


    def fit(self,rate,epochs):  #训练模型
        #算法
        self.a=np.array([1.0,1.0,1.0]).reshape(3,1)         #初始化系数
        for i in range(epochs):                        #指定迭代次数
            self.lossF()                #计算损失函数
            print(self.loss)
            for j in range(self.temp.shape[0]):
                if self.temp[j] <0:                      #如果误判样本，则按公式调节系数
                    self.a[0] +=rate*self.Y[j]                   #调整截距
                    self.a[1] +=rate*self.Y[j]*self.X[j][1]        #调整斜率
                    self.a[2] +=rate*self.Y[j]*self.X[j][2]    
        print("model is {}x1+{}x2+{}".format(self.a[1],self.a[2],self.a[0]))        #学习结束，输出直线

    def showResult(self):       #显示结果
        xmin=np.min(self.X,axis=0)[1]
        xmax=np.max(self.X,axis=0)[1]
        xp=np.array([xmin,xmax])
        yp=[-self.a[1]/self.a[2]*xmin-self.a[0]/self.a[2],
        -self.a[1]/self.a[2]*xmax-self.a[0]/self.a[2]]
        cls1x=[self.X[i][1] for i in range(self.X.shape[0]) if self.Y[i]==-1]
        cls2x=[self.X[i][1] for i in range(self.X.shape[0]) if self.Y[i]==1]        
        cls1y=[self.X[i][2] for i in range(self.X.shape[0]) if self.Y[i]==-1]
        cls2y=[self.X[i][2] for i in range(self.X.shape[0]) if self.Y[i]==1]
        plt.plot(cls1x,cls1y,'b^')                  #画出样本点  按两种类型分两种颜色
        plt.plot(cls2x,cls2y,'r^')
        plt.plot(xp,yp)                             #画出直线
        plt.show()