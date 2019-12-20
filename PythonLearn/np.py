import numpy as np
import math     

def test1():
    a=np.linspace(0,math.pi*2,50)
    b=np.sin(a)
    mask=b>=0
    print(a)
    print(b[mask])
    print(a[mask])

def test2():
    a=np.arange(0,100,10)
    b=np.where(a<50)
    print(a[b[0]])

def test3():
    a = np.array([[1,2], [3, 4], [5, 6]])
    print(a[[0, 1, 2], [0, 1, 0]]) 

def FO():
    a=np.arange(0,100,10)
    file_name="1.npy"
    np.save(file_name,a)

def FI():
    file_name="1.npy"
    b=np.load(file_name)
    print(b)

def FZ():
    a=np.arange(0,100,10)
    b=np.linspace(0,100,5)
    c=np.sin(b)
    np.savez("2.npz",a=a,b=b,c=c)
    arrs=np.load("2.npz")
    print(arrs.files)
    print(arrs['a'])
    print(arrs['b'])
    print(arrs['c'])

def FT():
    a=np.arange(0,100,10).reshape(1,10)  
    np.savetxt('3.txt',a,fmt="%d",delimiter=",")
    print(np.loadtxt('3.txt',dtype=int,delimiter=","))


if __name__=='__main__':
    FT()
