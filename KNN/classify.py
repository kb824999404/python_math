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
        plt.xlabel('x1')
        plt.ylabel('x2')
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

class PLA:      #感知器算法
    def __init__(self,x,y,rate,iterations):
        self.x=x
        self.y=y
        self.rate=rate
        self.iterations=iterations

    def inference(self):
        #算法
        a=[1,1]         #初始化系数
        b=1
        for i in range(self.iterations):                        #指定迭代次数
            loss,temp=self.lossF(a,b)                #计算损失函数
            print(loss)
            if(loss==0):
                break
            for j in range(len(temp)):
                if temp[j] <0:                      #如果误判样本，则按公式调节系数
                    a[0] +=self.rate*self.y[j]*self.x[j][0]        #调整斜率
                    a[1] +=self.rate*self.y[j]*self.x[j][1]    
                    b +=self.rate*self.y[j]                   #调整截距
        self.a=a
        self.b=b
        self.showResult()
    
    def lossF(self,a,b):  # x 是2维列表，每行一个样本, y是样本分类符，
        temp=[]
        for one in self.x:
            temp1=[one[i]*a[i] for i in range(len(one))]
            temp1=sum(temp1)+b   # 每个样本的 a1x1+a2x2+b的取值
            temp.append(temp1)
        temp2=[]
        for i in range(len(temp)):
            temp2.append(temp[i]*self.y[i])   # 每个样本函数值与真值的乘积
        s=0
        for i in temp2:
            s += max(0,-i)   # 计算损失函数，每项取负值，即误判样本
        return s,temp2  # temp2返回有用，用于找误判，调节系数

    def showResult(self):
        a=self.a
        b=self.b
        x=self.x
        y=self.y
        print("model is {:10.3f}x1+{:10.3f}x2+{:10.3f}".format(a[0],a[1],b))        #输出直线

        xvalue=[x[i][0] for i in range(len(x))]
        xmin=min(xvalue)                            
        xmax=max(xvalue)
        xp=[xmin,xmax]
        yp=[-a[0]/a[1]*xmin-b/a[1],-a[0]/a[1]*xmax-b/a[1]]
        cls1x=[x[i][0] for i in range(len(x)) if y[i]==-1]          
        cls2x=[x[i][0] for i in range(len(x)) if y[i]==1]
        cls1y=[x[i][1] for i in range(len(x)) if y[i]==-1]
        cls2y=[x[i][1] for i in range(len(x)) if y[i]==1]
        plt.plot(cls1x,cls1y,'b^')                  #画出样本点  按两种类型分两种颜色
        plt.plot(cls2x,cls2y,'r^')
        plt.plot(xp,yp)                             #画出直线
        plt.rcParams['font.sans-serif'] = ['SimHei'] 
        plt.rcParams['axes.unicode_minus'] = False 
        plt.title('感知器算法')
        plt.xlabel('x1')
        plt.ylabel('x2')
        plt.show()


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


if __name__=='__main__':
    file='山-变色鸢尾花瓣.txt'
    x=getMat(file)
    file='山-变色鸢尾花瓣分类.txt'
    y=getMat(file)
    knn=KNN(x,y)                                                            #使用KNN类进行模式识别
    knn.readUnKnow([[6.2,3.1],[4.8,3.8]],3)
    knn.inference()
    pla=PLA(x,y,0.01,10000)
    pla.inference()
    


