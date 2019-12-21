import numpy as np

if __name__=='__main__':
    x=np.arange(-3,3,1)
    y=np.arange(-3,3,1).T
    z=x.dot(y)
    print(x,y,z)
    print('{:6.2f}'.format(3.1416))
    L=[]
    L.append("Hello")
    L.append(1)
    print(L)
    x=[[1,2],[3,4]]
    y=[[5,6],[7,8]]
    print(x+y)
    x.extend(y)
    print(x)