import math
class Point():
    def __init__(self,coordinate,sampleClass):
        self.coordinate=coordinate
        self.sampleClass=sampleClass
    
    def getDistance(self,otherPoint):
        diff=[self.coordinate[i]-otherPoint.coordinate[i] for i in range(len(self.coordinate))]
        temp=[item*item for item in diff]
        result=math.sqrt(sum(temp))
        self.distance=result


p1=Point([1.0,2.0],1)
p2=Point([1.1,2.3],1)
p3=Point([1.3,2.5],1)
p4=Point([1.2,2.2],1)

p5=Point([8.0,4.2],-1)
p6=Point([7.7,4.7],-1)
p7=Point([8.1,4.3],-1)
p8=Point([7.9,4.5],-1)

X=[p1,p2,p3,p4,p5,p6,p7,p8]


while True:
    x,y=map(float,input('Please input the coordinate of the point:').split(','))
    if x==0 and y==0:
        break
    k=int(input('Please input the number of the sample:'))
    unKnow=Point([x,y],0)
    for point in X:
        point.getDistance(unKnow)
    
    X.sort(key=lambda o:o.distance)
    result=[X[i].sampleClass/X[i].distance for i in range(k)]
    result=sum(result)
    if result>0:
        unKnow.sampleClass=1
    else:
        unKnow.sampleClass=-1
    print(unKnow.sampleClass)
