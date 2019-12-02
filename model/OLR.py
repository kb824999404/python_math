import matplotlib.pyplot as plt 
import numpy as np
from scipy.stats import f  

    
class OLR:
    def __init__(self, X,Y):
        one=np.ones(len(X))
        self.X=np.c_[one,X]
        self.Y=Y
    def fit(self):
        XT=self.X.T
        tmp=np.dot(XT,self.X)
        inv=np.linalg.inv(tmp)
        tmp=np.dot(inv,XT)
        self.A=np.dot(tmp,self.Y)
    def getCoef(self):
        return self.A
    def predict(self,XNew):
        one=np.ones(len(XNew))
        X=np.c_[one,XNew]
        return X.dot(self.A)
    def showResult(self):
        a=self.A
        x=self.X[:,1]
        y=self.Y
        print("model is {:10.3f}+{:10.3f}x".format(a[0],a[1]))        #输出直线
        xvalue=[x[i] for i in range(len(x))]
        xmin=min(xvalue)                            
        xmax=max(xvalue)
        xp=[xmin,xmax]
        yp=[a[1]*xmin+a[0],a[1]*xmax+a[0]]
        plt.plot(x,y,'bo')                  #画出样本点  按两种类型分两种颜色
        plt.plot(xp,yp)                             #画出直线
        plt.rcParams['font.sans-serif'] = ['SimHei'] 
        plt.rcParams['axes.unicode_minus'] = False 
        plt.title('一元线性回归')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
    def Ftest(self,alpha):  # 给定置信度alpha
        x=self.X[:,1]
        n=len(x)   # 获取样本数
        f_arfa=f.isf(alpha, 1, n-2)   # f临界值
        Yaver=self.Y.mean()   # y平均值
        Yhat=self.predict(x)  #预测y
        U=((Yhat-Yaver)**2).sum()  #U值
        Qe=((self.Y-Yhat)**2).sum()  #Qe值
        F=U/(Qe/(n-2))   # f值
        answer=[F,f_arfa,F>f_arfa]  # 返回F、f临界、F>临界
        return answer

    

if __name__=='__main__':
    data=np.loadtxt(r'2.txt')
    X=data[0]
    Y=data[1]
    mlr=OLR(X,Y)
    mlr.fit()
    print(mlr.Ftest(0.01))
    mlr.showResult()
    # print(X)
    # print(Y)
    # print(mlr.getCoef())
    # print(mlr.predict(X))
