from MLR终版 import MLR
import numpy as np
import math

if __name__=='__main__':
    data=np.loadtxt('lndata.txt')
    X=data[:,:-1]
    one=np.ones(X.shape[0])
    Xs=np.c_[one,X]
    Y=data[:,-1:]
    lnY=np.log(Y)                   #对样本输出取对数
    mlr=MLR(Xs,lnY)
    mlr.fit()                       #求解模型
    print(mlr.Ftest(0.01))          #检验模型
    A=mlr.getCoef()                 
    print('model:','lnQ={} + {} a+ {} b'.format(A[0][0],A[1][0],A[2][0]))   #输出线性回归模型
    eA=np.e**A                                                              #对线性回归模型取幂
    print('model:','Q={} * {} ^a * {} ^b'.format(eA[0][0],eA[1][0],eA[2][0]))
    print('predict:',np.e**mlr.predict(Xs))     