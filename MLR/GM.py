import numpy as np
from module.MLR import MLR


if __name__=='__main__':
    x0=np.array([89677,99215,109655,120333,135823,159878,182321,209407,246619,300670])
    x1=np.cumsum(x0)
    B=[-(x1[i]+x1[i+1])/2.0 for i in range(len(x1)-1) ]
    B=np.array(B)
    oneCol=np.ones(B.shape[0]) 
    B= np.c_[B,oneCol]
    y=x0[1:]
    mlr=MLR(B,y)
    mlr.fit()
    a=mlr.A[0]
    u=mlr.A[1]
    x1hat=[]
    for k in range(1,len(x0)+3):                #预测后续2年
        x1hat.append((x0[0]-u/a)*np.exp(-a*(k-1))+u/a)
    x0hat=[x1hat[i+1]-x1hat[i] for i in range(len(x1hat)-1) ]
    x0hat.insert(0,x0[0])
    print(x0hat)

