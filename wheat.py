from PCA import PCA
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import PLSRegression

if __name__=='__main__':
    A=np.loadtxt("wheat_train_PCA_X.txt")
    B=np.loadtxt("wheat_train_PCA_Y.txt")
    aver=A.mean(axis=0)
    std=A.std(axis=0)
    A=(A-aver)/std
    pca=PCA(A)
    print(pca.SVDdecompose())
    T,P=pca.PCAdecompose(6)
    cls1=B==1.0
    cls2=B!=1.0
    plt.subplot(1,2,1)
    plt.title("PCA")
    plt.plot(T[cls1,0],T[cls1,1],'ro')
    plt.plot(T[cls2,0],T[cls2,1],'b^')



    pls=PLSRegression(n_components=4,scale=False)
    pls.fit(A,B)
    T=pls.x_scores_
    plt.subplot(1,2,2)
    plt.title("PLS")
    plt.plot(T[cls1,0],T[cls1,1],'ro')
    plt.plot(T[cls2,0],T[cls2,1],'b^')
    plt.show()

