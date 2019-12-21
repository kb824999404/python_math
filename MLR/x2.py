from module.MLR import MLR
import numpy as np
import matplotlib.pyplot as plt

def showResult(mlr):
    x=np.arange(-10,12,0.1)
    x2=x**2
    X=np.c_[x,x2]
    Y=mlr.Y
    Ypre=mlr.predict(X)
    xvalue=[X[i] for i in range(len(X))]
    plt.plot(x,Ypre,'ro')                             #画出直线
    plt.plot(mlr.X[:,0],Y,'bo')                  #画出样本点
    plt.show()

if __name__=='__main__':
    data=np.loadtxt('data/x2+2x+1.txt')
    x=data[:,0]
    x2=x**2
    X=np.c_[x,x2]
    Y=data[:,1]
    mlr=MLR(X,Y)
    mlr.fit()
    showResult(mlr)