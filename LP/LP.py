import numpy as np
import scipy.optimize as so

def func1(x):        #定义被优化函数
    ans=-(4*x[0]+2*x[1]+3*x[2])
    return ans


def problem1():
    fun1=lambda x:160-7*x[0]-3*x[1]-6*x[2]       #约束条件
    fun2=lambda x:200-4*x[0]-4*x[1]-5*x[2]
    _constraints=({'type':'ineq','fun':fun1},{'type':'ineq','fun':fun2})   #转化为字典，ineq不等于
    _bounds=((0,30),(0,50),(0,40))                 #优化范围
    result=so.minimize(func1,(5,5,5),method='SLSQP',
    bounds=_bounds,constraints=_constraints)
    print(result)

def func2(x):
    a=[13,9,10,11,12,8]
    z=0
    for i in range(len(x)):
        z+=a[i]*x[i]
    return z


def problem2():
    fun1=lambda x:400-x[0]-x[3]       #约束条件
    fun2=lambda x:600-x[1]-x[4]
    fun3=lambda x:500-x[2]-x[5]
    fun4=lambda x:800-0.4*x[0]-1.1*x[1]-x[2]
    fun5=lambda x:900-0.5*x[3]-1.2*x[4]-1.3*x[5]
    _constraints=({'type':'eq','fun':fun1},{'type':'eq','fun':fun2},
    {'type':'eq','fun':fun3},{'type':'ineq','fun':fun4},{'type':'ineq','fun':fun5})   #转化为字典，ineq不等于
    _bounds=((0,400),(0,600),(0,500),(0,400),(0,600),(0,500))                 #优化范围
    result=so.minimize(func1,(200,100,100,100,100,100),method='SLSQP',
    bounds=_bounds,constraints=_constraints)
    print(result)

if __name__=='__main__':
    problem2()