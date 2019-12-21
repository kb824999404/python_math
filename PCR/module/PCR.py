import numpy as np
from module.PCA import PCA
from module.MLR import MLR

class PCR:
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y
    def confirmPCs(self):           #用PCA类对数据进行SVD分解，计算特征值比值
        self.pca=PCA(self.X)
        compare=self.pca.SVDdecompose()
        return compare
    def fit(self,PCs):              #用独立主成分进行多元线性回归
        T,P=self.pca.PCAdecompose(PCs)
        self.P=P
        # one=np.ones(T.shape[0])
        # X=np.c_[one,T]
        self.mlr=MLR(T,self.Y)          #X=TPt    T=XP
        self.mlr.fit()
        self.A=self.P.dot(self.mlr.A)        #Y=TA=XPA
    def predict(self,Xnew):           #预测未知样本
        yhat=Xnew.dot(self.A)
        return yhat



