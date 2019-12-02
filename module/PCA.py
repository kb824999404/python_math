import numpy as np

class PCA:
    def __init__(self,X):
        self.X=X
    def SVDdecompose(self):             #SVD分解
        B=np.linalg.svd(self.X,full_matrices=False)     #X=USV
        ld=B[1]
        compare=[]
        for i in range(len(ld)-1):
            temp=ld[i]/ld[i+1]          #计算相邻特征值的比值
            compare.append(temp)
        self.T=B[0]*B[1]                #T=US
        self.P=B[2].T                   #P=Vt
        return np.array(compare)
    def PCAdecompose(self,k):           #获取主成分
        T=self.T[:,:k]
        P=self.P[:,:k]
        return T,P