import numpy as np
from module.Perceptron import Perceptron

def getMat(file):
    s = [];   f=open(file,'r')
    s=f.readlines();  data=[]
    for row in s:
        oneRow=row.split()
        if len(oneRow)==1:
            oneData=float(oneRow[0])
        else:
            oneData=list(map(float, oneRow))
        data.append (oneData)
    return data 


def loadDataByFile():
    file='data/山-变色鸢尾花瓣.txt'
    x=getMat(file)
    file='data/山-变色鸢尾花瓣分类.txt'
    y=getMat(file)
    X=np.array([a for b in x for a in b])      #拉成一维，再转化成二维，否则无法转化为array
    X=X.reshape(int(X.shape[0]/2),2)           
    Y=np.array(y)
    return X,Y

def loadData():
    X=np.loadtxt('data/山-变色鸢尾花瓣.txt')
    Y=np.loadtxt('data/山-变色鸢尾花瓣分类.txt')
    return X,Y

if __name__=='__main__':
    # x,y=loadDataByFile()
    x,y=loadData()    
    print(x,y)
    cla=Perceptron(x,y)
    cla.fit(0.1,1000)
    cla.showResult()

