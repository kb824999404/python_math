import numpy as np
from module.Perceptron import Perceptron


def loadData():
    #数据准备
    x1=np.array([[5.1, 3.5 ],  [4.9, 3. ],  [4.7, 3.2], [4.6, 3.1], [5. , 3.6], [5.4, 3.9],      #给定花瓣长宽   
        [4.6, 3.4], [5. , 3.4 ], [4.4, 2.9], [4.9, 3.1]])                          #山鸢尾
    x2=np.array([[5.5, 2.6 ],  [6.1, 3. ],  [5.8, 2.6], [5. , 2.3], [5.6, 2.7],                  #变色鸢尾
        [5.7, 3. ],  [5.7, 2.9],  [6.2, 2.9], [5.1, 2.5],  [5.7, 2.8]])
    X=np.vstack((x1,x2))
    y1=np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1])                            #分类数值       #山鸢尾
    y2=np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])                                                    #变色鸢尾
    Y=np.hstack((y1,y2))
    return X,Y 


if __name__=='__main__':
    x,y=loadData()
    cla=Perceptron(x,y)
    cla.fit(0.1,1000)
    cla.showResult()

