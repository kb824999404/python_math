import numpy as np
import matplotlib.pyplot as plt
from module.PCA import PCA



if __name__=='__main__':
    A = np.loadtxt("data/wheat_train_PCA_X.txt")
    B=np.loadtxt("data/wheat_train_PCA_Y.txt")
    aver=A.mean(axis=0)
    std=A.std(axis=0)
    A=(A-aver)/std
    pca=PCA(A)
    print(pca.SVDdecompose())
    T,P=pca.PCAdecompose(6)
    cls1=B==1.0
    cls2=B!=1.0
    plt.plot(T[cls1,0],T[cls1,1],'ro')
    plt.plot(T[cls2,0],T[cls2,1],'b^')
    plt.show()