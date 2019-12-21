from module.NGA import NGA
import math
import numpy as np

def f1(x):
    f=x[0]**2+2*x[0]+1
    return f

def f2(v):
    f=(v[0]-4)**2+2*(v[1]+3)**2+(v[2]-4)**2
    return f

def f3(v):
    pred=[v[0]*v[1]*(math.exp(-v[1]*i)-math.exp(-v[2]*i))/(v[2]-v[1]) for i in x]
    error=y-pred
    s=sum(error*error)
    return s 

def test1():
    nga=NGA(10,1,0,90,100,f1)
    nga.solve()
    ans=nga.getAnswer()
    print(ans)

def test2():
    nga=NGA(10,3,0,90,100,f2)
    nga.solve()
    ans=nga.getAnswer()
    print(ans)

def test3():

    nga=NGA(10,3,0,90,2000,f3)
    nga.solve()
    ans=nga.getAnswer()
    print(ans)




if __name__=='__main__':
    # ma=np.loadtxt("data/data.txt")
    # x=ma[:,0]
    # y=ma[:,1]
    test1()