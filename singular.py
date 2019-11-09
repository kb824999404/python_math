from MLR终版 import MLR
import numpy as np
data=np.loadtxt(r"singulartest.txt")
X=data[:,:-1]
Y=data[:,-1]
ones=np.ones(len(X))
X=np.c_[ones,X]
mlr=MLR(X,Y)
mlr.fit()
Yhat=mlr.predict(X)
print(((Yhat-Y)/Y*100).round(3))

