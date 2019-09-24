import numpy as np
import matplotlib.pyplot as plt

class KNN():
    class Point():
        def __init__(self,coordinate,sampleClass):
            self.coordinate=coordinate
            self.sampleClass=sampleClass
        
        def getDistance(self,otherPoint):
            diff=[self.coordinate[i]-otherPoint.coordinate[i] for i in range(len(self.coordinate))]
            temp=[item*item for item in diff]
            result=np.sqrt(sum(temp))
            self.distance=result

    def __init__(self,X,Y):
        self.points=[]
        self.sampleNum=len(X)
        for i in range(self.sampleNum):
            self.points.append(self.Point(X[i],Y[i]))
        
    def readUnKnow(self,X,k):
        self.unKnows=[]
        self.voteNum=k
        for i in range(len(X)):
            self.unKnows.append(self.Point(X[i],0))

    def inference(self):
        for unKnow in self.unKnows:
            for point in self.points:
                point.getDistance(unKnow)
            
            self.points.sort(key=lambda o:o.distance)
            result=[self.points[i].sampleClass/self.points[i].distance for i in range(self.voteNum)]
            result=sum(result)
            if result>0:
                unKnow.sampleClass=1
            else:
                unKnow.sampleClass=-1
        self.showResult()

    def showResult(self):
        for unKnow in self.unKnows:
            print(unKnow.coordinate,':',unKnow.sampleClass)
        for point in self.points:
            self.drawPoint(point,False)
        for unKnow in self.unKnows:
            self.drawPoint(unKnow,True)
        plt.show()
        
    def drawPoint(self,point,flag):
        x=point.coordinate[0]
        y=point.coordinate[1]
        if point.sampleClass==1:
            plt.scatter(x,y,color='y',marker='s')
        else:
            plt.scatter(x,y,color='b',marker='^')


if __name__=='__main__':
    x=[ [4.9, 3. ],  [4.7, 3.2], [4.6, 3.1], [5. , 3.6], [5.4, 3.9],
        [4.6, 3.4], [5. , 3.4 ], [4.4, 2.9], [4.9, 3.1]]
    x1=[ [6.1, 3. ],  [5.8, 2.6], [5. , 2.3], [5.6, 2.7],
        [5.7, 3. ],  [5.7, 2.9],  [6.2, 2.9], [5.1, 2.5],  [5.7, 2.8]]
    x.extend(x)
    y=[ -1, -1, -1, -1, -1, -1, -1, -1, -1]
    y1=[ 1, 1, 1, 1, 1, 1, 1, 1, 1]
    y.extend(y1)
    knn=KNN(x,y)
    knn.readUnKnow([[5.1,3.5],[5.5,2.6]],3)
    knn.inference()

