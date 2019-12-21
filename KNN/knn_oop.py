import numpy as np
from module.KNN import KNN


def loadData():
    x=[ [4.9, 3. ],  [4.7, 3.2], [4.6, 3.1], [5. , 3.6], [5.4, 3.9],            #准备数据
        [4.6, 3.4], [5. , 3.4 ], [4.4, 2.9], [4.9, 3.1]]
    x1=[ [6.1, 3. ],  [5.8, 2.6], [5. , 2.3], [5.6, 2.7],
        [5.7, 3. ],  [5.7, 2.9],  [6.2, 2.9], [5.1, 2.5],  [5.7, 2.8]]
    x.extend(x1)
    y=[ -1, -1, -1, -1, -1, -1, -1, -1, -1]
    y1=[ 1, 1, 1, 1, 1, 1, 1, 1, 1]
    y.extend(y1)
    return x,y

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
    return x,y

if __name__=='__main__':
    x,y=loadDataByFile()
    knn=KNN(x,y)                                                            #使用KNN类进行模式识别
    knn.readUnKnow([[5.1,3.5],[5.5,2.6],[5.,5.]],3)
    knn.inference()

