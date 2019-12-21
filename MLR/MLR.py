import numpy as np
from scipy.stats import f  

class MLR:
    def __init__(self,X,Y):
        one=np.ones(X.shape[0])       #将原来的X加上全为1的一列
        self.X=np.c_[one,X]
        self.Y=Y
    def modelling(self):          #根据公式求解回归系数
        XT=self.X.T
        XTX=np.dot(XT,self.X)
        XTXinv=np.linalg.inv(XTX)
        tmp=np.dot(XTXinv,XT)
        self.A=np.dot(tmp,self.Y)
        print(self.A.shape)
    def getCoef(self):      
        return self.A
    def showCoef(self):
        A=self.A
        size=A.shape
        for i in range(size[0]):
            for j in range(size[1]):
                print(A[i][j],'\t',end="")
            print()
    def predict(self,XNew):     #用求得的模型预测未知样本
        one=np.ones(len(XNew))
        X=np.c_[one,XNew]
        return X.dot(self.A)
    def Ftest(self,alpha):  # 给定置信度alpha
        x=self.X[:,1:]
        n=x.shape[0]  # 获取样本数
        Y=self.Y.T
        Yhat=self.predict(x).T  #预测y
        answers=[]
        for j in range(len(Y)):             #依次验证每个方程的显著性
            F,f_arfa=[],[]
            Yaver=np.mean(Y[j])  # y平均值
            U=((Yhat[j]-Yaver)**2).sum()  #U值
            Qe=((Y[j]-Yhat[j])**2).sum()  #Qe值
            for i in range(x.shape[1]):     #依次检验方程中的每个系数
                k=i+1
                f_arfa.append(f.isf(alpha, k, n-k-1))  # f临界值
                F.append((U/k)/(Qe/(n-k-1)))        # f值
            answer=[[(F[i]>f_arfa[i]) for i in range(len(F))]]  # 返回F、f临界、F>临界
            answers.append(answer)
        return answers

if __name__=='__main__':
    data=np.loadtxt('data/mlr_test_data.txt')
    X=data[:,:4]
    Y=data[:,4:]
    print(X.shape)
    print(Y.shape)
    mlr=MLR(X,Y)
    mlr.modelling()
    mlr.showCoef()
    print(mlr.Ftest(0.01))