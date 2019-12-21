from module.MLR import MLR
import numpy as np

A=np.loadtxt('data/mul.txt')
X=A[:,1]
Y=A[:,0]
Xs=np.c_[X,X**2,X**3]
mlr=MLR(Xs,Y)
mlr.fit()
print(mlr.getCoef())
