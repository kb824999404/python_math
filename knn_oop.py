import numpy as np
import matplotlib.pyplot as plt

class KNN():
    class Point():                                                                  #定义点类，便于保存样本点坐标、类别和计算距离
        def __init__(self,coordinate,sampleClass):                              
            self.coordinate=coordinate
            self.sampleClass=sampleClass
        
        def getDistance(self,otherPoint):
            diff=[self.coordinate[i]-otherPoint.coordinate[i] for i in range(len(self.coordinate))]
            temp=[item*item for item in diff]
            result=np.sqrt(sum(temp))
            self.distance=result

    def __init__(self,X,Y):                                         #用Point类保存已知样本点
        self.points=[]
        self.sampleNum=len(X)
        for i in range(self.sampleNum):
            self.points.append(self.Point(X[i],Y[i]))
        
    def readUnKnow(self,X,k):                           #保存未知样本点和投票样本数
        self.unKnows=[]
        self.voteNum=k
        for i in range(len(X)):
            self.unKnows.append(self.Point(X[i],0))

    def inference(self):                                #根据已知样本点识别未知样本点类别并显示结果
        for unKnow in self.unKnows:                     #计算未知样本与所有已知样本的距离
            for point in self.points:
                point.getDistance(unKnow)               
            
            self.points.sort(key=lambda o:o.distance)    #将样本按距离从小到大排列
            result=[self.points[i].sampleClass/self.points[i].distance for i in range(self.voteNum)]       #对新样本进行投票表决
            result=sum(result)                          
            if result>0:
                unKnow.sampleClass=1
            else:
                unKnow.sampleClass=-1
        self.showResult()

    def showResult(self):
        for unKnow in self.unKnows:                             #输出未知样本点类别
            print(unKnow.coordinate,':',unKnow.sampleClass)
        for point in self.points:                               #画出已知样本点
            self.drawPoint(point,False)
        for unKnow in self.unKnows:                             #画出未知样本点
            self.drawPoint(unKnow,True)
        plt.rcParams['font.sans-serif'] = ['SimHei'] 
        plt.rcParams['axes.unicode_minus'] = False 
        plt.title('KNN模式识别')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        
    def drawPoint(self,point,flag):                            #画点，如果为未知样本点，则标注其坐标
        x=point.coordinate[0]
        y=point.coordinate[1]
        if point.sampleClass==1:
            plt.scatter(x,y,color='y',marker='s')
        else:
            plt.scatter(x,y,color='b',marker='^')
        if flag:
            plt.annotate(r'$({},{})$'.format(x,y),xy=(x,y),xytext=(+20,-20),textcoords='offset points',fontsize=12,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))


if __name__=='__main__':
    x=[ [4.9, 3. ],  [4.7, 3.2], [4.6, 3.1], [5. , 3.6], [5.4, 3.9],            #准备数据
        [4.6, 3.4], [5. , 3.4 ], [4.4, 2.9], [4.9, 3.1]]
    x1=[ [6.1, 3. ],  [5.8, 2.6], [5. , 2.3], [5.6, 2.7],
        [5.7, 3. ],  [5.7, 2.9],  [6.2, 2.9], [5.1, 2.5],  [5.7, 2.8]]
    x.extend(x1)
    y=[ -1, -1, -1, -1, -1, -1, -1, -1, -1]
    y1=[ 1, 1, 1, 1, 1, 1, 1, 1, 1]
    y.extend(y1)
    knn=KNN(x,y)                                                            #使用KNN类进行模式识别
    knn.readUnKnow([[5.1,3.5],[5.5,2.6],[5.,5.]],3)
    knn.inference()

